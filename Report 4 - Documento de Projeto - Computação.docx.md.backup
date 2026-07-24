##### **REPORT 4**

**Documento de Projeto**

##### ***IDENTIFICAÇÃO***

| NO | NOME | e-mail | Telefone |
| :---: | :---: | :---: | :---: |
| **212170** | **Tales Augusto Sartório Furlan** | **tales.a.s.furlan@gmail.com** | **(15) 99800-0604** |
|  **252148** | **Eduardo Augusto Prestes Júnior** | **[dudu\_edn@hotmail.com](mailto:dudu_edn@hotmail.com)** | **(15) 98825-4996** |
| **210685** | **Arthur Alves Letissio** | **[arthurletissio52@gmail.com](mailto:arthurletissio52@gmail.com)** | **(11) 97753-2568** |

**TÍTULO:** AlLibrary: Plataforma Descentralizada para Preservação e Democratização do Acesso ao Conhecimento.

**LÍDER DO GRUPO:** Tales Augusto Sartório Furlan.

**ORIENTADOR:** MARCOS FABIO JARDINI.  
**CO-ORIENTADOR:** LUCAS NUNES MONTEIRO.

Data da Entrega:         18/05/2026

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_  
        Visto do Orientador

**LISTA DE SIGLAS**

CAS     *Content-Addressable Storage*  
CDN     *Content Delivery Network*  
DHT     *Distributed Hash Table*  
DNS     *Domain name system*  
DRM    *Digital Rights Management*  
I2P       *Invisible Internet Project*  
IEEE    *Institute of Electrical and Electronic Engineers*  
ILS       *Integrated Library System*  
IPFS    *Interplanetary File System*  
P2P     *Peer-to-peer*  
P50     *50th percentile*  
P95     *95h percentile*  
SaaS   *Software as a Service*  
SLA     *Service Level Agreement*  
SSO    *Single sign-on*  
SO       Sistema Operacional

**SUMÁRIO**

