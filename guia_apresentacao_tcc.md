# Guia de Estudo para Apresentação do TCC: AlLibrary

Este documento serve como um roteiro detalhado e explicativo para você estudar e se preparar para a apresentação/defesa do seu TCC. Ele detalha cada ponto dos slides "O que será feito", expandindo os conceitos para que você tenha total domínio do assunto na hora de falar e explicar para a banca. 

Ao final, incluímos uma seção extra com os "Recursos Utilizados" explicados de forma didática.

---

## 1. O que será feito: Rede e Protocolo (A Base do Sistema)

**O que está no slide:**
* Rede P2P sobre Tor para partilha de PDF e EPUB
* Protocolo para localizar, anunciar e transferir documentos sem servidor central
* Propagação descentralizada de catálogos e metadados (ex.: gossip)
* Documentos em chunks, com transferência paralela e verificação de integridade

**Como explicar na apresentação:**
> "Para que a nossa biblioteca descentralizada funcione de forma segura, resistente à censura e proteja a privacidade, a base do projeto é uma **rede P2P (Peer-to-Peer) construída sobre a rede Tor**. Isso garante o anonimato dos usuários e dificulta o bloqueio do tráfego. 
>
> Nós não teremos um servidor central clássico que guarda os PDFs ou que diz quem tem o quê. Em vez disso, usaremos um **protocolo de propagação (como o Gossip Protocol)**. Funciona como uma 'fofoca': quando um usuário adiciona um livro novo, o nó dele avisa os vizinhos mais próximos na rede, que por sua vez avisam os vizinhos deles, até que toda a rede saiba que aquele livro existe.
> 
> Além disso, quando alguém quiser baixar um livro, o download não virá de uma única pessoa. O arquivo é dividido em pequenos pedaços chamados **chunks**. Isso permite que o usuário baixe diferentes partes do mesmo livro de vários usuários simultaneamente (transferência paralela), acelerando muito o processo. Por fim, cada *chunk* possui uma assinatura criptográfica (*hash*) para **verificação de integridade**, garantindo que nenhum arquivo foi corrompido ou adulterado durante a transferência."

---

## 2. O que será feito: Aplicação e Dados (A Interface do Usuário)

**O que está no slide:**
* App desktop (estação P2P): integrar à rede, gerir acervo local, publicar e obter ficheiros
* SQLite local para metadados (sem BD externa obrigatória)

**Como explicar na apresentação:**
> "Toda essa complexidade da rede Tor e da transferência fracionada precisa ser invisível e fácil para o usuário comum. Por isso, a entrega principal para o usuário final será um **Aplicativo Desktop**. Essa aplicação atuará como um nó completo (uma estação P2P). 
>
> Através de uma interface amigável, o usuário poderá fazer tudo em um só lugar: gerenciar seus livros guardados na máquina (acervo local), buscar novos títulos na rede, baixar livros e também publicar seus próprios PDFs e EPUBs para a comunidade. 
> 
> Para que o sistema seja verdadeiramente autônomo e descentralizado, **não dependeremos de nenhum banco de dados em nuvem**. Cada usuário terá um banco de dados **SQLite rodando localmente** na sua própria máquina. Ele guardará os metadados (título, autor, capa) dos livros. Isso significa que, se o usuário estiver sem internet, a biblioteca local dele continua funcionando e abrindo os livros perfeitamente, garantindo a posse real dos dados."

---

## 3. O que será feito: Infraestrutura de Apoio (O Suporte à Rede)

**O que está no slide:**
* Serviço de sinalização para o encontro inicial entre nós (ambiente controlado)
* Painel de análise agregado (saúde da rede, disponibilidade, redundância, tráfego — sem identificar utilizadores)

