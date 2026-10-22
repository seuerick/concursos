# DATAPREV 2023 — Cargo 7 (Desenvolvimento e Software) — Itens 51–120

> **Fonte:** Cebraspe — DATAPREV 2023, prova de Conhecimentos Específicos (Cargo 7).
> **Uso:** referência para baterias de questões e simulados. Itens julgados (C/E) com justificativa.
> **Nota:** os itens 119 e 120 dependem de figuras (BPMN) e não foram julgados aqui.

## Julgamento dos itens

### 51 — E
Para garantir uma correta compilação de um código escrito em JavaScript, é necessário que as variáveis sejam definidas e inicializadas antes de seu uso no código.
> JS é interpretado/JIT e possui hoisting; não exige definição prévia.

### 52 — E
De acordo com o Clean Code, o programador deve ter o cuidado de declarar todas as variáveis locais em um único ponto, no início do código, como forma de facilitar a compreensão do código escrito.
> Clean Code recomenda declarar variáveis perto do uso, não todas no início.

### 53 — C
Web Service possibilita que recursos sejam disponibilizados para aplicações clientes, mesmo que estejam em sistemas diferentes e usando linguagens distintas.
> Correto (interoperabilidade).

### 54 — C
No SonarQube, a complexidade mede a quantidade de caminhos possíveis na execução do código.
> Correto (complexidade ciclomática).

### 55 — E
A principal diferença entre uma intranet e uma extranet é que a primeira é uma rede de uso restrito, enquanto a segunda é uma rede de uso público.
> Extranet não é pública; é restrita a parceiros autorizados.

### 56 — C
Os registros UDDI podem estar disponíveis de forma pública ou privada.
> Correto.

### 57 — C
Com a adoção de DevOps, na fase de operação de um software, as equipes buscam identificar os problemas antes que afetem a experiência do cliente.
> Correto.

### 58 — C
No XSLT, o processo de transformação do documento XML usa XPath.
> Correto.

### 59 — C
Apesar de primar pela agilidade, testes ágeis exigem processos bem definidos, sob pena de perda de qualidade do produto final.
> Correto.

### 60 — E
Na metodologia de pontos de função, qualquer função que apresente informação para o usuário por meio de processamento lógico é considerada uma saída externa (SE).
> "Qualquer função" é universal demais; a definição de EO exige dados derivados e envio para fora da fronteira (EQ também apresenta informação).

### 61 — E
Com a adoção de Scrum, o Scrum Master tem o papel de liderar o time de desenvolvimento e administrar os recursos do grupo.
> Scrum Master é um facilitador (servant-leader), não lidera nem administra recursos.

### 62 — C
Na aplicação do Kanban, é necessário que se estabeleça limites de trabalhos em andamento.
> Correto (limite de WIP).

### 63 — C
O reuso de software no nível de componentes pode exigir que se faça adaptações e ampliações do componente com código próprio.
> Correto.

### 64 — E
As técnicas de entrevistas e análise de protocolos, embora muito usadas, são pouco recomendadas por estarem sujeitas a produzir um produto final com informações pouco confiáveis.
> Entrevistas são recomendadas e amplamente usadas.

### 65 — E
Os requisitos funcionais de um software descrevem o que o software deve fazer, considerando critérios de desempenho das funcionalidades.
> Critérios de desempenho são requisitos não funcionais.

### 66 — C
Uma vantagem no uso de CSS é que, com ele, é possível fazer alteração no design sem afetar o código HTML.
> Correto.

### 67 — C
Ao se utilizar o HTTPS, uma sequência de passos denominada handshake precisa ser realizada para garantir a segurança da comunicação entre as partes.
> Correto.

### 68 — E
O uso de PWA traz praticidade e velocidade à interação com o usuário, estando restrito a alguns browsers específicos.
> PWA é suportado pelos principais navegadores modernos.

### 69 — E
A garantia de segurança e confiabilidade de um blockchain é feita por meio de uma terceira parte mediadora, cuja confiabilidade é publicamente aceita.
> Blockchain é descentralizado; não há terceira parte mediadora.

### 70 — E
Em uma arquitetura hexagonal, como as classes de domínio estão relacionadas ao negócio do sistema e seus dados, elas devem ser responsáveis pelo armazenamento de dados e as tecnologias usadas para esse fim.
> Na arquitetura hexagonal, o domínio NÃO deve ser responsável pelo armazenamento (isso cabe aos adaptadores/portas).

### 71 — E
De acordo com os conceitos de inteligência artificial, as máquinas reativas têm a capacidade compreender os seres humanos, entendendo seus estados mentais.
> Máquinas reativas não têm essa capacidade.

### 72 — C
A garantia de usabilidade de uma aplicação exige atualizações constantes que podem se basear no comportamento do usuário.
> Correto.

### 73 — E
Um sistema de gerenciamento de conteúdo desacoplado oferece menos flexibilidade do que um sistema acoplado, quanto à interação com o conteúdo criado no back-end.
> CMS desacoplado (headless) oferece MAIS flexibilidade.

