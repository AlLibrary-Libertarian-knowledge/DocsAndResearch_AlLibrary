# Análise Arquitetural Profunda: AlLibrary

Este documento apresenta uma dissecação técnica e didática de todas as escolhas de engenharia feitas na concepção do **AlLibrary**. O objetivo é explicar o **porquê** de cada ferramenta, biblioteca e protocolo terem sido escolhidos, como eles interagem entre si, e como o projeto se diferencia de soluções existentes no mercado, como o IPFS e o OnionShare.

Este material serve como base definitiva de estudos para a defesa do Trabalho de Conclusão de Curso (TCC), garantindo total fluência técnica perante qualquer questionamento da banca examinadora.

---

## 1. O Núcleo do Aplicativo: Tauri v2, Rust e a Revolução do Tokio

Ao projetar um aplicativo Desktop moderno, a escolha padrão da indústria por muitos anos foi o Electron (usado no Discord, VSCode, etc.). No entanto, o AlLibrary exigia uma arquitetura radicalmente diferente devido às restrições de consumo de memória, necessidade de criptografia pesada e I/O de rede constante (P2P via Tor). 

### 1.1 Por que o Tauri v2?
O Tauri v2 foi escolhido porque ele altera o paradigma do desenvolvimento Desktop. Em vez de embutir um navegador inteiro (Chromium) pesado que consome gigabytes de RAM, o Tauri utiliza as ferramentas de renderização nativas (Webview) do próprio sistema operacional do usuário. 
Isso traz duas vantagens cruciais:
1. **Pacote Enxuto e Baixo Consumo de RAM:** O aplicativo final é leve, o que é vital para nós de uma rede P2P que precisam rodar em *background* sem incomodar o usuário.
2. **Isolamento de Segurança (Privilégio Mínimo):** O *frontend* (interface visual feita em SolidJS) não tem acesso direto ao sistema. Ele precisa pedir permissão ao *backend* via IPC (Inter-Process Communication). 

### 1.2 Por que Rust e Cargo?
O "motor" (backend) do Tauri é escrito em **Rust**. A linguagem Rust foi escolhida por três motivos fundamentais para um sistema P2P descentralizado:
* **Segurança de Memória:** Diferente de C ou C++, o compilador do Rust impede falhas como *buffer overflow* ou *dangling pointers*, sem a necessidade de um *Garbage Collector* imprevisível como no Java ou Go. Isso significa que o aplicativo não vai travar subitamente (crash) ou vazar dados de memória.
* **Performance Extrema:** O Rust processa criptografia (criptografar e descriptografar *chunks* de PDFs) com velocidade próxima a do C, o que é mandatório para não deixar a CPU do usuário em 100% durante o *seeding* (envio) de arquivos.
* **Cargo:** É o gerenciador de pacotes e *build* do Rust. Ele garante que qualquer pessoa que clone o projeto conseguirá compilá-lo de forma reproduzível.

### 1.3 O Poder do Tokio: A Melhor Alternativa para P2P
Sistemas P2P precisam lidar com milhares de pequenas conexões de rede simultaneamente (solicitando pequenos *chunks* a múltiplos *peers* ao mesmo tempo). Se você abrir uma "Thread" no sistema operacional para cada conexão, o computador irá congelar.

A solução é o **I/O Assíncrono**, e é aqui que entra o **Tokio** (o *runtime* assíncrono do Rust).
* **Por que o Tokio é superior?** Se compararmos com o Node.js (que também é assíncrono, mas roda em *Single-Thread* — uma única linha de execução principal), o Tokio é **Multi-Threaded**. Ele gerencia uma piscina de tarefas (*tasks*) assíncronas e as distribui automaticamente pelas várias *threads* do processador do computador.
* **Na Prática:** Quando o AlLibrary está baixando 50 *chunks* de 10 usuários diferentes via Tor, o Tokio consegue deixar essas requisições "dormindo" enquanto espera a resposta da rede, usando a CPU para criptografar outro arquivo simultaneamente. Nenhuma tarefa bloqueia a outra (*non-blocking I/O*). Para gestão P2P, o Tokio é considerado hoje o padrão ouro na engenharia de software por suportar carga extrema com pouquíssimo uso de recursos.

---

## 2. Transporte e Privacidade: Tor e a importância do `tokio-socks`

O AlLibrary não usa a Internet aberta TCP/IP comum para transferir dados, pois isso exporia os IPs dos usuários, permitindo censura e quebra de privacidade. Utilizamos os **Onion Services** (Serviços Cebola) da rede Tor.