**Como explicar na apresentação:**
> "Apesar de ser uma rede P2P, existe um desafio técnico inicial: como o usuário 'A' encontra o usuário 'B' pela primeira vez ao abrir o aplicativo? Para resolver o problema de descobrimento, teremos um **Serviço de Sinalização (Signaling Server)** em um ambiente controlado por nós. Ele funciona apenas como um 'ponto de encontro'. Ele não guarda arquivos nem participa das transferências; ele apenas apresenta os nós uns aos outros. Depois de conectados, os nós conversam diretamente entre si e não precisam mais deste serviço para trocar arquivos.
>
> Além disso, para podermos validar e estudar o comportamento do projeto, criaremos um **Painel de Análise (Dashboard) de Telemetria**. É crucial ressaltar que, devido ao nosso foco em privacidade, **este painel não identifica usuários e não coleta dados pessoais**. Ele apenas agrega métricas de saúde da rede: quantos nós estão ativos, qual o volume de tráfego e qual a redundância dos arquivos (quantas cópias de um livro estão espalhadas), permitindo monitorar o ecossistema de forma macro."

---

## 4. O que será feito: Validação (Provando que Funciona)

**O que está no slide:**
* Testes de estresse com 10–15 nós simultâneos
* Métricas: latência de busca, taxa de sucesso de download e resiliência com churn

**Como explicar na apresentação:**
> "Na ciência da computação, não basta construir, é preciso provar a eficácia através de testes rigorosos. A nossa fase de validação consistirá em **Testes de Estresse criando um ambiente com 10 a 15 nós operando simultaneamente**.
> 
> Durante esses testes, vamos monitorar três métricas fundamentais:
> 1. **Latência de Busca:** Quanto tempo demora para uma pesquisa (ex: buscar pelo autor 'George Orwell') percorrer a rede descentralizada e retornar os resultados para o usuário?
> 2. **Taxa de Sucesso de Download:** Considerando que os arquivos vêm em pequenos pedaços (*chunks*) de múltiplos nós que podem ter conexões instáveis, qual a porcentagem de downloads que são concluídos 100% íntegros?
> 3. **Resiliência ao Churn:** Na literatura de redes, *Churn* é a taxa de entrada e saída de usuários (nós conectando e desconectando a todo momento). Nosso teste vai simular conexões caindo no meio de transferências para provar que a nossa rede é resiliente, ou seja, ela percebe a queda, encontra outras fontes automaticamente e o sistema não entra em colapso."

---

## 5. Recursos Utilizados (A Stack Tecnológica)

*(Use esta seção caso a banca pergunte sobre as tecnologias, ou para criar um slide extra demonstrando seu domínio técnico sobre as ferramentas escolhidas).*

**Como explicar na apresentação:**
> "Para tornar este projeto realidade, selecionamos tecnologias modernas focadas em desempenho, segurança e descentralização:
>
> * **Tauri (com Rust):** Utilizamos o *framework* Tauri para construir o aplicativo Desktop. A grande vantagem é que o 'motor' do aplicativo é escrito em **Rust**, uma linguagem extremamente rápida, segura e com rigoroso controle de memória — características essenciais para gerenciar conexões P2P pesadas e criptografia. Ao mesmo tempo, ele nos permite usar tecnologias Web no *front-end* para entregar uma interface bonita, mas consumindo muito menos memória RAM do que aplicativos feitos em Electron.
> * **Rede Tor (Onion Services):** Muito além de navegação anônima, utilizamos o Tor como a **camada de transporte** da nossa rede. Através dos *Hidden Services* (Serviços Onion), conseguimos criar túneis ponto-a-ponto altamente seguros, atravessando *firewalls* facilmente e garantindo que o IP real do usuário nunca seja exposto à rede, protegendo-o de censura ou retaliações.
> * **Banco de Dados SQLite:** Foi a escolha ideal para o armazenamento local. Sendo um banco de dados relacional que não exige instalação de um servidor à parte (ele reside em um único arquivo do sistema), ele garante que a biblioteca seja leve, autônoma e funcione no conceito *offline-first*.
> * **Conceitos de Gossip Protocol / P2P Chunking:** A arquitetura descentralizada bebe da fonte de projetos como BitTorrent e IPFS. Dividir arquivos pesados (como PDFs escaneados) em blocos e usar a rede para disseminar as informações de forma viral (*gossip*) garante que o sistema seja escalável. Quanto mais pessoas usam e compartilham, mais forte e rápida a rede fica, eliminando o ponto único de falha de um servidor central."
