# ANÁLISE DE PADRÃO - QUESTÕES DE TECNOLOGIA DA INFORMAÇÃO
## TCE/RS 2025 → Predição TCU 2025

---

## 🎯 ESTRUTURA GERAL DAS PROVAS DE TI

### **Seção 1: Conhecimentos Gerais de TI (Q29-36)**
- **Formato:** Julgamentos Verdadeiro/Falso (V/F)
- **Tópicos:** Conceitos básicos e operacionais
- **Dificuldade:** Iniciante a intermediária

### **Seção 2: Tópicos Avançados (Q12-40)**
- **Formato:** Julgamentos Verdadeiro/Falso (V/F)
- **Tópicos:** Bancos de dados, arquitetura, ferramentas especializadas
- **Dificuldade:** Intermediária a avançada

---

## 📊 TÓPICOS COBERTOS NO TCE/RS 2025

### **SEÇÃO 1 - CONCEITOS FUNDAMENTAIS (Q29-36)**

| # | Tópico | Tipo de Questão | Padrão |
|---|--------|-----------------|--------|
| 29 | Computação em Nuvem | Conceito | Definição e características |
| 30 | Windows | Sistema Operacional | Recursos básicos e funcionalidades |
| 31 | Windows - Barra de Tarefas | Sistema Operacional | Localização de funcionalidades |
| 32 | Internet vs Intranet | Redes | Comparação de características |
| 33 | Antivírus | Segurança | Limitações e garantias |
| 34 | Backup | Segurança | Tipos e funcionamento |
| 35 | Controle de Acesso | Segurança | Procedimentos combinados |
| 36 | Firewall | Segurança | Função e operação |

---

### **SEÇÃO 2 - TÓPICOS AVANÇADOS (Q12-40)**

#### **Docker & Containerização (Q19-26)**
- Imagens Docker
- Contêineres
- Docker Compose
- Orquestração
- Redes de contêineres

#### **Bancos de Dados (Q27-36)**
- SQL - JOIN
- NoSQL - Modelo key/value
- Integridade Referencial
- Índices e Seletividade
- LIMIT e OFFSET
- Otimização de queries

#### **Data Warehouse & Analítica (Q33-40)**
- ETL - Técnicas de junção
- OLAP - Operações
- BI - Modelos (Snowflake vs Estrela)
- Tabelas DIMENSÃO e FATO
- ELK Stack
- Elasticsearch e Shards
- MapReduce
- Data Lake

---

## 🔍 PADRÕES IDENTIFICADOS

### **Padrão 1: Falsidades Comuns (Pegadinhas)**
As questões frequentemente apresentam afirmações que:
- ✗ Usam palavras absolutas ("garante", "sempre", "nunca")
- ✗ Invertam relações lógicas
- ✗ Omitam exceções importantes
- ✗ Misturem conceitos parcialmente similares

**Exemplos do TCE/RS:**
- Q33: "A instalação de um antivírus garante proteção" → **FALSO** (não é garantia absoluta)
- Q35: "criptografia, backup e classificação são os principais procedimentos" → **FALSO** (lista incompleta)
- Q40: "data lake requer conhecimento prévio da estrutura" → **FALSO** (justamente o oposto)

---

### **Padrão 2: Conceitos Técnicos Precisos**
As questões cobram:
- Terminologia exata (shards, joins, OLAP, ETL)
- Diferenças sutis entre conceitos similares
- Funcionalidades específicas de ferramentas

**Exemplos do TCE/RS:**
- Q28: Chave estrangeira deve ser chave primária em tabela de **origem**
- Q30: No NoSQL key/value, chave e valor ≠ coluna e dado
- Q34: OLAP decomposição cria exibição **bidimensional**

---

### **Padrão 3: Progressão de Complexidade**
1. **Q29-32:** Conceitos básicos universais
2. **Q33-36:** Segurança e operação
3. **Q12-26:** Containerização e arquitetura
4. **Q27-32:** Bancos de dados e otimização
5. **Q33-40:** Ambientes corporativos (Data Warehouse, Big Data)

---

### **Padrão 4: Contexto Corporativo**
Todas as questões refletem:
- Ambientes de produção
- Escalabilidade
- Governança de dados
- Segurança da informação
- Compliance e controle

---

## 🎲 PREDIÇÃO PARA TCU 2025

### **Provável Distribuição de Questões (Baseado em TCE/RS)**

```
Seção 1 - Conceitos Fundamentais: 8 questões
├─ Computação em Nuvem: 1 questão
├─ Sistema Operacional (Windows): 2 questões
├─ Redes (Internet/Intranet): 1 questão
└─ Segurança da Informação: 4 questões

Seção 2 - Tópicos Avançados: ~15-20 questões
├─ Containerização (Docker): 3-4 questões
├─ Bancos de Dados: 4-5 questões
├─ Data Warehouse/ETL: 3-4 questões
├─ Business Intelligence: 2-3 questões
├─ Big Data/Ferramentas: 3-4 questões
```

---

## 🔴 TÓPICOS CRÍTICOS PARA O TCU

### **Altos Riscos (Muito Provável)**