### 2.1 O Roteamento Onion
Quando o usuário "A" pede um arquivo para o usuário "B", a conexão salta criptografada por 3 nós diferentes no mundo antes de chegar ao destino. O provedor de internet só sabe que o usuário está conectado ao Tor, mas não sabe o que ele está baixando, nem de quem.

### 2.2 O Papel Vital do `tokio-socks`
A rede Tor roda como um processo separado no sistema operacional e abre uma porta local (geralmente 9050) no protocolo **SOCKS5** (um tipo de proxy).
Se o nosso código em Rust tentasse abrir uma conexão HTTP normal, ele faria isso pela rede aberta, quebrando o anonimato. 

A biblioteca **`tokio-socks`** é a "ponte mágica" da nossa arquitetura.
* **O que ela faz?** Ela intercepta os pedidos de rede do Tokio (ex: *"conecte-se ao site abc.onion"*) e encapsula essa comunicação dentro do protocolo SOCKS5, mandando tudo para o túnel do Tor.
* **Por que é tão importante?** Porque ela foi desenhada especificamente para funcionar de forma **assíncrona** junto com o Tokio. Isso significa que podemos abrir milhares de conexões SOCKS5 pelo Tor sem bloquear o nosso aplicativo. Sem o `tokio-socks`, o AlLibrary não conseguiria se comunicar anonimamente de forma eficiente.

---

## 3. Gestão e Partição de Arquivos (Feito em Casa e `memmap2`)

Ao invés de embutir um cliente BitTorrent pronto ou uma biblioteca de IPFS gigantesca dentro do projeto, nós tomamos a decisão de **escrever a própria lógica de particionamento e distribuição**.

### 3.1 A Lógica de Chunks (Matemática Própria)
Para contornar a lentidão natural da rede Tor, arquivos pesados (como grandes PDFs) precisam ser divididos. Nós mesmos implementamos a matemática dessa partição:
* **Tamanho Fixo:** Baseados na literatura, optamos por um tamanho fixo de *chunk* (ex: 256KB ou 1MB) e não um número fixo de partes. O sistema divide matematicamente o tamanho do arquivo pelo tamanho do chunk para obter o `total_chunks`.
* **Benefício:** Ter controle total sobre o código nos permite acoplar a partição diretamente à nossa chave de criptografia. Cada *chunk* baixado é validado criptograficamente contra alterações e pode ser baixado de provedores (peers) diferentes simultaneamente.

### 3.2 O "Pulo do Gato": A biblioteca `memmap2`
Se fossemos particionar um PDF de 1 GB, carregar ele inteiro na RAM para enviar pelo Tor travou o aplicativo. Para resolver isso, trouxemos uma única biblioteca externa específica: a **`memmap2`**.
* **Como funciona:** O `memmap2` solicita ao Sistema Operacional que crie um "espelho" virtual do arquivo que está no HD (Disco Rígido) diretamente na memória. 
* **Na prática:** O aplicativo acha que o arquivo inteiro de 1 GB está na RAM. Mas quando um colega pede o *Chunk número 5*, o sistema faz um "corte" na memória e o SO busca apenas aqueles poucos Megabytes do disco na exata hora H de forma hiper otimizada. Isso nos permitiu servir centenas de arquivos mantendo o uso da memória RAM perto de zero.

---

## 4. O Coração do P2P: Descobrimento, Kademlia e Gossip

A parte mais complexa de uma rede sem servidor central é: *"Como eu acho quem tem o PDF que eu quero?"* A literatura acadêmica propôs soluções brilhantes para isso, chamadas de DHT (Tabelas Hash Distribuídas).

### 4.1 Trabalhos Correlatos: Chord e Pastry
A banca examinadora precisa saber que vocês estudaram as fundações.
* **Chord (2001):** Organizou a rede num anel lógico. A grande invenção foi a *Finger Table* (uma tabela de atalhos matemáticos). Em vez de perguntar um por um, a busca "salta" de forma geométrica pelo anel. A sua complexidade teórica provou matematicamente que o roteamento descentralizado pode achar qualquer arquivo em tempo *O(log n)*. É bonito e matemático.
* **Pastry (2001):** Inovou ao usar roteamento por prefixos (como números de CEP/Código Postal) e adicionou algo vital: **Consciência de Localidade**. O Pastry percebe se um salto lógico vai custar muita latência física de internet, e prioriza vizinhos mais rápidos. É o protocolo da resiliência a altas taxas de queda (*churn*).

