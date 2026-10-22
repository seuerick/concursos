# TCE/RN 2025 — Cargo 4 (Desenvolvimento de Sistemas) — Itens 51–120

> **Fonte:** Cebraspe — TCE/RN 2025, prova de Conhecimentos Específicos (Cargo 4).
> **Uso:** referência para baterias de questões e simulados. Itens julgados (C/E) com justificativa.
> **Nota:** os itens 51–120 correspondem à prova de conhecimentos específicos; os itens 1–50 (básicos) não foram persistidos aqui.

## Julgamento dos itens

### 51 — E
Bancos de dados NoSQL são projetados para garantir, por padrão, consistência forte (strong consistency), priorizando a integridade imediata dos dados em ambientes distribuídos.
> NoSQL prioriza disponibilidade/tolerância a partição (CAP); frequentemente consistência eventual.

### 52 — C
Dados estruturados são organizados segundo um esquema rígido previamente definido, enquanto dados não estruturados não possuem modelo predefinido, sendo tipicamente armazenados em formatos como textos livres, imagens e vídeos.
> Definição correta.

### 53 — E
Em arquiteturas de Big Data, dados não estruturados não podem ser indexados ou consultados diretamente, sendo obrigatória sua transformação em dados estruturados antes de qualquer análise.
> Dados não estruturados podem ser indexados/consultados diretamente.

### 54 — C
Em sistemas NoSQL orientados a documentos, como MongoDB, os dados são armazenados em estruturas flexíveis que permitem variação de esquema entre registros de uma mesma coleção.
> Correto (schema-less).

### 55 — E
A ingestão de dados em streaming não é adequada para cenários que exigem alta confiabilidade, pois não permite mecanismos de tolerância a falhas ou reprocessamento de eventos.
> Streaming (ex.: Kafka) permite tolerância a falhas e reprocessamento.

### 56 — C
Sistemas de armazenamento distribuído, como data lakes, permitem o armazenamento de dados em seu formato bruto, favorecendo abordagens ELT em detrimento de ETL.
> Correto.

### 57 — C
A instrução UPDATE pode ser utilizada em conjunto com subconsultas correlacionadas para modificar dados com base em valores provenientes de outras tabelas, respeitando as restrições de integridade definidas no banco de dados.
> Correto.

### 58 — E
A utilização de índices compostos garante melhoria uniforme de desempenho para qualquer consulta que envolva pelo menos uma das colunas indexadas, independentemente da ordem dos atributos no índice.
> Índices compostos seguem o leftmost prefix; ordem importa.

### 59 — E
O particionamento de tabelas elimina a necessidade de índices secundários, pois a divisão física dos dados já garante acesso eficiente em qualquer tipo de consulta.
> Particionamento não elimina índices secundários.

### 60 — E
Em ambientes de alta concorrência, a definição de restrições de chave estrangeira garante que operações de inserção e de atualização ocorram com menor custo computacional, pois o SGBD utiliza essas restrições para simplificar as verificações de consistência.
> Restrições de FK adicionam custo, não reduzem.

### 61 — C
A integridade referencial garante que valores de chave estrangeira em uma tabela correspondam a valores válidos de chave primária em outra tabela, evitando a existência de registros órfãos.
> Correto.

### 62 — C
A execução de comandos DML, como UPDATE e DELETE, sem cláusula WHERE pode resultar em operações em massa que afetam toda a tabela, podendo comprometer a integridade lógica dos dados.
> Correto.

### 63 — C
No catálogo GoF, o padrão de criação Singleton garante que haja somente uma instância para cada classe, com um único ponto de acesso a ela.
> Correto.

### 64 — E
Enquanto o foco do processo incremental é aprimorar o que já foi entregue, o objetivo do processo iterativo é entregar nova funcionalidade.
> Invertido: iterativo refina, incremental agrega.

### 65 — E
A primeira etapa de um projeto de software consiste na definição do time que irá trabalhar no desenvolvimento técnico.
> Primeira etapa é levantamento de requisitos/planejamento.

### 66 — C
Na fase de levantamento de requisitos de um projeto, as motivações informais da organização devem ser consideradas pelo gerente do projeto.
> Correto.

### 67 — E
Um dos objetivos do método Kanban é colocar a maior quantidade possível de itens em andamento, aumentando a capacidade de entrega do time de desenvolvimento.
> Kanban limita o WIP.

### 68 — C
A metodologia Scrum determina que a duração de uma sprint é inalterável, mesmo que todos os itens previstos ainda não estejam finalizados.
> Correto (time-box fixo).

