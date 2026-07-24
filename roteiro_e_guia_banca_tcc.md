# Roteiro de Apresentação e Guia de Estudos - TCC AlLibrary
**Duração total planejada:** 10 minutos
**Integrantes:** Tales, Eduardo e Arthur

---

## PARTE 1: Roteiro Cronometrado e Dividido

A apresentação foi estruturada para ser fluida e direta, respeitando a limitação de 10 minutos (aprox. 3m e 20s para cada um). 

### 1. Introdução, Trabalhos Correlatos e "O que será feito" (Tales - 3m 20s)

**[00:00 - 01:00] Introdução (Tópicos e Objetivos)**
* **Tales:** "Olá a todos, bom dia/boa noite. Nosso grupo é composto por mim, Tales, pelo Eduardo e pelo Arthur. Apresentaremos o nosso projeto: **AlLibrary: Plataforma Descentralizada para Preservação e Democratização do Acesso ao Conhecimento**. 
* Hoje, a nossa informação digital está amplamente concentrada em servidores centrais ou sob controle corporativo, o que facilita o bloqueio, a censura e a 'bolha de filtros'. Se um grande servidor é penalizado ou cai, o acesso àquele conhecimento é perdido.
* O nosso **objetivo principal** é combater essa vulnerabilidade. Estamos desenvolvendo uma plataforma totalmente descentralizada focada no compartilhamento de documentos PDF e EPUB, garantindo que a informação histórica e cultural circule de forma livre, segura e protegida contra manipulação em fontes únicas."

**[01:00 - 02:00] Trabalhos Correlatos**
* **Tales:** "Para embasar a arquitetura, estudamos protocolos teóricos como o **Chord** e o **Pastry**, que resolvem o problema de roteamento e busca rápida em redes sem controle central através de DHTs (Tabelas Hash Distribuídas).
* No cenário prático, nos inspiramos em softwares como o **IPFS Desktop**, que endereça os arquivos por conteúdo em blocos, e o **OnionShare**, que permite o compartilhamento direto via rede Tor. A proposta do AlLibrary é unir as melhores características desses projetos: o armazenamento eficiente em fragmentos (chunks) com a proteção e o anonimato de rede do Tor."

**[02:00 - 03:20] O que será feito**
* **Tales:** "Então, **o que será feito** concretamente? Entregaremos um aplicativo Desktop que atua como uma estação completa P2P. 
* Ele não buscará os livros em um servidor central. Ao invés disso, a comunicação ocorrerá sobre a rede Tor — garantindo o anonimato de quem busca e de quem disponibiliza. A propagação dos catálogos usará protocolos do tipo Gossip (fofoca), onde os nós avisam uns aos outros sobre novos conteúdos. 
* E quando o usuário quiser baixar o documento, ele fará o download em **chunks** (pedacinhos do arquivo) de forma paralela de múltiplos outros usuários, com validação de integridade no final. Tudo isso suportado por um banco de dados local **SQLite**."

---

### 2. Delimitações, Benefícios e Metas (Eduardo - 3m 20s)

**[03:20 - 04:20] O que NÃO será feito**
* **Eduardo:** "Obrigado, Tales. Para manter nosso escopo viável e rigoroso, é vital delimitar **o que não será feito**. Nós não estamos desenvolvendo um serviço em nuvem concorrente do Google Drive. 
* Não incluiremos funcionalidades de mercado, como *tokens* financeiros de criptomoedas, modelos comerciais globais, ou moderação automatizada de direitos autorais (DRM). E, embora usemos a rede Tor como camada, não estamos recriando um navegador completo à prova de agências globais. Nosso foco restringe-se à viabilidade arquitetural da plataforma de compartilhamento de documentos e sua eficiência em rede."

**[04:20 - 05:20] Benefícios**
* **Eduardo:** "Com essa arquitetura, trazemos **Benefícios Sociais e Técnicos** claros:
* **Socialmente**, devolvemos a **Privacidade**: com a abordagem *local-first*, os metadados de leitura nunca sobem para a nuvem; ficam no dispositivo. Além disso, criamos facilidade e resiliência de acesso: comunidades sob controle informacional seletivo ou sem rede estável podem propagar os livros entre si, sem um 'porteiro' único.
* **Tecnicamente**, reduzimos falhas catastróficas. Usamos uma camada de backend em Rust que elimina riscos comuns de memória. A rede confia na validação criptográfica do conteúdo, bloqueando adulterações."

**[05:20 - 06:40] Metas para o TCC 2**
* **Eduardo:** "Por isso, para a etapa de prototipagem e experimentação, nossas **Metas para o TCC 2** exigem provas técnicas. Faremos baterias de validação de roteamento operando um ambiente controlado de 10 a 15 nós.
* Extrairemos **Métricas de Desempenho** precisas: vamos medir a latência da busca, a taxa de sucesso no download dos *chunks*, e sobretudo, a resiliência ao *churn* — ou seja, como a rede reage quando vários usuários se conectam e desconectam subitamente durante uma transferência de arquivos."

---

### 3. Recursos e Demonstração (Arthur - 3m 20s)