[**1 INTRODUÇÃO DO TRABALHO	3**](#introdução-do-trabalho)

[**2 TRABALHOS CORRELATOS	5**](#trabalhos-correlatos)

[2.1 ARQUITETURAS DE TRANSMISSÃO DA INFORMAÇÃO ATRAVÉS DA REDE	5](#2.1-arquiteturas-de-transmissão-da-informação-através-da-rede)

[2.1.1 Chord	5](#2.1.1-chord)

[2.1.2 Pastry	6](#2.1.2-pastry)

[2.2 SOFTWARES SEMELHANTES	7](#2.2-softwares-semelhantes)

[2.2.1 IPFS Desktop	7](#2.2.1-ipfs-desktop)

[2.2.2 OnionShare	7](#2.2.2-onionshare)

[**3 O QUE SERÁ FEITO	8**](#o-que-será-feito)

[**4 O QUE NÃO SERÁ FEITO	10**](#o-que-não-será-feito)

[**5 BENEFÍCIOS	12**](#benefícios)

[**6 METAS PARA O TCC 2	16**](#metas-para-o-tcc-2)

[6.1. VALIDAÇÃO DE ESCALABILIDADE E ROTEAMENTO	16](#6.1.-validação-de-escalabilidade-e-roteamento)

[6.2. MÉTRICAS DE DESEMPENHO SOB CARGA	16](#6.2.-métricas-de-desempenho-sob-carga)

[6.3. ECOSSISTEMA DE ANALYTICS E OBSERVABILIDADE	17](#6.3.-ecossistema-de-analytics-e-observabilidade)

[6.4. FECHAMENTO ACADÊMICO DO TCC II	17](#6.4.-fechamento-acadêmico-do-tcc-ii)

[**7 RECURSOS UTILIZADOS	18**](#recursos-utilizados)

[**REFERÊNCIAS	23**](#referências)

1. # **INTRODUÇÃO DO TRABALHO** {#introdução-do-trabalho}

Em termos gerais, este trabalho apresenta a ALLibrary, uma plataforma digital descentralizada organizada em arquitetura *peer-to-peer* (PATEL, 2025), focada na circulação de documentos em formato PDF e EPUB para integridade histórica e cultural. A premissa da plataforma é garantir o acesso democrático a documentos e informações através de uma rede distribuída, reduzindo riscos de perda, indisponibilidade ou manipulação que pode acontecer quando se concentram em fontes únicas e/ou centralizadas.  
	A proposta deste trabalho é a elaboração de um aplicativo desktop para visualizar e compartilhar os arquivos e os status da rede descentralizada. Como reforço da integridade dos pares da rede *peer-to-peer*, a plataforma apresentada será implementada sobre uma rede de sobreposição segura chamada TOR, que garante o anonimato de cada ponto dos pares.  
	Ao longo da história a informação foi sendo fixada em livros para facilitar a propagação e revisão do conhecimento. No entanto é fato conhecido e descrito que o Estado e elites dominantes em comunidades, em muitos casos manipulam e controlam o acesso à informação por meio da censura, sobretudo por regimes autoritários do século XX, através da monopolização dos canais oficiais de circulação do saber (Gardner, 2024; Elmimouni, 2025\).  
Com a digitalização, essa lógica não desapareceu, reorganizou-se em diferentes camadas de controle informacional, nos quais o bloqueio explícito convive com formas indiretas de regulação da visibilidade e da atenção, no contexto da sociedade em rede e da personalização algorítmica que estrutura a visibilidade da informação (Castells, 1999; Kuznetsova, 2023).  
O cenário é intensificado na era da globalização digital, em que vieses algorítmicos em sistemas de busca, câmaras de eco em redes sociais e controles corporativos dos fluxos de informação ampliam os riscos de distorção e apagamento cultural, fenômeno associado à chamada “bolha de filtros” (Pariser, 2011).  
Esse rearranjo amplia os pontos em que decisões técnicas, jurídicas e econômicas condicionam o que pode ser encontrado, compartilhado ou reputado relevante (ENCYCLOPAEDIA BRITANNICA, 2024).  
O problema que orienta este trabalho reside na centralização de dados, que cria vulnerabilidades à manipulação, limita o acesso democrático ao conhecimento e reforça narrativas únicas em detrimento da pluralidade de fontes e interpretações. Nesse ambiente, narrativas hegemônicas tendem a silenciar perspectivas alternativas, como ilustram debates sobre revisão histórica e supressão de narrativas periféricas (Popescu, 2024).  
	O objetivo geral consiste em desenvolver a ALLibrary como plataforma descentralizada de informação para fortalecer a preservação de documentos histórico-culturais e reduzir dependências em fontes únicas. Como objetivos específicos, o estudo busca revisar o estado da arte sobre redes e trabalhos relacionados, especificar a arquitetura de redes proposta e implementar uma prova de conceito de compartilhamento de documentos com foco em disponibilidade e resistência à censura.  
	Para a comunidade e sociedade, essa proposta contribui ampliando acessos democráticos ao conhecimento histórico; para a área de computação, contribui ao articular descentralização, privacidade e preservação digital em um problema aplicado e atual.  
Quanto à metodologia, adota-se uma abordagem de pesquisa aplicada em redes de computadores, combinando revisão bibliográfica, modelagem arquitetural e desenvolvimento iterativo do protótipo. O percurso parte da fundamentação teórica para definição de requisitos e segue para implementação e validação técnica dos componentes propostos.  
Por fim, a estrutura desta monografia organiza-se em 8 seções: o capítulo 1 apresenta a introdução e os elementos centrais da pesquisa; o capítulo 2,  estado da arte e trabalhos correlatos; capítulo 3, a importância da segurança do acesso aos dados e preservação; capítulo 4, redes, ponto a ponto e Tor; capítulo 5 implementação; capítulo 6, cenários e testes; capítulo 7, resultados, conclusão e perspectivas de trabalhos futuros;  Bibliografia.

2. # **TRABALHOS CORRELATOS** {#trabalhos-correlatos}

A fundamentação técnica e análise de sistemas equivalentes permitem situar a plataforma AlLibrary no ecossistema de tecnologias descentralizadas e redes de sobreposição (*overlay networks*). Diferente das arquiteturas cliente-servidor convencionais, que apresentam pontos centrais de falha e vulnerabilidade à adulteração, as soluções correlatas aqui exploradas fundamentam-se em paradigmas de comunicação ponto-a-ponto (P2P) e estruturas de busca descentralizada (DHT).  
As ferramentas e protocolos de código aberto que poderiam ser utilizadas para atingir este mesmo objetivo variam significativamente em termos de topologia de rede, modelos de confiança, estratégias de fragmentação de dados (*chunking*) e garantias de anonimato. As tecnologias análogas a seguir servem para propósitos semelhantes ao projeto, porém de maneiras distintas:

## 2.1 ARQUITETURAS DE TRANSMISSÃO DA INFORMAÇÃO ATRAVÉS DA REDE {#2.1-arquiteturas-de-transmissão-da-informação-através-da-rede}

### 2.1.1 Chord {#2.1.1-chord}

O Chord apresenta-se como um dos protocolos pioneiros de Tabela de Hash Distribuída (DHT), fundamentado em uma topologia de anel lógico para o roteamento de chaves. Diferente de algoritmos que utilizam distâncias geográficas ou lógicas complexas, o Chord utiliza a aritmética de módulo para atribuir identificadores a nós e chaves em um espaço circular. Cada nó mantém uma tabela de dedos (*finger table*) que armazena informações sobre outros participantes em progressão geométrica ao longo do anel, o que garante que a localização de qualquer recurso seja realizada com uma complexidade de busca de O(log n). Por ser um protocolo de pesquisa acadêmica consolidado, ele oferece alta escalabilidade e previsibilidade teórica sem custos de licenciamento, sendo essencial para o estudo de redes P2P estruturadas (Stoica et al., 2001). 

### 2.1.2 Pastry {#2.1.2-pastry}

O Pastry constitui-se como um protocolo de rede ponto-a-ponto de larga escala que foca na localização de objetos com consciência de localidade da rede. Operando sobre um espaço de identificadores de 128 *bits*, o algoritmo encaminha mensagens baseando-se na proximidade de prefixos numéricos, ao mesmo tempo em que tenta minimizar a latência física ao priorizar rotas com menor custo de rede entre os nós. A performance do Pastry destaca-se pela sua capacidade de auto configuração e resiliência a falhas, mantendo a integridade do roteamento mesmo sob condições de alta rotatividade de participantes (*churn*). Como uma implementação lógica de código aberto, o Pastry não demanda custos operacionais centrais, sendo amplamente referenciado como uma alternativa robusta para sistemas distribuídos que exigem alta disponibilidade e otimização de tráfego (Rowstron; Druschel, 2001).

## 2.2 SOFTWARES SEMELHANTES {#2.2-softwares-semelhantes}

### 2.2.1 IPFS Desktop {#2.2.1-ipfs-desktop}

O IPFS Desktop ([https://ipfs.tech/](https://ipfs.tech/)) é uma aplicação que coloca o usuário na rede *InterPlanetary File System* (IPFS), usando o nó de referência Kubo. Por meio dele, arquivos são fragmentados em blocos, identificados por hashes e organizados em estruturas do tipo Merkle DAG, de modo que o endereçamento é feito pelo conteúdo e não por localização em um único servidor. Assim, o compartilhamento e a obtenção de dados ocorrem de forma entre pares, com roteamento auxiliado por DHT e troca de blocos entre nós, o que aproxima essa plataforma do desenho de sistemas distribuídos descentralizados e resilientes a falhas. Em termos de custo, o software é livre e o uso do protocolo não impõe cobrança; os custos práticos são infraestrutura local (armazenamento, banda) e, se se optar por serviços de *pinning* em nuvem, as tarifas desses provedores.

### 2.2.2 OnionShare {#2.2.2-onionshare}

O OnionShare ([https://onionshare.org/](https://onionshare.org/)) é uma ferramenta de código aberto que permite compartilhar arquivos, sites ou salas de chat fazendo com que o próprio computador do remetente atue como um serviço onion na rede Tor, sem depender de um provedor central para hospedar o conteúdo. O tráfego passa por circuitos em cebola, dificultando a associação entre quem oferta e quem acessa o material, o que o torna próximo de cenários em que se busca privacidade e circunvenção de bloqueios. Em comparação com plataformas de armazenamento P2P de longo prazo, o OnionShare tende a priorizar sessões de compartilhamento (muitas vezes temporárias) em vez de uma replicação global de objetos; isso o diferencia do modelo IPFS, mas mantém o paralelo com projetos que combinam distribuição de conteúdo com camadas anônimas. O programa é gratuito; o usuário arca sobretudo com o custo de conexão e com o desempenho típico da rede Tor.

3. # **O QUE SERÁ FEITO** {#o-que-será-feito}

O desenvolvimento do AlLibrary concentra-se na construção de uma solução descentralizada para o compartilhamento de documentos em formatos PDF e EPUB, voltada a usuários que necessitam consultar, preservar e distribuir materiais de interesse histórico e acadêmico, como historiadores, pesquisadores, estudantes e demais leitores, sem depender de um único ponto central de hospedagem como condição para o acesso à informação. O escopo prioriza a resiliência da rede, a privacidade do usuário, a confiabilidade na entrega e no recebimento dos arquivos e o anonimato dos participantes.  
A entrega principal consiste em uma rede de compartilhamento de arquivos em arquitetura ponto a ponto (P2P) construída sobre a rede The Onion Router (Tor), concebida como rede de sobreposição (*overlay network*). Nesse arranjo, a camada P2P do AlLibrary opera acima da infraestrutura Tor, e não de forma isolada da Internet convencional: essa rede fornece o plano de comunicação em que o tráfego de sinalização e de transferência pode circular com maior dificuldade de associação entre origem, destino e conteúdo; esse uso como conceito arquitetural, e não apenas como ferramenta auxiliar, constitui um dos diferenciais do projeto em relação a soluções P2P que não incorporam anonimato de rede de forma explícita.  
Sobre essa base, o protocolo previsto será capaz de localizar recursos, anunciar novos itens do acervo e transferir documentos entre participantes, sem exigir infraestrutura centralizada para a descoberta de conteúdo. O projeto prevê, ainda, a disseminação de catálogos e metadados entre os nós ativos, de modo que as informações sobre novos arquivos PDF e EPUB se propaguem de forma descentralizada, conforme a ideia de uma camada lógica de comunicação entre pares sobre a infraestrutura física, ilustrada na Figura 1\.

#### Figura 1 \- Representação da camada lógica do Gossip Protocol sobre a rede física

![][image1]  
Fonte: Adaptado de Abaskohi (2024).

Será implementado o particionamento dos documentos em fragmentos (*chunks*), com o objetivo de otimizar o tráfego na rede, viabilizar transferências paralelas e assegurar a reconstrução integral dos arquivos no destino, incluindo verificação de integridade do conteúdo recebido. Para permitir o uso da solução pelo usuário final, o projeto entregará uma aplicação desktop que funcione como estação de trabalho P2P, integrando-se à rede, gerenciando o acervo local e possibilitando a publicação e a obtenção de documentos. A persistência local de metadados e referências do acervo será mantida no próprio dispositivo, sem necessidade de servidor de banco de dados dedicado à infraestrutura externa.  
O escopo contempla o uso de rede de sobreposição voltada ao anonimato na circulação de sinalização e transferências, quando aplicável ao desenho do trabalho. Para apoiar a operação experimental da rede, será desenvolvido um serviço de sinalização para facilitar o encontro inicial entre nós em ambiente controlado e um painel de análise para acompanhamento agregado da saúde da rede, da disponibilidade de conteúdo, da redundância de arquivos e do volume de tráfego, sem exposição da identidade dos participantes.  
	Por fim, o trabalho prevê a validação da arquitetura por meio de testes de estresse em rede controlada, com amostra de 10 a 15 nós ativos simultaneamente. Serão coletados dados sobre latência de busca, taxa de sucesso no download de fragmentos e resiliência do sistema perante a rotatividade de usuários, com o objetivo de demonstrar a viabilidade do protocolo e do particionamento dos arquivos para o uso acadêmico proposto.

4. # **O QUE NÃO SERÁ FEITO** {#o-que-não-será-feito}

Este capítulo delimita, de forma explícita, o não escopo no desenvolvimento do AlLibrary dentro do domínio de compartilhamento descentralizado de arquivos e fragmentação em *chunks*, evitando confusão com produtos maduros já existentes no mercado ou com linhas de pesquisa que exigiriam infraestrutura operacional, governança institucional ou cronogramas típicos de maturidades superiores de projeto.  
Por operar em maturidade inicial própria a Trabalho de Conclusão de Curso e iniciativas de pesquisa aplicada, o trabalho não pretende disponibilizar um serviço em nuvem centralizado completo, concorrendo diretamente com soluções de armazenamento SaaS de grande escala, nem assumir garantias típicas de SLA, suporte continuado, custódia jurídica de conteúdos ou conformidade ampla para grandes instituições (por exemplo, requisitos formais equivalentes aos de sistemas integrados de bibliotecas ILS ou portais institucionais fechados, considerando a natureza de código aberto do projeto). Também não será desenvolvida uma infraestrutura universal equivalente ao ecossistema completo IPFS/libp2p com *pinning* comercial integrado, *marketplaces* econômicos, contratos incentivados (*tokens*) ou modelo de reputação distribuído; o foco mantém‑se na experimentação controlada de um protocolo de compartilhamento e na otimização de transferência via particionamento em *chunks*, sem pretensão de substituir nós de rede globais consolidados.

No que tange privacidade, não cabe ao escopo entregar um anônimo de rede de propósito geral no nível de um navegador Tor completo nem demonstrações formais de segurança à prova de adversários globais; integrações com camadas como Tor/ SOCKS ficam restritas aos cenários definidos pela arquitetura e aos experimentos planejados, sem prometer equivalência aos catálogos de ameaça de sistemas já maduros (Signal, Tor Project, navegadores *hardening*, etc.). Adicionalmente, não será implementado conjunto integral de ferramentas de moderação institucional, DRM proprietário, sistema global de denúncias/processos jurídicos ou filtros de licenciamento editorial automatizados; a responsabilidade legal sobre materiais circulantes permanece fora da engenharia proposta deste trabalho.

Quanto aos ativos bibliográficos, não será coberto como requisito mínimo de produto  o suporte exaustivo a todos os formatos e fluxos editoriais (AZW, *digital rights ecosystems*, *pipelines* de distribuição de editoras etc.), nem um motor de  recomendação treinado com *big data*, assim como *mobile* nativo, painel *web* público *multitenant*, CDN própria, painel corporativo SSO (SAML/OpenID) e Kubernetes como plataforma de operação para milhões de usuários. Por fim, não integra ao escopo a etapa típica de maturidades 2 e 3 de *software* (por exemplo engenharia de confiabilidade contínua, auditorias de segurança formais repetidas e estrategização de adoção urbana/“*Smart Cities*”), permanecendo o esforço alinhado à protótipo/validação arquitetural com integração dirigida de ferramentas já existentes onde isso reduz retrabalho, em vez de recriar o mercado de soluções equivalentes já consolidadas (OnionShare para fluxos onion pontuais, ecossistema BitTorrent/clientes amplos para *swarming* universal, *gateways* IPFS públicos para cache global, entre outros paralelos apenas citados em trabalhos correlatos).

5. # **BENEFÍCIOS** {#benefícios}

A produção e a circulação de conhecimento contemporâneas ocorrem cada vez mais mediadas por  plataformas centralizadas, nas quais algoritmos de curadoria, políticas de moderação e critérios opacos de relevância reorganizam o que pode ser encontrado, destacado ou ocultado. Esse arranjo favorece situações em que um único polo de decisão técnico ou corporativo passa a influenciar de modo desproporcional o acesso a coleções, metadados e rotas de distribuição, tensionando a ideia de biblioteca como espaço plural de consulta. Em paralelo, fenômenos descritos na literatura sobre personalização algorítmica sugerem que ambientes informacionais podem tornar-se progressivamente homogêneos para cada usuário, reduzindo exposição intencional a perspectivas diversas e dificultando o contato com frentes de conhecimento menos visíveis nos circuitos dominantes (Pariser, 2011).

Nesse quadro, o AlLibrary posiciona-se como uma proposta *local-first* e descentralista, voltada a sustentar um acervo documental (por exemplo, PDF e EPUB) com circulação entre pares, reduzindo dependência de um servidor único como condição necessária para obter ou republicar materiais legítimos para comunidades acadêmicas e leitoras através dos protocolos de rede P2P. Em vez de substituir instituições ou curadores humanos, o projeto busca recolocar parte do controle operacional nas mãos dos próprios usuários e da comunidade que semeia conteúdos, alinhando-se a uma imagem de rede como espaço potencialmente mais plural, desde que apoiada por protocolos e práticas que limitem concentração e monopólio informacional (Castells, 1999). Assim, a relevância do trabalho não está apenas na novidade técnica isolada, mas na articulação entre desafios sócio informacionais e uma solução que combine aplicação desktop, armazenamento local e compartilhamento P2P como caminho para informação mais acessível sob premissas explícitas de privacidade e resiliência distribuída.

Dentre os benefícios sociais e técnicos, podemos elencar os sociais em:

* Privacidade  
  * Metadados de acervo e hábitos de uso tendem a permanecer prioritariamente no dispositivo, em linha com uma arquitetura *local-first*, ao contrário de modelos em que o catálogo e *logs* ficam por padrão sob gestão remota de um único provedor.

  * O desenho reduz a exposição a telemetria centralizada de leitura típica de ecossistemas fechados, ao diminuir a necessidade de uma conta/SaaS como intermediário obrigatório para consultar ou republicar coleções entre pares autorizados.

  * Em cenários previstos no escopo, o tráfego pode contemplar roteamento mais anônimo (por exemplo, integração com Tor/*proxy* SOCKS), aproximando-se de práticas recomendadas para usuários que precisam reduzir correlação entre identidade e conteúdo (Tor Project, 2024), sem pretender equivalência a um navegador completo de anonimato de propósito geral.

  * Em comunidades com restrições de rede ou informação seletiva, a combinação P2P com camadas opcionais de anonimato pode viabilizar continuidade de acesso quando um único ponto de distribuição torna-se indisponível,  aqui o benefício é social e organizacional (manter circulação), não apenas técnico.

* Facilidade de acesso à informação  
  * Estudantes, pesquisadores em campo, grupos com baixa conectividade estável ou pouca margem para assinaturas comerciais podem se beneficiar de um modelo em que o conhecimento circula pela própria comunidade, com replicação cooperativa e sem impor um único portal institucional como *gatekeeper* obrigatório. O foco em formatos largamente adotados (PDF/EPUB) favorece reuso em leitores convencionais e fluxos acadêmicos já estabelecidos, reduzindo atrito para adoção.

Os benefícios técnicos podem ser elencados em:

* Segurança e Redução da Superfície de Ataque  
  * A arquitetura baseada em Tauri v2 isola o núcleo nativo em Rust da interface web, operando sob o princípio de privilégio mínimo para proteger o sistema operacional do usuário.

  * A persistência de dados via SQLite embutido elimina a necessidade de serviços de banco de dados externos, reduzindo vetores de ataque por rede local.

  * A camada de rede utiliza RustLs e o roteamento via Rede Tor, mitigando a exposição de endereços IP e protegendo a comunicação contra interceptações.

  * O sistema impõe a validação estrita dos formatos PDF e EPUB, limitando a execução de arquivos maliciosos e reduzindo a superfície de ataque em comparação a plataformas de compartilhamento genéricas.

* Integridade e Endereçamento por Conteúdo  
  * O projeto implementa o endereçamento por conteúdo, onde cada arquivo é fragmentado em *chunks* identificados por *hashes* criptográficas únicas.

  * A verificação de conteúdo permite que o nó P2P valide a integridade de cada fragmento recebido, garantindo que o arquivo final seja uma cópia idêntica ao original anunciado.

  * Esta abordagem estabelece uma distinção clara entre a integridade técnica do arquivo (garantia de que os *bytes* não foram alterados) e a verdade factual do documento, que permanece sob responsabilidade editorial do autor.

* Velocidade e Desempenho  
  * A filosofia *local-first* utiliza caches locais para contornar a latência típica de serviços em nuvem, permitindo acesso instantâneo ao acervo já baixado.

  * O protocolo P2P habilita o paralelismo de *download*, permitindo que o sistema consuma pedaços de um mesmo arquivo de múltiplos *peers* simultaneamente, otimizando o uso da banda disponível.

  * A utilização de uma *stack* enxuta, composta por Rust, SolidJS e Vite, minimiza o consumo de recursos de *hardware* (CPU e memória), garantindo alto desempenho mesmo em máquinas de uso geral.

* Descentralização de Dados e Resiliência  
  * O modelo descentralizado elimina o ponto único de falha, garantindo que o acervo permaneça acessível enquanto houver pares ativos na rede, independentemente da disponibilidade de um servidor central.

  * A comunidade atua como uma distribuidora orgânica, onde protocolos como Kademlia e Gossip organizam a localização e disseminação de documentos de forma autônoma.

A solução foca em um protocolo P2P customizado para documentos acadêmicos, garantindo que a rede de sobreposição seja otimizada para a resiliência e continuidade do fluxo de  informação.

6. # **METAS PARA O TCC 2** {#metas-para-o-tcc-2}

No segundo estágio do Trabalho de Conclusão de Curso, pretende-se fechar o ciclo experimental do AlLibrary: validar o comportamento do protocolo em rede sob carga, medir desempenho com critérios explícitos e comunicar resultados de forma auditável (monografia e defesa). As metas abaixo estão organizadas para que testes, validações e coleta de evidências sustentem as afirmações técnicas sobre roteamento/DHT, transferência por *chunks* e observabilidade da rede descentralizada.

## 6.1. VALIDAÇÃO DE ESCALABILIDADE E ROTEAMENTO {#6.1.-validação-de-escalabilidade-e-roteamento}

* Montar e operar uma rede estável em ambiente controlado com amostragem significativa de 10 a 15 nós ativos simultaneamente (participantes convidados/coordenados), registrando condições do experimento (SO, horário, perfil de *churn* programado, limites de banda quando aplicável).

* Demonstrar, com evidências coletadas, que o esquema inspirado em Kademlia/DHT mantém integridade operacional da tabela e capacidade de resolver rotas de busca sob entrada e saída contínua de pares (*churn*), relacionando o comportamento observado à complexidade esperada de busca O(log n) por meio de medições e gráficos (por exemplo, tempo médio de *lookup* vs. tamanho da rede).

* Registrar *logs* estruturados do experimento (eventos de *join/leave*, falhas de rota, *timeouts*) para permitir reprodutibilidade parcial na dissertação.

## 6.2. MÉTRICAS DE DESEMPENHO SOB CARGA  {#6.2.-métricas-de-desempenho-sob-carga}

* Executar baterias de testes de estresse com foco em taxa de sucesso de download e reconstrução integral de arquivos PDF/EPUB a partir de *chunks*, incluindo cenários com variação de:

  * tamanho do arquivo;

  * número de fontes/*peers* disponíveis;

  * taxa de *churn* durante a transferência.

* Grandezas que serão avaliadas:

  * Taxa de sucesso de download (% de execuções que reconstruíram o arquivo com *hash*/conferência esperada).

  * Tempo até conclusão (p50/p95, se possível) por classe de tamanho.

  * *Throughput* efetivo (MB/s) quando mensurável no ambiente.

  * Número de *retries*, falhas por *timeout* e taxa de corrupção detectada (se houver verificação por bloco).

  * Latência de busca na DHT (tempo médio para localizar provedores/recursos).

  * Tempo de propagação de metadados em mecanismos de natureza *epidemic/gossip* (quando aplicável ao desenho).

* Consolidar os achados em tabelas e figuras (ex.: distribuição de tempos; sucesso vs. carga; impacto do *churn*), com uma subseção de discussão ligando resultado a objetivo do protocolo.

## 6.3. ECOSSISTEMA DE ANALYTICS E OBSERVABILIDADE {#6.3.-ecossistema-de-analytics-e-observabilidade}

* Implementar uma camada de observação que permita visualizar a saúde da rede e o desempenho agregado, respeitando privacidade (dados anonimizados/agregados, sem identificar usuários; evitar telemetria sensível por padrão) para validação técnica do TCC.

* Desenvolver um *dashboard* web próprio: plataforma em Django e Next.js para análise de dados. 

## 6.4. FECHAMENTO ACADÊMICO DO TCC II {#6.4.-fechamento-acadêmico-do-tcc-ii}

* Correlacionar resultados experimentais aos objetivos e às hipóteses definidas no projeto.

* Finalizar a monografia e preparar a apresentação para banca.

7. # **RECURSOS UTILIZADOS** {#recursos-utilizados}

Esta seção descreve, de modo organizado, os ambientes, equipamentos, ferramentas de desenvolvimento e tecnologias empregados na construção do ALLibrary, aplicativo desktop descentralizado orientado a acervo em PDF/EPUB e comunicação P2P, indicando para que cada recurso foi utilizado no projeto.

O desenvolvimento ocorrerá em ambiente desktop, com sistema operacional Windows 11 e Linux Ubuntu  24, em máquinas de uso geral. Como editor adotou-se o Visual Studio Code, oferecendo integração com assistentes, depuração e extensões para Rust e TypeScript. O controle de versão foi feito com Git, hospedando o código e a documentação em repositório remoto de código aberto na plataforma GitHub, viabilizando rastreabilidade, colaboração e releases.

A solução desktop adota Tauri v2 como framework de aplicação multiplataforma: combina uma interface web (motor de webview) com um backend nativo em Rust, permitindo expor APIs seguras entre front e núcleo. No Tauri v2, a integração costuma ser mediada por comandos/capabilities, com ênfase em sandbox, permissões explícitas e redução da superfície de ataque em relação a runtimes que embutem um navegador completo como contêiner do app.

No front-end, a interface reativa foi implementada com SolidJS, priorizando reatividade fina e bundle enxuto, e TypeScript para tipagem estática, legibilidade e manutenção. O Vite atua como servidor de desenvolvimento (carregamento ESM, HMR) e como ferramenta de build do front em produção (empacotamento via Rollup), integrando-se ao fluxo típico Tauri \+ SPA para otimizações de tamanho.  
	O núcleo do aplicativo é escrito em Rust, escolhido por desempenho, segurança de memória e adequação a I/O de rede e concorrência. O gerenciamento de dependências e builds utiliza Cargo. Quando aplicável ao código, o runtime assíncrono Tokio organiza tarefas concorrentes (rede, timers, canais), enquanto crates de apoio cumprem papéis específicos na stack de rede e de dados.

Para persistência local embutida, utiliza-se SQLite como banco acompanhante ao aplicativo, armazenando metadados e estruturas do acervo no disco, por meio de transações frequentemente caracterizadas como ACID, sem necessidade de um servidor de banco dedicado em processo separado.f

No plano de rede e privacidade, o ecossistema Tor fornece roteamento em camadas e, em setups comuns, um proxy SOCKS local (ex.: porta 9150 no Tor Browser ou 9050 no Tor em sistema). A crate tokio-socks integra essa camada ao ecossistema async do Tokio, permitindo encaminhar TCP (e cenários compatíveis) via SOCKS5, usualmente para tráfego que deve sair pela rede Tor. O tipo UdpSock habilita datagramas UDP sem conexão, útil para mensagens P2P com baixo overhead quando o desenho tolera não-garantias de ordem/retransmissão nativa. O reqwest funciona como cliente HTTP/HTTPS, consumindo APIs e recursos remotos; o axum organiza um servidor HTTP minimalista e tipado (rotas/handlers/middleware sobre Tower/hyper) quando o projeto expõe API local, webhooks ou painel embutido. Por fim, serde estrutura serialização/desserialização (JSON, TOML, MessagePack etc.) entre disco, IPC e mensagens de rede.

No que diz respeito à infraestrutura de rede e conectividade, a arquitetura do projeto AlLibrary é fundamentada na orquestração de ambientes isolados via Docker, técnica empregada especificamente para a manutenção e implantação do servidor de rastreamento (tracker) desenvolvido em Rust. Esta abordagem garante a plena reprodutibilidade do ambiente de sinalização e facilita a escalabilidade dos serviços auxiliares.

Para a camada de privacidade e anonimato, o sistema adota nativamente o protocolo de Onion Services da rede Tor. A escolha por esta tecnologia permite o estabelecimento de conexões ponto-a-ponto (P2P) resilientes, superando barreiras comuns de rede como NAT e firewalls sem a necessidade de exposição de endereços IP públicos. A integração dessa rede de sobreposição é realizada diretamente no núcleo da aplicação por meio de bibliotecas (crates) assíncronas, assegurando que o fluxo de dados e a descoberta de pares ocorram em um ecossistema seguro e descentralizado.

O AlLibrary utiliza os padrões de compartilhamento validados por esse ecossistema para estruturar sua própria lógica de transferência, garantindo que a preservação e a democratização do acesso ao conhecimento ocorram sob os mais rigorosos critérios de proteção à identidade dos usuários.

###### Tabela 1 \- Tecnologia e sua função no projeto

| Tecnologia / recurso | Função no AlLibrary |
| :---- | :---- |
| **SO (Windows/Linux)** | Ambiente onde o projeto é desenvolvido, testado e executado localmente. |
| **Máquina (hardware)** | Recursos computacionais para build Rust, frontend e execução de nós/locais. |
| **Cursor / VS Code** | IDE/editor, depuração, integração Rust/TS e produtividade. |
| **Git \+ GitHub** | Controle de versão e hospedagem do código/documentação (URL real). |
| **Tauri v2** | Shell desktop multiplataforma (webview \+ Rust), IPC e modelo de permissões. |
| **Rust \+ Cargo** | Núcleo do app (lógica, rede, performance), gerência de crates e builds. |
| **Tokio (async)** | Runtime assíncrono para rede e concorrência. |
| **SolidJS** | UI reativa (componentes, estado, performance). |
| **TypeScript** | Tipagem estática e manutenção do front-end. |
| **Vite** | Dev server (ESM, HMR) e build de produção do front (Rollup). |
| **SQLite** | Metadados/acervo persistente local embutido. |
| **Tor** | Rede/onion routing; integração típica via SOCKS local durante operações anonimizadas. |
| **tokio-socks** | Cliente/async SOCKS (SOCKS5) integrado ao Tokio (Tor ou proxy compatível). |
| **UdpSocket** | UDP/datagramas para mensagens rápidas P2P. |
| **reqwest** | Cliente HTTP(S) para consumo de APIs/conteúdos. |
| **axum** | Servidor HTTP local (REST/painel. |
| **serde** | Serialização de dados (JSON/TOML/...) entre disco/rede/UI. |
| **Docker** | Containers para reprodutibilidade (Tor, CI, serviços auxiliares) . |
| **OnionShare** | Ferramenta externa correlata (testes/demos de compartilhamento via Tor). |

Fonte: elaborada pelo autor

# **REFERÊNCIAS** {#referências}

ABASKOHI, Amir. **Gossip-Protocol: A simple implementation of Gossip Protocol in Go.** GitHub, 2024\. Disponível em: [https://github.com/AmirAbaskohi/Gossip-Protocol](https://github.com/AmirAbaskohi/Gossip-Protocol). Acesso em: 13 mai. 2026\.

CASTELLS, M. **A sociedade em rede**. São Paulo: Paz e Terra, 1999\. v. 1\.

CLARIZEN **Online Project Management Software,** 2014\. Disponível em: [http://www.clarizen.com](http://www/). Acesso em: 20 mai. 2014\.

COBALTO, **Sistema Integrado de Gestão**, 2014\. Disponível em: [https://cobalto.ufpel.edu.br/](https://cobalto.ufpel.edu.br/). Acesso em: 20 mai. 2014\.

**IPFS Powers the Distributed Web**. Disponível em: \<[https://ipfs.tech/](https://ipfs.tech/)\> .

SILVA, E. C.; GIL, A. C. **Inovação e gestão de projetos: os “fins” justificam os “meios”**. Revista de Gestão e Projetos, São Paulo, v. 4, n. 1, p. 138-164, 2013\.

JIRA Agile | Atlassian, 2014\. Disponível em: [https://www.atlassian.com/software/jira/agile](https://www.atlassian.com/software/jira/agile) . Acesso em: 23 mai. 2014\.

Kademlia Documentation. **Kademlia 2.2.3 documentation**. Disponível em: https://kademlia.readthedocs.io/en/latest/. Acesso em: 15 maio. 2026\.

KERZNER, H. **Gestão de Projetos.** 2.ed. Porto Alegre: Bookman, 2007\. 821 p. 

PARISER, E. **The Filter Bubble: What the Internet is Hiding from You**. Nova York: Penguin Press, 2011\.

PALLERMO, J. *et al*. **ASP.NET MVC 4 in action.** 1.ed. USA: Oreilly & Assoc, 2012\. 406 p.

PMI. **Um Guia Do Conhecimento Em Gerenciamento de projetos (Guia PMBOK)**. 5.ed. São Paulo: Saraiva, 2014\. 496 p.

PROIETE, C. **Introdução ao ASP .NET MVC 3.0. PROGRAMAR**, 27\. ed, p. 6-11, fev. 2011\. Teamwork.com \- Online Project Management & Task Management Software. Disponível em: http://www.teamwork.com/. Acesso em: 20 mai. 2014\.

MAYMOUNKOV, Petar; MAZIÈRES, David. **Kademlia: A Peer-to-peer Information System Based on the XOR Metric**. New York University, 2002\. p. 3\. Disponível em: https://pdos.csail.mit.edu/\~petar/papers/maymounkov-kademlia-lncs.pdf. Acesso em: 13 mai. 2026\.

**OnionShare**. Disponível em: \<https://onionshare.org/\>. Acesso em: 15 mai. 2026\.

**TOR PROJECT. Tor Project**. \[S.l.\], 2024\. Disponível em: [https://www.torproject.org/](https://www.torproject.org/). Acesso em: 14 mai. 2026\.

**What is Tauri?** Disponível em: \<[https://v2.tauri.app/start/](https://v2.tauri.app/start/)\>. Acesso em: 15 mai. 2026\.

## 

[image1]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAdoAAADqCAIAAACKixPhAAA2bUlEQVR4Xu2dvYrtRtaGxWDM4WCaxgzGwTA0jTEnGIZDB8PBweBgBx+OBtOBmWiixsEEjhSYYfJzAQ46nrCDwfEOfAXNXMG+hn0J+lav92idtVdJ2rWlqlJJqido1CVt/dTPW6tW/VVNcvb7fc3c3t5WPeyY9+/fPz8/298X1gtliePxaEMLhX4ow0Ax7ImEkKbd3d2RptkTF1LZgAg8PT3Ri1KU0V96b3t6EIpr+snDwwP9nD74cDjYKwrLZ4kSfH9/X2yFeSFz7fr6+vHx0Z6YD3ofMilsqDex5Jh0k/IraSj9DVjYqACQKNNtSaDtucIyoeo2YA4pbAGy8Ej4ss02pFGX2p0gvBxTHIliUqzZ0yGA1lN60F97rlBITmm0JSZ/g4zecITZHlKO6fFkqFMLwp6ICaXKbrcbVxcV5oLSa0qbLjfqui6OizSQtUd2mA3NEsrkl3q0w8gxPZhqgxltBLxAto2XwnYomTAei2sQo/LwdxIEkGP4iGfUYkC2OX359M7NQmE06FyyoYUQYDiWDc0eDEOwoT34XtcJBqvZ0FlBdZTbWxUAJU1iX1ZhBaA7atHuIM+Ox5FyjBEOOUdQ8V0UCuuAtCxnqfHEp+0+Uo49xX5GUGFk/pKFFXNpN06hk8fHx3V01NOHnPVanDntcpErZF5Ii+ltRww3KYSl+I4K4zgcDpkPaLuUYUP2MmGle83eZXcpJMdhp6IUCoUEULFdX0VO+jnQ2XuBHJOuLbSmokS9u7uzoYVCElbg95yFdbiMXeij+jq0feX4OrO54SMYqJTWym630+M0dU8CfOv6VHAPnf9wy9WzuDbl7CzFIzqOvnlDXt9MQryCokWm/RZcFroF05fqLqTaYeWYorr0ZRXGgV4fG7ouOhcvPC/Ha4oaMpBX8y3CQNtnHGTKhb1hoeAP5ed1m8agc6CF/d9A4rWyNv46LH2NW8cGpBi5AVnWBN+5IJEK21DLlj2jQ87IMUWNZ2t3QSy9giHrlSQyqgpPYX3tj1Bkm2RZsan8Y2ydXjkmFV66bPVx5DmXNrRwDoq3s9OKmjKQoDCB9Y1sG8bUPb1yvO4pbVgBzobmDdWOWTXisnqZZVFc85141vcrQ9dA3ZJEkbL6oTmPj4/LsuNyqx0r3m3LhhY8WJwpkAbKTrll8gTotSy6s8VGmgz5l4oF6V3p8StMgZrtG5EdF/nwDj3aTrmiFkDmc1sWYSysuJuhkIyNd+fAf2XleIlO1SlstkIOy7LcPoUMWVBDMAYwgq3y5rCvR0ooE2Ro2WX4SoXgkOmzqbI2QOnbRJE/kWOKlEW0jsPy+PhYSkWhMCPZtsiTOeIwN+0kFtI8OEM2NfK8UMiNbJUn2axUehAp8kc5pv8z79eKR5oYH6YY6dukuN2bsvgfQ3XSRzkuPZs2KCZ1XVczkUPdUxCo3G3WDAIx2qZYP5Yi9vb2lu6PKUv0l4r5/f29NsZxmbwD/UuX4V+spVW1jhQKrBmUo+D1KD36w5PowfLUbZK4NqJERcInhrJXkeNCVsTwVMjcCpI1UmTSt70aMwZVlWP5lfnX/RXdikoQFo0Jrhgv0o8junu2A02C10KdXKddX59iW2QxZfcpZa8ix4V8gF1iQydTtVNGyRaGnpp2If37YaivE24ER+SYyo4WyRj264c7xqiggkBSlWZo8IsfPUL89iFynLIOaNYox1R4EJncgnxh10I5R0KoWCaO6otIY3NkCKVRDMfxQ7vDstyf/tW6X6kp/jX7HyQJkGf0vzhIJ8cx3DeLI2WdpK3jlKxGjrHcDFSYpLbu2VwK7c2aofSlAqlLVD6kzHtZUUVb3fieke5xiKycpWNdDeBiHNNP9L+p5ZheK1J7mT7Arfbd2N+fjoc3/2oOjHuHIKS0noocjwN7KJB4TTGp6Lcv3SZVVayQ2Ykhag3fFj1vIkEYQQyho2PREBEoSK35tzmVY1nncs8gPCAvT4pRM8taefTS1F7Aq0tNiNYBrpRaCDIhsYB/960rHW1SbDAVr+Mxmen06tWrm5sbGxqfhcoxUjzGm8O+jlG0Cj7ESNOGm/uw2/Zs0kr6wp47vfZFrHzMQdyqielZehG1GNJGVoyuXlCliO+G/qU6AN8s6QHj1PyrQyQ6Gq5CpthHfaTxUxNv376NlBGHWaIcww8YTzGfeXO2lG2jghDDAMKUCh0SJPNo/YnEixDHGHL7rPaNh/VthKBmGo67it3qItn636ZHjuXnYUnmW6yLs8KDlLEkzmh7IhXVqTdzIwQRSgPaUuhRoLo8VJpS6sT2br0sGNRpmU8H0SHqhjgSkaVwZD48/b4djwL0v31yHCPvJiuQyR5kWIocU/xQHojUpTEMSrINjc/ZYlizs07+1UJGpr2xdWKUjuDE0OJFE7cNaEJ0k1ByvCiscRTIv51yHKnAUCaO7a9AhBc5HgC9LjY0FWjYZSJnFA9uOTrLjh3iNjQ/4onPQom1vw5sYQFGPmWsHc83ob+SEvc8IBTWUNPOWZR/a+70wzH9RBogkRISnhMbGhQYQUWO+6ja8fnzQhE1TgonQpk/+LSI2Fl6NJFK8XKJ1S5DZ+WeqU8n3rhpYHo2zb8CbrXvGjwXkDR5t8hxJ1TRZmKWNvwy6Y30GP6ZqOVlCq4ULJRQMfwyhNOGTWZ/uqUIOknU+ZFAjm1oaCLVT4YixwaqgKnODpWtAzKLjRyPfPwwzYrkOJQN9+JJsGEhOPAqG+KmmA7lIRJKumen4RyQUC1leluT23TN58oxJjgAOiVOdqrM0DuMUR/4fHMxIVaVnJI7Cwj/4osv7Im5oZefq+POB4r/VQ6Dm12XZ5fjUH6hzuI2gijW8aIZyCLwfdvQHuD1rnjQHjRUp5krx40aZofmBfIKXYY0gv0or4cRgQivT7eYwkBdV0Eo8IcffnCfOzt37WSnbAlV3vLBjHSaBXp62JbHi2/UKb/agDNn3WR1f/6spvD1hbj3GUeUmU6LxkQ0VqS85vXeRhvmB96y+uuvv6Zko7/oq3RjfqfW1XviJY1QZnQLQy7YnfaeV2qiRM29nSaL4IlT5JheGwMQK160EJNQAR2jesDbXhRRdH3YMhkJmbhUCIjk5ynUbPqYpS+feXYPBVK5QGlCAcHF+GFnCZIL9tyd26j1xWAn4XrkfPktDiZS5Niy50WBoSwDUJKzk+ADGPKhQUUNfvnll7odIgKjtT4nx7LuNZYlk3Bh58ixHtONxyF7Nayk8HhcKscY9dX5AgPQr+j9KSvTs4ZbxFWXFZ8nVNTTNyV1HovK1dWVCbGvEocgD9Iq2ShxlAPTrqViKKtrDlxQORNzKmc1TnOfiaxBjkloAg4WhoDe3Nx89tlnX375JekXKlh7nR8HXh2qYvnWNuBZOYYKN+0gXK2tcjEuIBUW7QaQY3qidEti2ZDdhXIMTae/o61XGOl97ni4WWxoxjwxNjQmiP8EvHnzRv8bSl/OEsR7e1aOkfnlAnzj2QvcQlc5cmzuM5GZ5fjA25/Y0MsJ+BWdyksvCX30fxDlM7Semvbn+mzdI8dQ5J9//tk49ZDhKmUCixxXpwu5Nqe5DY4OiIi/HMOLHdCxCBPb3DC9sTmdIPLhT6hyfinJnuvmihGclWPjKK/bWYvDF1Sn5R3XmAeZ+0zk5O7TOXStfqlDjBe8clrBbJsO3aEzxEdiPHGfFYM+OTaxYbhX23yJHCPf6Ca/yDHManE9n5VjZLiBCyZSc5cjYjixrgWkcoymeIQtnj5QukjLLAH0rOneKsgxxFQLiP4KyngwieBT1hfgevcCNDrRRyL+6OuuVTrl6ROpgsT7nn3e9emmfih7GHcFExgGozhupP6R9LjjQZFyAe58x8MJKKZwW4TQZXRzuSygggwLYij85VgnM7IdjkWOm9arIJeJHCNcK/iwHItWxgOK/9NPPy3RNAaUPwM6x4YJUjwv4sizBJI9tzPPXwrKBcmC9ltCTOt2XBO8wyh3ksnRaIP+dF6AqBDxwWX0ry6/uCbIfIWXJ9mwUUj6HXmeMcml1o7mdEkKWG3NqXXceYGcFU+oWFXHrlU6pxPwVgPo5BSQn0ygZJeG383kJLmMYu+uHS6m76PHOVB09cmxOxIjKr/++qsNWhRuMkUiZaJokj1X26qjMVKzUF6iIlTG0tEBkTVxpI+l+hU5NhfjArcPbd/lcW+CamjwdJUaxQR6vrM0wUb3p2lMBAJd+Rc8caMxBsFzoycVm3tBLD4BrXuM8iS++OIL3L+zgFyEDERbNC8G1vS4ADHkmP6ajr49eyrkX6RrE65soCltQ6fRqXT+chwWV47hHdIhBR+C55NO0jzFpWKX43SH0o5HAVeKv/zlL1999RUdvH37VkyNiY7Xe56vO90HPS8vsWPMz9HofAO3g1FYHV/ifauUs8K9AH4PBB55rjB+oi+T3+JgIo8R1tPqJBM5pvIWqnm0NTp7rYOjS1BKgj/3gddjosL1xz/+0VX5YhA0sEEbLqL2zOVU7Eqv1QrZqBW19b3jvdZhOOtrtG8UBq9cUHN/YKX22XY97i+fEciVfs+zOWxoBHKQ451a6aIwAp0tIxFcFj3Rz6WKZ1w+QTc++vObruGewlyfmQ+IopdYCCJAiNCzyn5gdIj5yb5r30A305990DgouwQZB61xX77JQ45dI6VwEQkq77l0Sj/3lifEq5PnoUJ0xwPmZNYM/TuQ34LYUosGMfAS6UGSPMhNZieGp6IzK88rx0G6swsxehoMse/fx4jnPvFOOpUzCRMjw3SIyzH0WkKLAxEexjqmlIDn1zVsFwS9fLI8Ma8cwy9vzxUuJ3hbyjBCFoPQ+Vx4BXUZf+RVpcjsvZ+8PupZyV43H50VpEETo3IdxC5amhnl+Jtvvll6H3Q+xK7CO2UxAe5zYfyK8+HAy70G7AoWF/MGqdsFCT5EevHdYBSHDY3GXHL8n//8J+VnbgFxcJGaoNsZfdp1u6ofSRiSu+J+LdIvf+vnosQ6Mg1rpT13Ifq5NXenU63z3XffwUAmwyV4JXTkWV02dAPUavjDh0iniJB6b5tQhRSqnvdhLjmGWNjQwgRevXp1r6b1+9DnZnVx5Rha37QDSSU10SXQtB5t9HVj5BICoapyH8zDdA3SqqVpbZS//e1vFY9c8q9FRoNP2xTaS/PROk4pRhlSOWubRmUuOSYDp++5VJjneqtFM9oURR+XNFQ7ceV4pxZ5gMXdOFONb3k9VX0BqE4XLat4NQY527QuCMgxKfXr16/pgPLMv/71Lzb3X/Z3p3uerUVG437vujmcjl7/8PGJm+oZkthdU/MaUWjMJuOvf/3re97cZM+bwErzueZm9YAoFOJx5CV7+jqy3FKp5XjPBvIzTz6GgCKc7rnvkWOEN5wDochyFu4C/ARXysWaqPlkH2gxgKVg0vfjP1RQo0Z0zlA+3sK3S1uVPhZD9N++favbBFIUdZkvpOGetykwgW6IThp4PHAMA1nsYrkYFxwv2aMAeUCuNAycCkIVbqpw5rhD0U5idrMlsM82CcLoxmxwTAvgyPs3V6d78cEmqnn7O3XtS8EGKMb6VCEUpJgm2l3t06lwrdaYbVpBr5w9CvCXlFdnRdwBtTLCd+ynOivHsa3XB9530YauEVd2TiLdPb0F0Fq0oeGIenN/yAoeaAHIANIRhe2x3YkVbkd9Byh7X7O34PLMmxNKHLqyCC02gRr00UHWoa2NWrFWgBw3/AhRZPmJ+9yU1IP+9HUAJ6EJPIn0fdcE5dWzhbRv/GoFEtYRcjwA3XDH+3CjhBtR3mZ+OwtiDMeuLHbKsemFrto9B0SOsQSlHkchcozUEas8Bzmm8rhuAxkf6MqOjXS3zKybh6DbnmaL6Xk34a9fv57Rew7b2TrRGG6Xf1xxf1OgpeKmWqccm8CqHQAncizhEs8ix0fuxpef+8jxbfxZnXteGdmGroW+6LWhGLRoAlfMbhvjumoeomRDWyo2pjAY9o430LJX5AQcIDW7R0zyQZXqVbhHYECZwghXr1ZPgPTFkOTbdu6ce7F098kpxJLWaIRXgyJA90/QrMGanDZ04TwPriLdEenbGYCcptAO6GAyOk0q4fvvv//HP/6BY5Rn7b5cECLTrqAceM/yNCkeik7ruJMDr4F55PFtQRLO87mx2a1uDVgqXAOC0B3pA/q9JtLkuZSzS/oQO6iTir2KJjZWVgw0Jir2PGgX5NZaGk64eKQpGj6sSYse1MaVnXRH+hNvPGpD18VFSweEBQvguTme3mc4tUbjPkvz5s2bikdE4DI4E+eKnNyAQQ2727Qw4C1B+GibFD1pfX7SSi3fnpLhDNOkHb6JzGlDl8ZAKgu9kT5uzNNSMEPiUwJfUN2zd/quXXkgLMP91PTQm5sbuuaRabjCgDfZXlpQQIgxb9i0QHGKInPv9FK6ILbpDm6EV+z5Td/b3Jk5DcksthU4kalQ+ziBeyOdjKP0mSANnlETkMd2+g3lKlidfXLc+I1Iu5ThNjie+Mij3LTX4tlj4fDCpezUyD+TB3777bfvvvvuWq1aiQvSz5jty5wzkuEreYK62YZ2ceYLKw8De3EMm4oxeM/s1dgdyLE7jQoMOPvHMSzH8lZLt0EWDVV+T7yrN7LE73//+7dv34oGJRajxI/z5Jo3P7WhGUNGGBk0/u3dM5E+Y6M+EmR3+MdOWOrTLVlR1WE8k9Hf4HE+LMfyVlvoM8iNR57TiDFtJDfffvvt119/DUXGgmq4LLEMBc+BQUBhmav8jkBaw56cj3REgQ1dJpXHCrPx0LancVaYFwteGM7eULL4ddfcTYDux4uyV3oyfz0XCDGGe8PR/NVXX0l6ycEh8rYjhrMZpvG7Jgb+bf8ZwVR1G3oOrx8880q4NnRpzF6p3NzcyLErxzqGRyTkMNW58VI4iygadpXgzc92T8VmwIc23BTIHGP96ZyQMgP75MCU1YMBvRozvsAwo9/tfKQDoxeLg+RjdscoWT1m+pOcqk6H8vgUhovAqAkbqkDiej6XtHtYsmMznBUxJ8KGZowkzTOvH6RPmUySrBb0zAkzguGYifvkz0IJRK802iC4INLdvLIUMkk2TAzDsZbjvTOTKvjb1s6CmQaU8xk9Of5QJjTf8szrr+uQs62BHDjycu+1bFvZ5UnTslizi1mdjEj+cizc8o4qNjQ5SM1ho+csF0d6Z6bJFsSRDZ0Pehlt4Lg60kTQ4qY1JWxoFyOeTrZAMqutcaRW0ld/YOcsm6ygQqSLbp/O3p1uGYNvT4N9FYeJ0hOQ4+COKrHBsPEgVcLFWVaPS80cmPPjnDiR2J9r5tMFfSVzIp63HVF7JdY+8ywpBvoDjS8of/q8K2/fvtX/zqU4nYxukkcCXgKfiiQge64j+5LvUkZm2dxkzuW9s7FCDqAO72teRLUxKb1CZZpOHpiojwBaZzEaQZ38QIZyTO95aVX35s0bY3NlmKVzA/pIERXPeD/y3mbXPJGyM/uNZnyWRY6PqiDjoAi6Pd0xrAASFOY0ciy5bs97u8mpvp7SeaHc+HBu7RgXKu03NzdGjt1Z1IUBHni0WSjbEZlK1i+NwaQsG9ZQD4LUjfZEYZQjIkPgP8Wx9onrfJjYfzIAZnnYUA+ueSK1+W0xMi7lmQfpIiZHizIataFkfYAAWZYajNO7FKczi+doWfjXUpeacp0Me8lHQ1+h74zCVjkjBRedEySlcpbjSOkbD6qwybCFUCDP7NoF+QQ5hTZNrWbSJiCAHIMDbyMyi3f/mrGhGUPZwl8Zw+LZF1QFMi2v4ywyMFxC6OxcLTa0jifaUDu1PlzOchykzi5owpQ6QMmjc1IaMOpwruI3mrnKVeW3JlSoapWyBOUHoylBGKjPQr38pcDs8oneYSrlHDd3myvbFNIQUo6Fml0tkYZno8WBbs2+IQqFPtCIsaEOiGQbWugnVFY3toXR31BPKeTJ+ZI5EYxTnu5cJuWlZm/Ubs30PDI2NDKkyD6lusqsk3YjID+InWHkeC7D3zCjt23dRJfjRtmzcJxf1OCiH0a1tedlrvVLffyb76Mteb6OkuzphR+HyK4pLLPkFhcUZxtamMw8qUuZDF2cGM1juOP9yesJA1MKwxzn3uqlmqnXdzqULa8DzYjtg4pG1SW7dcI1Kwqz0JHqhS1AVd2Mnnf0+kYVtUgkqMZqHm5lQ9lkXmKMFfwpcpwFszQF7u/vI7kj+jhO2Cr70h+mj89QPPRsWFMVb/7aKXKcCxe51ENxx9hQRVhjsHKmmXlCMtRpMPZBr93Z3r+IPc/Avui5hj63wzjS9/p2Mi4FCz4EyyuFJXI8t/lYQDVpBuU4bEt8N2GS9IGXpcaIoIm9jnuesm9DR/HI2yra0DkImEwFQ5i8UggFptjb0Mj0tY4btu9Gq8CB0VY/5NgECkdegEKcEnveOE7Omjc0dzD37JNj3MR9unnJH3/80d834t5NAgPKcaj7FHKmpHF29CljVDC7t1N5h70ZnaBSub29hbNYpKTiYTMNu60RaASLfkWWqRnUCKmVy66vrxFFFS8sgAPIn6h5pxzrZcLpLAawiy+iai13OWhOFwCSp9BfWM0SUrcLyOGAPoFu+8TbciOc7uM5W7Wzf5U+KhNPRSEqNssWNgvJR6enWDTuIkiJRMhIBKF9onTaqXrHG17gWB7kemzlerkt/RAaJ28o+tgpx3u1Gqd+k6aVURF3ecRR7SZTtb4L+ounSEWFy0y10ajKxt/p4b52k81iPUde59eGFsLRkfaFTJjFXUiSFGSEv5bjmmmU0hnZwrFc37DSaVmUa/rWm8f8xkvl+J///GfljIB2nws1hGQ3rQGr74azNU9xcuW46ml2dOJax/lMgKq57WJDC+GwWbaQFf7FOCw8oGDSajhGjo11bGSLKoB96wEQDrz80Lt37255ZjyuNyIIo1iM+kvl+JdfftGGJ2LbyDFUHpfRX3xI067+IQmEb+yU48a5Zx9uhBc3xaawWbZQAPAm+4hIJ1qORfL65LjmqW6dZu+OR1xUTNN290GhjrxywrPa4Ly6UI5xN1FY8Qjrr4YjAj+E91lOyZs07Tf2ybHnwDvXpzHCcV9YLuezSCEHZiyW6Hajvxf1Me55k1bSNfG0wsKFnMEXoVu+RvfhUIZi4kB+C+2u1LIbFYP7I1xC9D3fvHnzu9/97v/+7//0m4jWy8V4N22T6npCvyc9CLXFrt33wPhYEHX0mWTkwgs03NwxMTww4iUx9P6ZvMm6KXJc8AJdVSRSrpJ2oq3js3TaxQG5ZoalMDdMlTAvy4q65VLkeHnc9u9FHQ/RVvhSz5ZPTzmmu2lvQyTy0TVPnniBLRtaWDszyLFpQgL4AW1o4RwjhqCNpmZ8pI2SmNrp1IQ/+3p02TgtxvDkPrP67HNzJiu7uJCSpHKM8mxDFWbIUcGHZE49komff/7Zhs4KybEZlofesz6ZzpZDS5BRhqGgrFUqhpQkleOz/rthsS4MA8euDQ0EtV3evXuXYeHUeQZ+7SWaxo88/Q8OenuusBnSyTEZLFKYSZSplQrTxpTwTCYgrYDKY8sPTyi9Sk0ZD4y3G7ZUClsgnRxrRwTGtDZqppOwxJZmnoSys9B3Z0MzwK0kqPrJqrF/FioIt7e3UZs1IzjOvVnMZklXzEw5gVi4w/UrZ7hoYQQBS9R15L2IxgE3q/uN73mLWxOYISTBPPPxg42SVQwfyijjmUgnx7rkUHqjzHRax0WO84HUzZRMTGrQIYlB02rYix1q5Y14kBAvotoopCSdHOvFX6p2ocVOOdb/Fual0/x0AwsjyMoibrjozVvRFtJp34E3WcBxxRx5KwrjLC6jj6dAURq2beHONzmo9YuTsUqZOGa2XmVWL7NNkpYrPY5HDnRbuGjxRML2zvclR7JyCw94zRuI2HOXQC+cp+8ifcVWyJnUuWGgJJMuh1WTwhSGJaxPqQMSvAsRy/1klcfQ1JhY2Uyh1AdZMUNiuO3fhvNl2LJXmMjd3d36UqRzMMa8XF1d2aCEZFU5FWaQ40JwniZsMNpH+n7/bQ6uevfuXeK1ASi3DDRSCzNS5LjQTWLTGCPQZ2y2z4K7gUgCpvviC5FImg8KS4Fs7TS2KkagJ/BEd1L7LVAXDzRBEnw+PSJx/VoYQZHjZRPJpeAjUvf399CRNMIdCdnRw55ICBnIwX1NhSVS5HjZROqY8pEnGXpxqeszQ+mhD5m3Uom9Tktn/3khN4ocFzo4q7DQa1jH/q5Put5dw6/QxF/IMMMqsODiW5AKm8JHjlHCsd7bWeOOrPiz98yH9D1d/lVaYcWUTLBUokrGWek88orVDV9JBu9ZOV6WdUafFnaueSfaIh6YcVPYDkWOl0pUb+BZOW7YQBbfMXwXd3d3WlaivmFssHSyjw99HHRnHck+ET6dIvqZU+S40IGnkpJm0ZVQFqwJ1bRdfPGELCUHxoaGoDrdqyWNHBcyp8hxoYOzzgcBXXNffvkl9Jfa+NfndkQsNI6hWuS40BQ5XiKR7DWDpyL/+uuvn3766UZ6ogLGvBleEmnAYmFZbKIUrYxIUz8MPgJBmvKGITnGJh3EiufgHqPtMZqyPvNJ2cIspMsEhVDEkAMX49x0+eGHH+iaP/zhD1BhkuPffvuNbOrZZx5HBdufe/rW/Ukpx57tnkJ60mWCwrIgVR0ww7/99turq6tXr16RjnzzzTf39/ez76GXkuBfWnzHhabIcWGAs61aUiW6hlRbm8MwljH6bWuG2HDDZUBzEwxzLuRPkeOFMVCkg+O50himPuuLSYXJWCaT2Qx309vXrpLhtS+QdlSHPTNiYqfX4nWnwjDwp+14J2+YDhqYEelTBBQ5XhiJ3bIXTRwgtb1j7IlTINZGqaHdC5UJevmq7eKjaqlPkSHHqLeu1b6RF0VyEII7W7IF4ltxD/NFGYwSET+puF8kjUAXOS4MQeo/3AAPzp7RIVjvggpG5sY1bK6mX5HpLIVDGiRW5VeFUGAGP8Uz/Q2Ve+k+GDtEiRWvMityXDiDp8siHmSYQLN2PPfPns4JMfk7vRb0/mhAaHOYKpvg4zQ2CwklRWY8exZZke5Pieim73SyztwFg1stw3KMyueff351dWVDszHo0BrttDGTmdJkOkEF6DVQSinELbGffPLJzc3Nn/70pz//+c8SjRS9H+M0Dp11GE//ttlpuWBIeLIUbzh3QfftiQl0pFMhW9wKWcyxqNBzTbbbOdqXJ1RmYNGYiKq5uyaGHtE9qY1M9u8PP/xA1dibN2/kFCkvyrCEpInGTjmm+iPN02Mz+xopZBLVyvs0hY50KiyIZLnQFOmll2R6fypF9FEoS/a0H3STvp5VCof7slKz+EiOzcaAnUIZnDRPmQVUb0GkcApUH5wdFerDatNpI4yWkhFof+jS5XgAilJSTIj12VEiDQ+rGNZ0cWLCmyHhybpJ1yfH1AShNNrF7FUbAV5pisNkbem0NQZUIAbS6l+xHA/wzAuKotQZpYY/x4y/NmhZxMXqZERWJseSCfOEatmBPDDMqtJp9czlO9ZU3H2xTTkeAH6JN2/efP7553pMseb169dyXJ1bEiQgfXKcPvNMB112NjQzrseuMZv7h8EYoc9DdsfaCBiaqqH2oDQwq3Zqjb3X8nEL+SyfSVntk08+saHToLS7urqyodGgTPL111/b0Aup23X3CcqikjntdS1ShyWzi0Gffg28ap5QvPm4j3IA3bk29Bzd6ZQDZDtQ1FMpvXQI4b6dBImW47hqainMIsfEzc3NRDeZBqlM97QnovH27dtXr17Z0Auhd64vmegFOaYMmbht0SfHywJOgAUV5xFOlbzSCWNWKPfQgWsJjgP7U9A9VznY/tL0DgUEZc/92qNTSg9RomRKqRr0aKoDRjcqx0GRltJlLKSM2BgceZbdRTZZJsCm9C8gWaQT/AwJlAVzohLbJmExDscEkdaJjkOZqlS3kyAGoKJV856nRgrT+5cgUj6LbITi6urqbPzEoE+O/WViRqBoKWvNsBx5drVnE6o7nZKBwhlkyJ4/98wi8qKLiavEEia4VRqKTcUdfWR7mvyHMQlw7tNvScFNASN1Tmz+iOvAnT4XA4qQzz//3IYmoU+O58o8F5GssoyKZ5OoO53SEHA2ywjgxJjr6aGYq0S5cuwiHa3E2Xjuk4x46KiD78LThBkB/G8+kRaD9HEbCp/21iKAv8WGOsyQTmSWVjxGwp6YAzSc++ZW5U/OcnwR6SXDjTqqocM21EjfybiTBwWPNE/Sx20QVtbfQyJzNiHOnA4OtDieGTKCY/LFRwLiakoagivL2ZwanM6oo8BQqzLunSVmgkeaJ+njdjqYd2dDF85ZYz9pOpncmRXo5Q9SDmOjGxamxQ3vbcWze3VUoz9hx3PJ6nanZ1TXYMfI58spuYOA8C+++MKemMZcvuNO4Mi6dIQlgA991zUK0DzRxL800YInVuepPY8HtaHZ4OlsXRzDXccd6RQDyjqLiN+707Vo80R3QrolSpc9FF0cyJWUFqIUu9PVFyu1GkvNgyVM450eDcUf0LJxPDA2NCadImVAR1/FvjW3fxI887YRD7w2+fvB/VvdSNup8SSSFsETq/NL6bZ5+uh8GvWLBhnGhjIpPpseTxll2ErPBwwMsKG54qarKbFSwrXYuRIAKuW0EYmRswjET1xlmUg9uHF1cJ55Vw4b2gPpWs3jfyqWPBin4JqHtNOBj4vDjbSdkmOMvIY3L2xi+X9pDlzPulpmGvpSpDs0IO6uaPlDBWOnGoM548atKbEw9iEl7sVuCdcGV802l5T5R54WhZ+4yjKdsN1ow+getmS4kablGAvYN4ESq2kXGGM1jl7MQ7FnbOjqoEq30+aLmE5o6C3FKDYceSZrtjmDXuy///0vVRvffvutOYWSXPOIEd0xDbOrOh3TItpasbvZuEEItBwRDjWJJ8fuYOR4pJR+wY20HeOm1/TEgtd7QI6TRfVFdL7qKulsBET8+OvlrPfRR1aZY99ubCEOQeLHH380l1WtHLvdUHvu66+UVSUGV+Ws7Yub4BTazrqEu8oShE6TIQZuSUiAG2kixz///LPRxz0PkhudWHhWnxxrl3RWJO4/mBGqet1uKptOoaBoHejTWBBkRs1rR6CkofBQlNL7vHv37rPPPkOzw5UVt+wZ9FpTUsLhuNRqKCUc7lEpJ1Hl+OzLByHSy5/FfS602ARqRicWzvbJMTWqKPDTTz9F3zWuATve7tpcnwAqZbM0WWbk0VmZx6ZTEKrTvLJoKL7cSiwxeIcHnvluJo+5hdkte83pZVSYxbaSEg4qtR6QlPAjj8uWO0SVY3pWgpwzlwnmRlqnHAdPrM4s0bAc3Nzc3PMmUg9zL5ZmfGsbwSRNdzpN4dnZ5nLpkPzNmFFQovACNU9S0Gc7nRUmBIEiczvlE0dzWC4jrb9rl2u5UyOXdVtHxhLIr8JyHXn0t2uSJMONNB3JQvDE6swSADnqf//7H0TZZ3xIJLZmGgOTJXrTaTRL9xd3Qlk8ZQvu2A53lWL5yCseuDriuWgvyhgV7FBf4SpLKNASt6GBuGNsaCo8I00SK5R718Qn5QGjubUaZfjEOznAAnDzWyTcOmk76AwZMt+jY9eGroW7+Ctzwn2mVVjok1G3qZuG2FERw0E0vFVHAmJHWh+epfKWF4DWIZhheBt/8dsZ68jZoRaJ1EZe6eQJalQbuhYoa8bQCAFWYd1OivUkdjnpI7aySDM8IJ6qFI/YkdaH54f3Oe6xSrjptAjLXNk4Bx55eQYce6WTDxtpbgT3cEGFRzcMkY/T5+YEynIXbsJ6zVMkbGhyEkRaJ6G+HXpdcb+fO4xyNCu24TyRDqEw6dTMl9USQ1kniNW2azvoJt4tvRCDZMldqYG3I8Do3T5XT2KSRZpB5DhsboGLeWLv33EJO0PHhkwxZNEwERGw2yF/LsrTrhEBp0eovsGLXiYgyZSF8tV11/wlHw48ty3Zq55lrjcRvTPDcqYj/X53l+wIp9FN9S2DHB5AjqN2hWfIXdfgJBfIrsixyMq4XNuH0akpdspFJFYW2FD+Zb7OcleBxJEmpCmez7xSWOWstjE8cj/DZJoFpFGAdKII9Swkq2G4XB15IxZ4xMZ10Pljsj6JfqQHGYZjIB7o64fNi5ESAGYahtlmW7znirQ0cqxB7582R+CdO73qheAGe3DSFKgw1vGR9x61oWuHRGHAOUO5kMyEA09opizo+isCMlfkz6Us4MArXqKEA/h/nhIuQjSCuSINBkEQ59hFoN9PRPk9711rrsm8Hy/2eCphz/tJTpXjNO+aIZ1VPcnE1dUVVBh6/cw7KMfTiG3K8UKZK9KqDEagou1CtvDNzY2Ixly5N09eJkbasAtxq7uN4OYksgVev35NWf/vf//7Tz/9JLbbrms2XSjc1wBUDUS1yudSlkUzV6R1mg5pqBk4lI686RS9zJdffvnNN98080VInrx44WzYJWTrpEuDuL2QzyjbjR4+PJrb080pUmJfZZBDz3rbeRKpXU9WoY3EJMwox5ojr+oJgf7+++9hu9iLAoE+BspyVEAeeO2tpl18Ri+S17AIPvK+CvIvXYZ/KdO+b/cEaNjAx8vDzAqeSV5uasO8KQMGl9IpHNVM9gGedBuaN4t74U7gUrehebDn1bdtaCCqdoAHOn6bdsUlnIV2IYl3p4aF+bdRbQvUJTiOoX6TrOMn3m3Xhm4Jyuj59ws3s7ZVwSIqLcMS39lldpfxACQg8VydIsdYqQ4hWmqr1p/uhhuzt1OOdXgoXtoxNsybnG3DNP2hMWrINTEw+GQRUHUr9lQhOA+MDQ0EnNQNG8VoHVanW6iIXjftHHpR4YrR/+Igthy/vIYN88a16jdIthVSH9epFvk2g0mCO9oKAzypReuzRY9KDs6DM+vV+NBdw7zPa9Enx+4dJvLivbFh3qQp1ZlzaCebL4UjY0MDsefpGDZ0+Wby4qjUZlrZUp3uex0WxEDNgzpQQtFiRuZ/VvMGpPxCas2/zakc37ULDe4ZhAdkpBzrWiIgujNUHrF3+kPRTS/tEfoX/aHyr/SH7tupyaYBEpDglWQyHhkbOoF1dH8BU68k8H1tjeCNfc0Db4kC0YQoI/zAnF77YqPowH3P1FbcqonZ1BsZIzGikqRB10iohdz+0Ea1I6AmGM0j/wJ5QznAzzvNtyksV441j6cruQzU/Kgd5d/g8VkYzbLqjBgaAkwWDdUiFDmOx8gYiaFBNYPjqh2GUjn9ng1XfToQZnJff6hO9cpZ32Q6wW+YAzo+H3lfKH2qdBvkybKyYjw5PvBKftSepggxWjEFrItiQ4MyMkYiJTxS6FnNKKuc/lAcwP+gawX86/aHxpbjeC2X1RCv4KXnwEuR2NDC5awpV4RiZIwMNGan4EpbZ3+oSKr7r9sf6v48OKXBvkrCOtYjoU2QZVE5LdrCGDkmAyGIL8aw57mJteoMbXr6Q0VzYTjTv7ie/tXuDjmI2hnaRGsrFOblbLLmsIDcck2BKubIiiVCIjZGjiMNcUP/JkSzVjuNN139oaYztOk32KHLfWeDEMo5VVgWlAkjlYVh7u/vF2G5DwPfrg1dIDLEayIv48FsmAcxZgbvTyewH8MtoxwkpoZJ8IhFEyPD5MaR9xywoYV+qEaZfa5K54C2EQRRgBfHrA3zIIYxeOAdXFBh1ryyeCi/UpCYGqZ4wTqRvL4mnRpI6Kjd7qGsk3wwFtgshKoPgnzISDkO8uw1QfEY1RmyRMhaDFhtR+qDHaBT/p6enjw/anoNfVjUkqTjCKUkD7y2fX062wvdTo+8I8l73seLxBcLn8HF9NRunIZ4di9A4HveaEpyIEJw2YfHB/qQl1e3YR6M+9WKKXJ8ESNMEk8R7GTE4/qgVB7xJmjw4fjIa/6env8AyYe++eydhAkYEZmdaEP7qBb20kqlZ5Ndt9t7Dl9AEiwJh7PurDT3PqOhm4+5S5Bn58BE+0UoctyJjl7kWsSST/7Zn05U7Su39AhX4PRvL+1mkdE7gn7zcXKs0cLR8HdpM7zTJF8xob7XxKorx6aqu293Fh6+oHIm8VbOrDRznyls3VkR6kM2LscHngQl/9a8bbYuIWhF/vvf/6aIQgtRLq7aiTm4plECqpW0UwQr3hazQT7mK8WZIL+V28pP8Dh9c5Fa/cI17/VJf1EycVuRY2rebsF6TUAQh8xZOd6zI0IuQPqevaBy9hisnFlp5j6jocz2Uo5ssAfTnz2RUM3PUB+ycTluODejv05bxDqvI9eacBzjFHI/AmGQisjiuP3FR6rWVJHSiNKya2kcORYVhkux4SYnspPcrWm9io3z5pBjHVKYSJB1Nowci5/X5DSRfulbHr6A3k0uQO2r82TT86BxfMiENtiD6c/WwJIyITrQtB/d5uee0SEIPBsS6kMo2dybbw1EZqfsXirHDaeyDvGXY5MQ5raUl/AvVPWRkfamPEXymCvHt0wxjUNROQ6BESADIFG0Guikp0IK9ZQ8IBfgevcC+CuQFSGX6B7Eg7QuydNH8yED22APOsvGpeCb3/Om93RD+dqK1/7YsxliYtYtt51RT/EFG61qF7Wo2lJqCqc+nkKo+ywa9GLrxp1OJn85ll7scXKsB9XB22BSBy+J/KCvrxi5DMfmzZEt79v9fgrTobSYPmxGMoBunHUiciEYGXUvcENcC3I6GCU5JlfpDDqFzmIpB+YCKQNSwHQthwsoaZ+dDe2fu5z0OA5VqDrFYmtQHjUDbyV69zz9/dCO3BKlwzF6se94i0mkacW2BkJw2V277LemauVYPA/IGzVv6Y0KXrsd9A9xoIWg0/DBm8s1kGO5WMILU5juexQ5XijiJBnzDaFqBh2DKEX6wFwgKiwHJg1qRgwfQYoQwGU4DpWEUcf/LwiJ+T0blVpMr3lYKGIeOossiMtw9pZXw0HIzc0N0he/qtiM1RUthBsCihuilsXFt+0OaXJWdxlJ+ZecAOietzy2CRkGmo53a7jM3PMeCHCm4d3cSqJwKSYVRmD6hxeHCMjIbwiiyDoGq9aFhFwugZLdUcz0AYqEvoDuYMRXSo65DMehkjBI73AhB0rNOgtmAMOm0HXJSD2a7n1vTtVQ91GKHJOw6r7OTpei6Qw98thsBNLxB4+M02cKQslxkMqpkAPF2p2FLbv7SKM+dmCcnvJlevuiYTW84yUxRYvRlYn2IEIondB+FMmT5qdcUDNyAR1jhIr49eE+rrkRisukUTy9XilafClBMk9hTWxZjqXHohktx0HsyiA3mZ3pHRFbI0/fzlMGixdvmW0qsu391v/4M31sSrMWOV7HVxS0R6uQnsoZM74FjHqMlJLppgTms1IBEL/EQimdP4XCdNDlbkNXzZ7RIeO/X/eJbZbpructU/w8Bc0x3KYT+YNxnCbQ/u9PGQbfFNN4GjlUZo+MDS3MxHZU5fb21lWP8XJM1rF7u02x9MHnhaYM88iMFXgvfehrB4xXkw36egxUv215+HpAtmMTFc4SZPhp5vRl+El6unHfX9XuBVCYSPpmVqdtUsgBzBuwoSvi2L/L7SQ5lpVWtkkp0oVCDDDVy4auggfe1s+GtkyS48YZN7cdBuK0MJr379/H61g7u/piIR/2vEOoDV04T09Pw9l7qpimb2ZmQpHjxbFZ02GhrGxiiM+irAEy6O32NkfYbCWUkoo3YrChF1Is4kWz2+1Woy2da3YbAsjx6l3vBtKIbc6vnxdsHGNDBzkyNrSwKNahLZ4tM6+LzhJkCYulsLI21FIg40JM3YEBLY+Pj9Nt6kI+PD09Lb3P/PF007IBwshxs5n2OwnxgBYUkqFTYYThXFgQ2KVlieWOsiVZ9/7DqIPJ8Uba7+toOhUKi4MMvuFhCbmBVdJs6CDB5JhqsGVF1giofl56u6lQWC5BenfTgJ00bOg5Lv7BAMMjnJeO7A5VKBTmgsy+/GeI0BuO614KKcfN4Py/RUOGv78DqFAoRKVSO2pmBYaZje7JCCzHzUq9qyPaHYVCIRJkG2ELTXtiVshoI/Wb8lZRVIbeaTXD7zF9fnR1VygUInHkZSpz8F3sdrsgC4pFkeM1SVildqQuFAoZEkoNLwX1waXDJwaIIscND0JYSh/oAGeX/CgUCjmAvY5SmoAYUxy2ez+WHDccQVO82rNTMza0UCjkChlP9/f3JDt0EEl5yESj+5P0e060u4iIcty002ls6BJY96C9QmHFRFJMkviKiaf1ceUYBI+X2CzaqC8UCgL6+sgoJI2+dCzwnsHP0zSUU8hxs5DB2w0nXhnTViisFZJXdL7BziWd3bWQQCGQjumaS7U7COmkR6/IlSeXrvdRKBSWC5V32L8ae1Fa0slx09qeefoBSIgXYb8XCoW1klSOAeauZDKAjOpDapusYExeoVBYOjPIcdPO7J5dkQ+HA1nrq1xko1AoLI555BhADQPOafEH9UFxExcKhXyYU46F29vbh4eHBOL4/PwMIc7Tf10oFLZMFnLc8GrC8BvEE0pSfHrEahbTKBQKKyMXORZgwGJI4MSBcYfDAWvyL25bl0KhsEGyk2MN6Sn24ICLmY5JXjvXbSKDF1sIywBvOpio5oVCoZCS/we9Wb/vjPy8TwAAAABJRU5ErkJggg==>