### 69 — C
De acordo com o conceito INVEST, as histórias de usuário devem ser independentes, negociáveis, pequenas e testáveis.
> Correto.

### 70 — E
Na estrutura de um storytelling, o clímax e o desfecho ocorrem no mesmo momento, ao final da narrativa.
> Clímax e desfecho são momentos distintos.

### 71 — C
O uso de mocks é recomendado para testes de unidade, mas deve ser evitado para testes de integração, para garantir a comunicação com todos os serviços acessados.
> Correto.

### 72 — E
Throughput e Velocity são duas métricas de software que identificam a quantidade absoluta de itens entregues em determinado período de tempo.
> Velocity é relativa (estimativas), não absoluta.

### 73 — C
O processo de deployment blue/green utiliza dois ambientes de produção com as mesmas configurações, o que permite um método de implantação de baixo risco.
> Correto.

### 74 — C
Sob o mesmo namespace, diversos contêineres Docker podem ser executados e interagir entre si, com compartilhamento local de dados.
> Correto.

### 75 — E
Em um data warehouse, o armazenamento orientado à transação não necessita de múltiplas operações de entrada e saída para carregar dados no banco de dados.
> DW é orientado a assunto, não a transação.

### 76 — C
É chamado de esquema estrela o conjunto formado por uma tabela de fatos, várias tabelas de dimensão e chaves estrangeiras que relacionam dados da tabela de fatos aos dados das tabelas de dimensão.
> Correto.

### 77 — E
No contexto de regras de associação, o conceito de confiança refere-se à expectativa de que um dado, grupo ou banco de dados atue da maneira esperada em dada situação.
> Confiança em regras de associação = P(Y|X); a definição dada é de confiabilidade.

### 78 — C
O k-means é um algoritmo iterativo de agrupamento baseado em centroides, isto é, ele divide um conjunto de dados em grupos semelhantes com base na distância entre seus centroides.
> Correto.

### 79 — E
Em mineração de dados, dado ruidoso é aquele cujo valor está fora do domínio do atributo.
> Dado ruidoso = erro/variação aleatória, não necessariamente fora do domínio.

### 80 — C
Na metodologia CRISP-DM, a preparação dos dados serve para limpá-los, tratando valores ausentes, outliers e inconsistências.
> Correto.

### 81 — C
Uma anomalia é um valor discrepante, ou seja, um valor que se localiza significativamente distante dos valores considerados normais.
> Correto.

### 82 — C
Histograma é uma representação da distribuição dos dados de certa base, conforme um ou mais atributos desses dados, por meio de um gráfico de barras.
> Correto.

### 83 — E
Enquanto um falso positivo é um erro do tipo 2, um falso negativo é um erro do tipo 1.
> Invertido: FP = tipo 1, FN = tipo 2.

### 84 — C
Em um processo de mineração de texto, a tokenização é o processo de dividir textos longos em palavras individuais, removendo-se espaços e pontuação, para fins de identificação da frequência de termos ou da estrutura de uma frase em um grande volume de documentos.
> Correto.

### 85 — E
Modelos de regressão linear são métodos estocásticos para modelagem da relação entre variáveis aleatórias e uma função polinomial.
> Regressão linear modela relação linear, não polinomial.

### 86 — E
Considere o seguinte código em Python:
```
1 import numpy as np
2 S = np.array([45, 55])
3 U = np.array([[12, 22, 33], [45, 55, 66]])
4 print((U.T + S).T)
```
A execução desse código resultará no erro a seguir: `NameError: name 'T' is not defined`.
> `U.T` é transposição válida do numpy; não gera NameError.

### 87 — C
O PROC SQL integra o software Base SAS e pode ser usado com qualquer conjunto de dados SAS.
> Correto.

### 88 — C
Considere o trecho de código a seguir, em linguagem R:
```
1 m <- matrix(1:9, nrow = 3, ncol = 3, byrow = TRUE)
2 result <- rowMeans(m) + colMeans(m)
3 print(result)
```
A execução desse trecho de código terá o seguinte resultado: `[1] 6 10 14`.
> rowMeans=[2,5,8], colMeans=[4,5,6], soma=[6,10,14]. Correto.

### 89 — C
Em tabelas dinâmicas de planilhas eletrônicas, a área de valores corresponde à área em que se devem colocar os campos em que se pretende efetuar cálculos como soma, contagem de valores, média aritmética, entre outros.
> Correto.