1. **Segurança da Informação**
   - ✓ Antivírus vs Malware (limitações)
   - ✓ Firewall (filtragem, tipos)
   - ✓ Backup (tipos: total, incremental, diferencial)
   - ✓ Criptografia (confidencialidade, não integridade isolada)
   - ✓ Controle de Acesso

2. **Bancos de Dados Relacionais**
   - ✓ SQL - JOIN (tipos e funcionalidade)
   - ✓ Integridade Referencial (FK/PK)
   - ✓ Índices (seletividade, desempenho)
   - ✓ LIMIT/OFFSET (funcionamento)

3. **Analítica e BI**
   - ✓ Data Warehouse (estrutura)
   - ✓ Modelo Snowflake vs Estrela (normalização)
   - ✓ OLAP (operações: drill, decomposição)
   - ✓ ETL (transformação, limpeza)

4. **Containerização**
   - ✓ Docker (imagens, contêineres)
   - ✓ Orquestração básica

---

### **Médios Riscos (Possível)**

- NoSQL e modelos alternativos
- Elasticsearch/ELK Stack
- MapReduce e Big Data
- Data Lake
- Computação em Nuvem (modelos)

---

### **Baixos Riscos (Improvável)**

- Detalhes específicos de configuração
- Sintaxe exata de comandos
- Comparações muito técnicas entre produtos

---

## 📋 QUESTÕES ESPERADAS PARA TCU 2025

### **Tipo 1: Falsidades por Absolutismo**
```
"O uso de [ferramenta X] garante proteção completa contra [ameaça Y]."
Resposta: FALSO (adicione sempre "limitações")
```

### **Tipo 2: Inversão de Relações**
```
"[Conceito A] é dependente de [Conceito B]"
Resposta: FALSO quando a verdade é o oposto
```

### **Tipo 3: Diferenciação de Conceitos**
```
"[Conceito A] = [Conceito B]"
Resposta: FALSO quando há diferença sutil
```

### **Tipo 4: Caracterização Técnica**
```
"A função de [ferramenta] é [descrição precisa]"
Resposta: VERDADEIRO se exata, FALSO se incompleta
```

---

## 🛠️ TEMAS ESPECÍFICOS A ESTUDAR

### **CRÍTICO (>80% de chance)**
- [ ] Tipos de Backup (total, incremental, diferencial)
- [ ] Firewall vs Antivírus (diferenças)
- [ ] SQL JOIN (INNER, LEFT, RIGHT, FULL)
- [ ] Chave Primária vs Chave Estrangeira
- [ ] Modelo Snowflake vs Modelo Estrela
- [ ] Tabelas DIMENSÃO vs FATO
- [ ] ETL - Extract, Transform, Load
- [ ] OLAP vs OLTP
- [ ] Docker - Imagem vs Contêiner
- [ ] Seletividade de Índices

### **IMPORTANTE (50-70% de chance)**
- [ ] Computação em Nuvem (SaaS, PaaS, IaaS)
- [ ] Intranet vs Internet
- [ ] Criptografia (confidencialidade, integridade)
- [ ] Elasticsearch e Shards
- [ ] MapReduce (processamento paralelo)
- [ ] Data Lake vs Data Warehouse
- [ ] NoSQL - Modelo key/value
- [ ] Docker Compose
- [ ] Redes de contêineres

### **CONTEXTUAL (30-50% de chance)**
- [ ] Windows - Funcionalidades básicas
- [ ] ELK Stack (Elasticsearch, Logstash, Kibana)
- [ ] Integridade Referencial
- [ ] Comandos SQL avançados (LIMIT, OFFSET)
- [ ] Big Data - Conceitos

---

## 💡 ESTRATÉGIA DE ESTUDO

1. **Semana 1:** Memorizar tipos de backup, firewall, antivírus
2. **Semana 2:** Dominar SQL - JOINs, PKs, FKs, Índices
3. **Semana 3:** Aprender Data Warehouse, BI, OLAP
4. **Semana 4:** Docker, Containerização, Orquestração
5. **Semana 5:** Big Data, ETL, Ferramentas
6. **Semana 6:** Revisão com foco em "pegadinhas" (falsidades comuns)

---

## ⚠️ ALERTAS IMPORTANTES

### **Pegadinhas Comuns do CEBRASPE:**
1. Palavra "garante" = Geralmente FALSO
2. Palavra "sempre" ou "nunca" = Geralmente FALSO
3. "Requer" quando é opcional = FALSO
4. Listas incompletas = FALSO
5. Inversão lógica de causa/efeito = FALSO

### **Verificação Rápida:**
- Questão tem absoluto? → Suspeito de ser FALSO
- Questão é precisa e específica? → Provável ser VERDADEIRO
- Questão omite exceção conhecida? → FALSO

---

## 📚 RECURSOS RECOMENDADOS

1. Documentação oficial: Docker, SQL, Elasticsearch
2. NIST/ISO 27000 (segurança)
3. RFC IETF (redes e protocolos)
4. Manuais de OLAP e Data Warehouse
5. Estudar todas as provas CEBRASPE de TCE (2024-2025)