**[06:40 - 07:40] Recursos Utilizados**
* **Arthur:** "Obrigado, Eduardo. E como vamos operacionalizar isso? Sobre os **Recursos Utilizados**, formamos uma *stack* de alto desempenho:
* O sistema Desktop utiliza o framework **Tauri v2**. Isso nos permite ter uma interface belíssima construída com tecnologias web (**SolidJS** e TypeScript via **Vite**), mas com um backend robusto programado em **Rust**. O Rust com o runtime assíncrono **Tokio** nos dá altíssima segurança e gerencia conexões de rede pesadas sem gargalos.
* Utilizamos o **SQLite** como banco de dados embutido no desktop, sem precisar de servidor extra. A camada P2P se conecta através do roteamento **Tor**, integrando o cliente **tokio-socks**. Para orquestração de testes e o servidor tracker de sinalização, usamos conteinerização com **Docker**."

**[07:40 - 09:30] Demonstração do Protótipo (Apresentando o GIF/Vídeo)**
* **Arthur:** "Para materializar, vamos olhar a nossa demonstração do protótipo que está rodando no telão. 
* *(Arthur aponta para o GIF/Vídeo na tela e narra dinamicamente)*:
* 'Notem que temos aqui dois usuários distintos do aplicativo AlLibrary. O usuário pesquisa por um material. A requisição vai para a DHT, e o roteamento sobre a rede Tor encontra o outro nó que tem o livro. 
* Observem o painel de download: o arquivo não desce de uma só vez, ele é quebrado em *chunks*. O sistema captura essas partes, as valida criptograficamente e recria o PDF no destino. Ao terminar a barra de carregamento, o usuário já consegue acessar os metadados gravados localmente em seu SQLite e visualizar o documento sem nenhuma dependência de infraestrutura externa!'"

**[09:30 - 10:00] Encerramento**
* **Arthur:** "Nossa conclusão até aqui é que a descentralização atrelada a tecnologias contemporâneas como Rust e Tauri é plenamente capaz de democratizar o acesso ao conhecimento com segurança. Agradecemos a atenção de todos e dos nossos orientadores Marcos e Lucas, e abrimos o espaço para considerações e perguntas da banca."

---
---

## PARTE 2: Guia de Estudos (Respostas Rápidas para a Banca)

Aqui estão as perguntas mais capciosas que os professores da banca (como profissionais de tecnologia/redes) poderão fazer com base no documento do projeto, juntamente com a postura de resposta recomendada.

### 1. Se vocês não usam um servidor central, como ocorre o 'Aperto de Mão' (Handshake) inicial entre o primeiro usuário e a rede?
**Resposta:** "Para resolver o problema do descobrimento em redes P2P (*bootstrap*), nós utilizamos um **Serviço de Sinalização (Tracker)**, isolado através de Docker em um ambiente controlado por nós. Ele serve *apenas* como um ponto de encontro. Assim que os nós se conhecem, eles estabelecem os túneis diretos e a troca de metadados via Gossip, e o Tracker deixa de participar da transferência."

### 2. Por que escolheram Tauri com Rust ao invés da solução de mercado padrão como Electron com Node.js?
**Resposta:** "A escolha foi puramente técnica pensando em Performance e Segurança. O Electron funciona embutindo uma instância completa do Chromium (Google Chrome), o que devora memória RAM do usuário. O Tauri usa os motores de renderização nativos do SO (Webview), deixando o pacote final minúsculo e muito leve. Além disso, a linguagem **Rust** garante imunidade contra corrupção de memória e o **Tokio** lida muito melhor com as rotinas assíncronas de I/O de rede (criptografia e chunks) do que a *thread* única do Node.js."

### 3. A rede Tor (Onion) é conhecida por ser muito lenta. Isso não vai prejudicar baixar um PDF longo?
**Resposta:** "Sim, a latência do roteamento cebola é inevitável porque o tráfego passa por diversos nós globais. É exatamente por isso que adotamos o particionamento em blocos (**chunks**). O download do arquivo ocorre simultaneamente de vários provedores diferentes ao invés de uma única linha contínua. Esse paralelismo (similar a um *swarming* de BitTorrent) compensa o gargalo do Tor."

### 4. Como vocês garantem que os arquivos disponíveis não são vírus ou falsificações com nomes trocados?
**Resposta:** "Como delimitamos no escopo, não fazemos curadoria editorial (se o título bate com o conteúdo), porém, fazemos uma validação de **Integridade Técnica**. Usamos endereçamento baseado em conteúdo: o arquivo é validado através do *hash* criptográfico final dos *chunks*. Se o arquivo for alterado no trânsito em um mínimo byte, a assinatura não bate e o arquivo é descartado."

### 5. No TCC 2, como vocês pretendem validar e apresentar os resultados com apenas 10 ou 15 nós ativos?
**Resposta:** "Em pesquisas de *overlay networks*, uma amostra entre 10 e 15 nós, se estiverem altamente sobrecarregados através de scripts e provocando saídas e entradas constantes (**churn** programado), já é suficiente para forçar reajustes na DHT (atualizações nas tabelas de roteamento) e queda de conexões. Nossa camada de *Analytics*/Painel vai compilar os tempos médios de latência e de sucesso antes de um colapso total."

### 6. Como vocês justificam classificar o projeto como "Local-First" se a premissa é uma rede P2P na internet?
**Resposta:** "Ele é P2P para o *descobrimento e o primeiro download*. Uma vez que a plataforma valida o arquivo e ele desce, gravamos no **SQLite** local da máquina. O conceito *Local-First* brilha aqui: se o usuário entrar em um túnel, o roteador quebrar ou for censurado, ele continua acessando a base completa do que já adquiriu através do próprio aplicativo, sem depender de nuvem para abrir o software."