### 90 — C
Modelos de IA generativa, como os baseados em arquiteturas transformer, são capazes de produzir novos dados a partir de padrões aprendidos durante o treinamento.
> Correto.

### 91 — E
Em modelos de deep learning, o overfitting ocorre quando o modelo possui baixa capacidade de representação, sendo raro em redes neurais profundas com muitos parâmetros.
> Overfitting ocorre com alta capacidade (muitos parâmetros).

### 92 — C
Redes neurais profundas diferenciam-se das redes neurais rasas principalmente pela presença de múltiplas camadas ocultas, permitindo maior capacidade de representação.
> Correto.

### 93 — E
Em algoritmos de aprendizado de máquina, a validação cruzada (cross-validation) é utilizada para aumentar o conjunto de treinamento ao duplicar os dados disponíveis, elevando assim a capacidade de generalização do modelo.
> Cross-validation não duplica dados; particiona para avaliação.

### 94 — C
Em pipelines de MLOps, a automação de testes, de monitoramento e de re-treinamento contínuo contribui para a confiabilidade e para a escalabilidade dos sistemas de ML.
> Correto.

### 95 — C
A mitigação de viés em modelos de IA pode envolver técnicas como balanceamento de dados, regularização e avaliação de métricas de equidade.
> Correto.

### 96 — E
Modelos altamente interpretáveis, como árvores de decisão simples, tendem a apresentar menor transparência em comparação a modelos complexos, como redes neurais profundas.
> Árvores simples são MAIS transparentes.

### 97 — C
Diferentemente das arquiteturas tradicionais de N camadas, a arquitetura de microsserviços se baseia na descentralização da gestão de dados, em que cada serviço deve, idealmente, possuir sua própria base de dados, de forma a garantir a independência de implantação e o baixo acoplamento.
> Correto.

### 98 — E
A adoção de uma estratégia de camadas fechadas (closed layers) permite que a camada de apresentação acesse diretamente os serviços da camada de dados quando houver necessidade de otimização de performance, desde que a camada de negócio permaneça inalterada.
> Camadas fechadas NÃO permitem pular camadas (isso é open layers).

### 99 — C
No padrão arquitetural MVC (model-view-controller), o componente controller atua como um intermediário que interpreta as entradas enviadas pelo usuário e coordena as atualizações necessárias no model, de forma a permitir que a lógica de negócio e o estado dos dados permaneçam independentes da interface de apresentação.
> Correto.

### 100 — E
No padrão de projeto abstract factory, a inclusão de uma nova categoria de objeto em uma família de produtos já existente prescinde da alteração da interface da fábrica abstrata e de suas subclasses concretas.
> Incluir nova categoria exige alterar a interface da fábrica abstrata.

### 101 — C
No que se refere ao desenvolvimento de soluções mobile baseadas em padrões W3C, a arquitetura de uma PWA (progressive web app) utiliza service workers para atuar como um proxy de rede programável de forma a permitir que o usuário mobile acesse funcionalidades críticas da aplicação mesmo em cenários de latência elevada ou ausência de conectividade.
> Correto.

### 102 — E
O framework gRPC adota o formato JSON como padrão nativo de serialização de dados, o que assegura a interoperabilidade direta com navegadores web.
> gRPC usa Protocol Buffers, não JSON.

### 103 — C
Nas arquiteturas cloud native, o isolamento provido pelo uso de containers permite que falhas em serviços individuais sejam mitigadas pela substituição automática das instâncias comprometidas.
> Correto.

### 104 — C
A ISO 31000:2018 promove uma compreensão compartilhada dos riscos, e suas diretrizes ajudam a incorporar o gerenciamento de riscos na governança, estratégia, planejamento, processos de relatórios, políticas, valores e cultura de uma organização.
> Correto.

### 105 — E
O COBIT 2019 contribui para que as organizações atinjam seus objetivos de negócios por meio de uma gestão de TI eficaz, entretanto, como não inclui estruturas de auditoria com vistas ao controle de governança de TI, faz-se necessária a utilização da COSO no que diz respeito a aspectos concernentes à auditoria.
> COBIT 2019 inclui estruturas de auditoria/assurance.

### 106 — C
A prática de gerenciamento de continuidade de serviço do ITIL v4 fornece estrutura para a construção de resiliência organizacional com a capacidade de produzir uma resposta em caso de desastre, visando garantir que a disponibilidade e o desempenho de um serviço sejam mantidos em níveis suficientes após um evento súbito não planejado que cause danos ou perdas graves.
> Correto.