### 4.2 A Hegemonia do Kademlia (E por que o IPFS o usa)
Com o passar dos anos, tanto Chord quanto Pastry foram superados na indústria prática pelo **Kademlia**. Projetos gigantes como BitTorrent e IPFS usam variações do Kademlia.
* **Por que o IPFS escolheu Kademlia?** O Kademlia introduziu a Métrica XOR para calcular distâncias entre os IDs. A mágica do XOR é que a distância é *simétrica* (se a distância de A até B é 5, a de B até A também é 5; o que não era verdade no anel do Chord). Isso permitiu que a rede IPFS armazenasse informações de roteamento no próprio trajeto de resposta (um super caching passivo). No IPFS, a informação viraliza organicamente muito rápido.

### 4.3 A Escolha Arquitetural do AlLibrary: O Tracker com Gossip Simulado
Ao invés de tentar implementar um cliente Kademlia completo (o que tornaria o projeto pesado demais e difícil de garantir o anonimato estrito via Tor), nós optamos por uma solução híbrida para o descobrimento: **O Serviço de Sinalização (Tracker) com Fofoca (Gossip)**.

Como a auto-descoberta está funcionando no AlLibrary:
1. **O Tracker (Sinalizador):** Temos um servidor isolado que serve como "Ponto de Encontro". 
2. **O Announce (O Gossip):** Nós implementamos um *Loop assíncrono* em Rust via WebSocket. Constantemente, o nosso aplicativo sussurra (*Gossip*) para o Tracker: *"Eu sou o Nó X, e acabei de adicionar esses 3 PDFs novos à minha base SQLite"*.
3. **O Lobby:** O Tracker compila a fofoca de todos os nós ativos e devolve o *Lobby* (o mapa completo atualizado de quem tem o quê).
4. **O Transporte Descentralizado:** Baseado nesse Lobby, o aplicativo do usuário se conecta **diretamente (P2P)** aos outros usuários via túneis Onion. **O arquivo PDF NUNCA passa pelo Tracker.**

**O Porquê:** Essa escolha arquitetural garantiu que tivéssemos o melhor dos dois mundos. A eficiência e velocidade de busca de um modelo com indexação rápida (sem a latência severa de pular entre nós lentos do Tor no Kademlia puro), mantendo a transferência de dados e arquivos pesados 100% descentralizada, censura-resistente e P2P.

---

## 5. Diferenciação de Mercado

O projeto se consolida resolvendo falhas e focando em nichos que soluções prontas (IPFS e OnionShare) não atendem perfeitamente para este caso de uso acadêmico/histórico.

### 5.1 AlLibrary vs. OnionShare
* **OnionShare:** É uma ferramenta espetacular para vazar documentos anonimamente. O repórter levanta um nó Tor, o denunciante acessa, baixa o arquivo, o nó é fechado e a rede deixa de existir. **O OnionShare é efêmero.**
* **O Diferencial do AlLibrary:** Nós não somos efêmeros. O objetivo é criar uma biblioteca histórica **persistente**. O AlLibrary foi arquitetado para rodar silenciosamente, mantendo os documentos vivos em uma base de dados SQLite local, orquestrando um *swarming* de *chunks* entre centenas de nós continuamente conectados. Não é apenas uma transferência segura; é uma rede de acervo.

### 5.2 AlLibrary vs. IPFS Desktop
* **IPFS Desktop:** É o protocolo interplanetário padrão-ouro. Porém, o IPFS tem um foco primário: disponibilidade e replicação global. O IPFS por padrão não oferece anonimato de rede forte contra a vigilância do tráfego (os IPs dos *peers* costumam ser visíveis ou inferíveis em redes não fechadas). Além disso, o foco em replicação global do IPFS pode incentivar uma dependência de nós comerciais massivos de hospedagem na nuvem.
* **O Diferencial do AlLibrary:** Nosso ecossistema opera sob a premissa de um *Threat Model* diferente. O foco principal é a circulação segura em cenários onde até mesmo procurar por certos documentos históricos pode ser arriscado. A dependência fundamental da **Camada Tor** no núcleo da nossa aplicação, e a abstração focada unicamente na indexação de metadados em bancos **SQLite locais (Offline-First)** garante que a propriedade dos metadados literários fique sob controle total de cada máquina do usuário, formando uma bolha segura focada em proteção de identidade antes da proteção em hiperescala comercial.

---
**Conclusão Final:**
O AlLibrary prova, em sua estrutura de engenharia de software, que é possível utilizar ferramentas desenhadas na fronteira da tecnologia (Rust, Tokio, WebAssembly/Vite e Onion Routing) para criar uma biblioteca descentralizada, focada em resiliência criptográfica por blocos, e entregar tudo isso encapsulado em um app leve e fácil para o usuário final. Foi uma amálgama de componentes altamente especializados servindo a um propósito democrático singular.
