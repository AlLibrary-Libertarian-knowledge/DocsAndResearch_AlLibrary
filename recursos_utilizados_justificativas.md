# Justificativa dos Recursos Utilizados no AlLibrary

Este documento destrincha o slide de "Recursos Utilizados" (onde aparecem as logos das ferramentas). O objetivo aqui é te dar a resposta exata de **"Por que vocês usaram isso e não a ferramenta X?"** para caso a banca questione as suas escolhas tecnológicas.

---

## 1. Tauri v2 (Framework Desktop)
* **A Alternativa do Mercado:** Electron (usado no VS Code, Discord, Slack).
* **Por que o Tauri foi melhor:** O Electron funciona embutindo um navegador Google Chrome (Chromium) inteiro dentro do aplicativo, o que consome uma quantidade absurda de memória RAM (geralmente mais de 500 MB só para abrir). O **Tauri**, por outro lado, usa o motor web nativo que já vem instalado no sistema operacional do usuário (Webview2 no Windows, WebKit no Linux/Mac). O resultado é um aplicativo minúsculo (poucos Megabytes) e que quase não consome RAM. Além disso, o motor por trás do Tauri é escrito em Rust, garantindo muito mais segurança e bloqueando acessos indevidos do frontend ao sistema operacional.

## 2. Rust (Linguagem do Backend)
* **A Alternativa do Mercado:** Node.js (JavaScript), Python ou Go.
* **Por que o Rust foi melhor:** Aplicativos P2P precisam lidar com duas coisas muito pesadas: Conexões de Rede simultâneas e Criptografia constante. O Node.js e o Python são linguagens interpretadas e, em muitos casos, rodam em uma única thread (Single-thread), o que formaria um gargalo. O **Rust** é uma linguagem compilada (rápida como C++) e possui o runtime **Tokio** (que gerencia requisições assíncronas espalhando-as por todos os núcleos do processador perfeitamente). E o mais importante: o compilador do Rust garante 100% de segurança de memória, eliminando falhas fatais que poderiam corromper os PDFs durante a remontagem dos *chunks*.

## 3. SolidJS + TypeScript + Vite (Ecossistema Frontend)
* **A Alternativa do Mercado:** React.js e Webpack.
* **Por que foram melhores:**
  * **SolidJS vs React:** O React usa algo chamado *Virtual DOM*, que consome CPU para calcular o que mudou na tela antes de atualizar. O SolidJS não usa Virtual DOM; ele atualiza os elementos diretamente (reatividade fina), sendo considerado um dos frameworks mais rápidos do mundo.
  * **TypeScript:** Ao invés do JavaScript puro, usamos TypeScript para ter tipagem estática (definir exatamente o formato dos dados). Isso evita que o frontend envie dados errados para o backend em Rust, eliminando dezenas de *bugs* silenciosos na interface.
  * **Vite:** Substituiu os antigos empacotadores (como Webpack). Ele atualiza a tela instantaneamente enquanto programamos e gera um pacote final extremamente otimizado e minificado para produção.

## 4. Rede Tor (Camada de Transporte e Anonimato)
* **A Alternativa do Mercado:** VPNs comerciais, I2P ou apenas a internet TCP/IP pura.
* **Por que o Tor foi melhor:** Usar a internet pura exporia o endereço IP de quem está compartilhando livros, sujeitando os usuários a censura. O Tor, através dos **Onion Services** (Hidden Services), permite que dois computadores se conectem diretamente de forma criptografada em túneis de ponta-a-ponta, escondendo o endereço real de ambos. Outra vantagem absurda: o Tor consegue atravessar *Firewalls* restritos de roteadores automaticamente (NAT Traversal), algo que na internet normal exigiria configurações complexas do usuário.

## 5. SQLite (Banco de Dados Local)
* **A Alternativa do Mercado:** PostgreSQL, MySQL ou Firebase (Nuvem).
* **Por que o SQLite foi melhor:** A proposta do AlLibrary é ser **Descentralizado e Local-First**. Depender de um banco em nuvem mataria o projeto, pois se o servidor caísse, ninguém acessaria os livros. Depender de um PostgreSQL local exigiria que o usuário final instalasse um motor de banco de dados pesado na máquina dele. O **SQLite** não é um serviço, ele é apenas uma biblioteca; o banco de dados inteiro vive dentro de um único arquivo (tipo `.db`) escondido na pasta do aplicativo. Ele é ultraleve, super rápido para buscas de metadados e garante a independência total da máquina.

## 6. Docker (Containerização)
* **A Alternativa do Mercado:** Instalar os serviços (como o Tracker de Sinalização) manualmente direto na máquina ou VPS.
* **Por que o Docker foi melhor:** Garantia de reprodutibilidade. Durante os testes de validação (Testes de Estresse de 10 a 15 nós), precisávamos garantir que o ambiente rodaria exatamente igual no Windows ou no Linux. O Docker cria um "container" isolado com tudo o que o Tracker precisa para rodar. Com um simples comando, a rede de testes sobe limpa, sem conflitos com outros programas instalados no computador.

## 7. Git & GitHub & VS Code (Ferramentas de Desenvolvimento)
* **Por que os utilizamos:** O VS Code é atualmente a melhor IDE gratuita com suporte nativo superior ao *Rust Analyzer* (que acusa erros de Rust antes mesmo de compilarmos). O Git e GitHub são o padrão ouro da indústria para versionamento de código, garantindo que o trabalho feito por você, pelo Tales e pelo Arthur estivesse sempre sincronizado, além de servir como repositório aberto para a avaliação da banca, dando transparência acadêmica ao TCC.

## 8. OnionShare (Referência/Trabalho Correlato)
*(Ele aparece na sua imagem de recursos, mas funciona mais como inspiração)*
* Nós o utilizamos não como uma dependência, mas como **a maior referência técnica** do projeto. O OnionShare provou para o mundo que é possível usar a rede Tor para transferência direta de arquivos entre duas pessoas sem instalar servidores complexos. Nós pegamos essa premissa validada por eles e evoluímos: enquanto eles focam em transferências efêmeras (apagar a rede logo após o download), nós utilizamos a rede para montar uma base bibliográfica pesquisável persistente com divisão matemática em *chunks*.