### 107 — C
Um KPI (key performance indicator) é um valor mensurável que se relaciona com metas, objetivos e estratégias específicas que ajudam a avaliar o desempenho de tarefas em uma organização.
> Correto.

### 108 — E
De acordo com o Guia SCRUM (versão 2020), a sprint planning inicia a sprint ao definir o plano de trabalho do que será realizado na sprint, na qual, para cada item do product backlog selecionado, o product owner planeja o trabalho e a forma necessária para criar um incremento que atenda à definição de pronto.
> Quem planeja o trabalho é o time de desenvolvimento (Developers), não o product owner.

### 109 — E
Conforme o disposto no PMBOK 7.ª edição, o domínio de desempenho da entrega trata das atividades e funções associadas a riscos, que incluem aspectos afetos à incerteza e suas implicações, sendo a capacidade de antecipar ameaças e de compreender as consequências dos problemas um dos objetivos esperados da execução desse domínio.
> Riscos/incerteza pertencem ao domínio de incerteza, não ao de entrega.

### 110 — C
Considere que as fases que compõem o processo de elaboração de certo plano diretor de TIC (PDTIC) sejam preparação, diagnóstico e planejamento. Considere, ainda, que se pretenda realizar a análise dos ambientes interno e externo da TIC por meio do método SWOT. Nesse caso, a atividade pretendida deve ser executada na fase de diagnóstico e, para o ambiente interno, podem ser analisados a qualidade dos processos e serviços providos e o nível de satisfação dos usuários com os serviços prestados.
> Correto (SWOT na fase de diagnóstico).

### 111 — C
De acordo com o DAMA-DMBoK, a modelagem de dados é o processo de descoberta, análise e delimitação dos requisitos de dados de forma iterativa, podendo incluir modelo conceitual, lógico e físico, de forma a representar e comunicar esses requisitos de dados.
> Correto.

### 112 — E
A função recuperar do CSF (Cybersecurity Framework) do NIST visa apoiar a capacidade de contenção dos efeitos de incidentes de cibersegurança, incluindo, entre outras ações, o gerenciamento de incidente, que, por sua vez, abrange análise e mitigação do incidente.
> Contenção/gerenciamento de incidentes = função Responder; Recuperar trata da restauração.

### 113 — C
Consoante disposto na norma ABNT NBR ISO/IEC 27002:2022, anonimização consiste na alteração irreversível de dados pessoais de forma tal que o titular dos dados não pode mais ser identificado direta ou indiretamente; consoante o disposto na LGPD, anonimização consiste na utilização de meios técnicos por meio dos quais um dado perde a possibilidade de associação, direta ou indireta, a um indivíduo.
> Correto.

### 114 — E
Ao final do contrato, os módulos implementados serão de propriedade da empresa contratada, que poderá repassar, mediante compensação financeira, os direitos de propriedade intelectual para o contratante.
> Em contratos públicos, os direitos de propriedade intelectual dos módulos pertencem ao contratante (órgão público).

### 115 — C
Na administração estadual, o gestor de contrato pode ser auxiliado, no cumprimento das atribuições do cargo, por recursos terceirizados.
> Correto.

### 116 — E
A menos que esteja expresso de forma diferente no edital, os testes e demais provas exigidos por normas técnicas são de responsabilidade do contratante, quando entidade pública.
> Testes são de responsabilidade da contratada, não do contratante.

### 117 — C
Estão entre os critérios de julgamento no modelo de licitação por concorrência: menor preço, melhor técnica, maior retorno econômico.
> Correto.

### 118 — E
Para fins de obtenção de preço estimado, a Instrução Normativa SEGES/ME n.º 65/2021 estipula como único método o cálculo da média a partir de um conjunto de três ou mais preços.
> A IN 65/2021 prevê múltiplos métodos, não apenas a média.

### 119 — C
Nos termos da Instrução Normativa SGD/ME n.º 94/2022, na renovação de centro de dados, deve-se priorizar a contratação de serviços em nuvem.
> Correto.

### 120 — E
Em contratações que envolvam recursos de cooperação estrangeira, serão admitidas condições decorrentes de acordos internacionais desde que aprovadas pelo presidente da República.
> Devem ser aprovadas pelo Congresso Nacional, não pelo presidente.

---

## Resumo

- **Total de itens:** 70 (51–120)
- **C:** 39 | **E:** 31
- **Distribuição:** 55,7% C / 44,3% E