### 74 — C
Os direitos concedidos a usuários com acessos privilegiados são restritos e controlados, sendo necessário ter requisitos para expirar esse tipo de acesso.
> Correto.

### 75 — C
No gerenciamento de informações, deve ser evitado o uso de mensagens de correio eletrônico de terceiros para o fornecimento de informações temporárias de autenticação secreta de usuários.
> Correto.

### 76 — E
Uma política de gerenciamento de chaves deve estabelecer a forma apropriada de lidar com chaves comprometidas: deve-se manter registro e auditoria das atividades que tenham relação com o gerenciamento de chaves e não se deve jamais destruir chaves comprometidas, as quais devem ser somente arquivadas.
> Chaves comprometidas devem ser revogadas/destruídas, não apenas arquivadas.

### 77 — E
O controle de acesso a código-fonte de programas deve ser vedado à maioria dos times de tecnologia, exceto ao time de suporte, que deve ter acesso irrestrito às bibliotecas de programa-fonte.
> Time de suporte NÃO deve ter acesso irrestrito (menor privilégio).

### 78 — C
No desenvolvimento de uma política para criptografia, o uso de criptografia no transporte de mídias móveis é opcional, desde que, para o transporte, as mídias sejam lacradas e rastreadas durante todo o tempo em que estiverem em trânsito.
> Correto (condição satisfeita).

### 79 — C
Em um perímetro de segurança física, as portas corta-fogo devem ser providas de alarme e monitoramentos e devem ser testadas em conjunto com as paredes, a fim de se estabelecer o nível de resistência exigido.
> Correto.

### 80 — C
A modelagem de ameaças pode ser aplicada no componente de um software, para apoiar a seleção de recursos de segurança.
> Correto.

### 81 — C
Durante a fase de implementação, são aplicados padrões de codificação e testes.
> Correto.

### 82 — E
A fase de implementação contempla a aplicação de testes de segurança sem o uso de soluções para análise de código.
> A fase de implementação usa análise de código (SAST).

### 83 — E
A fase de design prevê a definição da estrutura geral do software relacionado à segurança e a realização de revisões de código.
> Revisões de código ocorrem na implementação, não no design.

### 84 — C
Na fase de suporte e manutenção, deve ser estabelecido um time ou grupo responsável por respostas a incidentes de segurança.
> Correto.

### 85 — C
Com ferramentas de análise estática, é possível identificar vulnerabilidades do tipo XSS (cross-site scripting) em aplicações web.
> Correto.

### 86 — C
O processo de análise estática envolve a identificação de problemas na sintaxe do código-fonte.
> Correto.

### 87 — E
Na análise dinâmica, é possível revisar todo o código-fonte sem a necessidade de execução do software.
> Isso é análise estática; a dinâmica exige execução.

### 88 — C
Durante a análise dinâmica, é possível identificar exceções que não foram tratadas.
> Correto.

### 89 — C
Security misconfiguration indica que a aplicação pode estar vulnerável devido à utilização de contas e senhas default que estão habilitadas e ainda não foram alteradas.
> Correto.

### 90 — C
Insecure design recomenda o uso de LIMIT e outros controles SQL para prevenir a divulgação em massa de registros em caso de injeção de SQL.
> Correto (OWASP Top 10 A04:2021).

### 91 — E
Cryptographic failures tem como diretiva de prevenção bloquear o acesso a recursos internos de um ambiente, exceto aos recursos que realmente necessitem ser públicos, como websites disponíveis para a Internet.
> Bloquear acesso a recursos internos é prevenção de SSRF/misconfiguration, não de falhas criptográficas.

### 92 — C
Uma POSIN deve estar em conformidade com a legislação vigente, com as normas pertinentes, com os requisitos regulamentares e contratuais e com as melhores práticas de segurança da informação.
> Correto.

### 93 — E
Competências e responsabilidades, apesar de serem importantes, não devem constar da POSIN, pois sua definição é restrita à alta administração da organização.
> Competências e responsabilidades devem constar da POSIN.

### 94 — E
Uma collection no MongoDB é equivalente a uma tupla ou registro nos bancos de dados relacionais.
> Collection equivale a tabela; documento equivale a linha/registro.

### 95 — C
Transformar uma tabela de PESSOA em duas tabelas, de PESSOA FÍSICA e de PESSOA JURÍDICA, é um refinamento de especialização.
> Correto.

### 96 — C
No MER, a entidade associativa é utilizada para representar um relacionamento entre relacionamentos.
> Correto.

### 97 — E
Para representar a propriedade atual de um automóvel, deve ser utilizada a cardinalidade 1:N entre as duas tabelas envolvidas.
> Propriedade atual é 1:1 (um automóvel tem um proprietário atual).

### 98 — C
A DCL (Data Control Language) é utilizada para controlar quem tem acesso aos objetos do banco de dados.
> Correto.

### 99 — E
A DDL (Data Definition Language) é utilizada em bancos de dados para comandos de UPDATE nas tabelas.
> UPDATE é DML, não DDL.

### 100 — E
Uma tabela está na primeira forma normal quando ela não contém tabelas aninhadas.
> 1FN exige valores atômicos (sem grupos repetidos); a definição dada é imprecisa.

### 101 — E
As colunas de uma tabela na terceira forma normal devem depender da chave primária, de forma direta ou por meio de dependências transitivas ou indiretas.
> 3FN exige dependência direta, SEM dependências transitivas.

### 102 — C
Para estar na segunda forma normal, é suficiente que a tabela não contenha nenhuma dependência parcial.
> Correto (2FN = sem dependência parcial).

### 103 — C
Uma VIEW é um objeto do banco de dados, mas não possui nenhuma linha em sua estrutura, pois faz referência a linhas e colunas de outras tabelas.
> Correto.

### 104 — C
Ao executar um comando de SELECT em mais de uma tabela sem a cláusula WHERE, o resultado será o produto cartesiano das tabelas acessadas.
> Correto.

### 105 — E
O comando UNION é utilizado para combinar as linhas de duas tabelas, mesmo que as colunas dessas tabelas sejam de tipos e tamanhos diferentes.
> UNION exige colunas compatíveis em número e tipo.

### 106 — C
Um dos objetivos da BI (Business Intelligence) é fornecer informações coletadas em DW (Data Warehouses) para tomada de decisões.
> Correto.

### 107 — E
As ferramentas utilizadas para manipular dados em Big Data são as mesmas utilizadas em bancos de dados relacionais.
> Big Data usa ferramentas próprias (Hadoop, Spark etc.).

### 108 — E
O gerenciamento do escopo do projeto dispensa a criação da EAP e abrange tanto coletar os requisitos do projeto quanto definir o seu escopo.
> O gerenciamento de escopo NÃO dispensa a EAP (WBS).

### 109 — C
Um portfólio de projetos tem como objetivo facilitar a eficácia da governança e do gerenciamento do trabalho alinhado a estratégias e prioridades organizacionais, em que o gerenciamento de projetos visa executar os projetos da maneira certa, ao passo que o gerenciamento de portfólios visa executar os projetos certos.
> Correto.

### 110 — C
Nos ciclos de vida altamente adaptativos, os riscos são reduzidos pela elaboração progressiva dos planos iniciais, em que as entregas acontecem com frequência de acordo com os subconjuntos avaliados pelo cliente de todo o produto.
> Correto.

### 111 — E
Um dos princípios do Scrum é reduzir o desperdício, assim convém que, na sprint, o Scrum team se subdivida em subtimes, de modo a maximizar o paralelismo de execuções.
> Scrum team é único e multifuncional; o Scrum não prevê subdivisão em subtimes.

### 112 — C
No Scrum, que é um framework que aborda soluções adaptativas para problemas complexos, o product owner ordena o trabalho para um problema complexo, enquanto o Scrum team e seus stakeholders inspecionam os resultados.
> Correto.

### 113 — C
A análise de riscos inclui a consideração das causas e fontes de risco, a probabilidade de ocorrer um evento específico, a probabilidade de que este evento provoque consequências e a gravidade dessas eventuais consequências.
> Correto.

### 114 — E
Na gestão de riscos, o nível de risco refere-se à significância de um risco, demonstrada pela combinação das consequências e de seu impacto.
> Nível de risco = combinação de probabilidade e consequências (impacto), não "consequências e impacto" (redundante).

### 115 — E
A solicitação de um usuário que inicia uma ação de serviço acordada como parte regular da entrega de serviço deve ser gerenciada pela prática de gerenciamento de incidente, de modo que se restaure a operação normal do serviço o mais rápido possível.
> Solicitação de serviço é gerenciada pela prática de gerenciamento de solicitações, não de incidentes.

### 116 — E
A prática de gerenciamento de segurança da informação tem como objetivo principal a elaboração e manutenção da política de segurança da informação da organização.
> O objetivo principal é proteger a informação (CIA); a política é um meio, não o fim.

### 117 — C
No domínio entrega, serviço e suporte (DSS), há processos relacionados ao gerenciamento de solicitações e de incidentes de serviço, assim como ao gerenciamento de problemas e de continuidade.
> Correto (DSS02, DSS03, DSS04).

### 118 — C
O processo estratégia gerenciada do domínio alinhar, planejar e organizar (APO) visa garantir que cada iniciativa da organização esteja claramente conectada a uma estratégia abrangente, de modo que haja transformação digital na organização.
> Correto (APO02).

### 119 — (figura BPMN — não julgado)
De acordo com a notação BPMN apresentada na figura a seguir, a Tarefa 2 (#2) e a Tarefa 3 (#3) serão executadas concomitantemente.
> Depende da figura (gateway paralelo).

### 120 — (figura BPMN — não julgado)
De acordo com a notação BPMN apresentada na figura a seguir, apenas uma das tarefas #1, #2 e #3 será executada, ou seja, no momento de decisão (#Decisão), um único caminho deverá ser seguido.
> Depende da figura (gateway exclusivo).

---

## Resumo

- **Total de itens:** 70 (51–120)
- **Julgados:** 68 (119 e 120 dependem de figura)
- **C:** 37 | **E:** 31
- **Distribuição:** 54,4% C / 45,6% E
