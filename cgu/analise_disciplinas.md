# Análise de Distribuição de Gabaritos por Disciplina

> **Objetivo**: verificar se há padrão na distribuição das respostas (Certo/Errado) por disciplina/tópico nas provas Cebraspe mais similares ao **Cargo 4 (Desenvolvimento de Sistemas) do CGU 2026**, e comparar os tópicos cobrados com o conteúdo programático do edital.

## 1. Metodologia

- **Provas analisadas** (70 itens cada, itens 51–120):
  - **TCE RN 2025 – Cargo 4 (Desenvolvimento de Sistemas)** — prova e gabarito oficiais Cebraspe.
  - **DATAPREV 2023 – Cargo 7 (Desenvolvimento e Software)** — prova e gabarito oficiais Cebraspe.
- **Extração**: `pdftotext` nos PDFs oficiais; itens ordenados por número e respostas cruzadas com o gabarito (C = Certo, E = Errado, X = anulado).
- **Classificação**: cada item foi atribuído a um tópico com base no enunciado, seguindo as frases de tópico das provas.
- **Validação**: os totais por prova conferem com os gabaritos oficiais (TCE RN 4: C=38, E=30, X=2; DATAPREV 7: C=32, E=33, X=5).

## 2. Resultado Geral

| Prova | Itens | C | E | X | % C | % E |
|---|---|---|---|---|---|---|
| TCE RN 2025 – Cargo 4 | 70 | 38 | 30 | 2 | 54,3% | 42,9% |
| DATAPREV 2023 – Cargo 7 | 70 | 32 | 33 | 5 | 45,7% | 47,1% |
| **Combinado** | **140** | **70** | **63** | **7** | **50,0%** | **45,0%** |

- Combinando as duas provas, a distribuição é **~50/50** (C=50,0%, E=45,0%, X=5,0%), consistente com a análise agregada anterior (11 provas, 685 itens: 49,1% C vs 50,9% E).
- Individualmente, há leve viés: TCE RN 4 pende para **C** (54,3%), DATAPREV 7 pende para **E** (47,1% E vs 45,7% C). Amostras pequenas — não é estatisticamente robusto, mas sugere que **não há um viés sistemático de banca**; o equilíbrio é o padrão.

## 3. TCE RN 2025 – Cargo 4: Distribuição por Tópico

<details><summary>Expandir tabela por tópico</summary>

| # | Tópico | Itens | C | E | X | % C |
|---|---|---|---|---|---|---|
| 1 | Bancos de dados, Big Data, NoSQL | 51–62 | 6 | 6 | 0 | 50% |
| 2 | Projetos e processos de software, padrões de projeto | 63–66 | 2 | 2 | 0 | 50% |
| 3 | Práticas ágeis (Kanban, Scrum, INVEST, storytelling) | 67–70 | 2 | 2 | 0 | 50% |
| 4 | Testes e métricas de software, DevOps | 71–74 | 2 | 1 | 1 | 67% |
| 5 | Bancos relacionais, modelagem dimensional | 75–76 | 1 | 1 | 0 | 50% |
| 6 | Pré-processamento de dados, CRISP-DM, mineração | 77–85 | 5 | 4 | 0 | 56% |
| 7 | Ferramentas de apoio à análise de dados (Python/R/planilhas) | 86–89 | 3 | 1 | 0 | **75%** |
| 8 | MLOps, IA generativa, deep learning, viés | 90–96 | 4 | 3 | 0 | 57% |
| 9 | Padrões arquiteturais e padrões de projeto | 97–100 | 2 | 2 | 0 | 50% |
| 10 | Integração de sistemas, serviços web | 101–103 | 2 | 1 | 0 | 67% |
| 11 | COBIT 2019, ISO 31000, COSO, ITIL v4 | 104–106 | 2 | 1 | 0 | 67% |
| 12 | SCRUM, PMBOK 7, PDTIC | 107–110 | 2 | 1 | 1 | 67% |
| 13 | Cibersegurança, LGPD, DAMA-DMBoK | 111–113 | 2 | 1 | 0 | 67% |
| 14 | Gestão de contratação de soluções de TI | 114–120 | 3 | 4 | 0 | 43% |

</details>

**Leitura**: a maioria dos tópicos fica em ~50/50. Desvios observados (amostras de 2–7 itens, apenas direcionais):
- **Mais C**: ferramentas de análise de dados (75%), integração/serviços web, COBIT/ISO/COSO/ITIL, cibersegurança/LGPD (67%).
- **Mais E**: contratação de TI (43% C) — tópico com itens de "pegadinha" sobre procedimentos de licitação/fiscalização.

## 4. DATAPREV 2023 – Cargo 7: Distribuição por Tópico

<details><summary>Expandir tabela por tópico</summary>

| # | Tópico | Itens | C | E | X | % C |
|---|---|---|---|---|---|---|
| 1 | JavaScript, Web Services, análise estática | 51–54 | 2 | 2 | 0 | 50% |
| 2 | Intranet/extranet, UDDI, XSLT, DevOps | 55–58 | 3 | 1 | 0 | **75%** |
| 3 | Testes ágeis, pontos de função, Scrum, Kanban, reuso | 59–63 | 2 | 2 | 1 | 50% |
| 4 | Engenharia de requisitos, CSS, PWA, HTTPS | 64–68 | 2 | 2 | 1 | 50% |
| 5 | Blockchain, IA, arquitetura hexagonal, usabilidade, CMS | 69–73 | 1 | 4 | 0 | **20%** |
| 6 | Segurança da informação (acessos, chaves, criptografia, física) | 74–80 | 4 | 3 | 0 | 57% |
| 7 | Ciclo de vida de desenvolvimento seguro (SDL) | 81–84 | 1 | 3 | 0 | **25%** |
| 8 | Análise estática e dinâmica de código | 85–88 | 2 | 1 | 1 | 67% |
| 9 | OWASP Top 10 | 89–91 | 1 | 1 | 1 | 50% |
| 10 | POSIN (Política de Segurança da Informação) | 92–93 | 1 | 1 | 0 | 50% |
| 11 | MongoDB, MER, modelagem de dados | 94–97 | 2 | 2 | 0 | 50% |
| 12 | SQL (DCL, DDL, normalização, VIEW, SELECT, UNION) | 98–105 | 4 | 4 | 0 | 50% |
| 13 | BI, Big Data | 106–107 | 1 | 1 | 0 | 50% |
| 14 | Gerenciamento de projetos (EAP, portfólio, ciclos de vida) | 108–110 | 1 | 1 | 1 | 50% |
| 15 | Scrum | 111–112 | 1 | 1 | 0 | 50% |
| 16 | Gestão de riscos | 113–114 | 1 | 1 | 0 | 50% |
| 17 | ITIL v4 / COBIT | 115–118 | 2 | 2 | 0 | 50% |
| 18 | BPMN | 119–120 | 1 | 1 | 0 | 50% |

</details>

**Leitura**: padrão ainda mais equilibrado — 15 dos 18 tópicos em exatamente 50/50. Desvios:
- **Mais C**: intranet/extranet/UDDI/XSLT/DevOps (75%).
- **Mais E**: blockchain/IA/arquitetura hexagonal (20% C) e **ciclo de vida de desenvolvimento seguro – SDL (25% C)**.

> **Padrão relevante**: nos tópicos de **segurança** (SDL, blockchain, arquitetura), a Cebraspe tende a descrever uma **prática incorreta como se fosse correta** — o item vira **E**. Em tópicos de **conceitos de infraestrutura/ferramentas** (intranet, UDDI, XSLT, DevOps), a tendência é **C**. Isso é direcional (amostras pequenas), mas útil para leitura crítica de enunciados.

## 5. Comparação com o Conteúdo Programático do CGU 2026 – Cargo 4

<details><summary>Expandir mapa de sobreposição</summary>

### 5.1 Tópicos do CGU 2026 cobertos pelas provas analisadas

| Bloco do edital CGU 2026 | Coberto por TCE RN 4 | Coberto por DATAPREV 7 |
|---|---|---|
| Engenharia de software e programação (requisitos, testes, padrões de projeto) | ✅ (63–66, 71–74) | ✅ (59–68) |
| Arquitetura e integração (padrões arquiteturais, serviços web) | ✅ (97–103) | ✅ (53, 70) |
| Persistência de dados (SQL, modelagem, NoSQL) | ✅ (51–62, 75–76) | ✅ (94–107) |
| Desenvolvimento seguro (segurança de apps, OWASP, SDL) | ✅ (111–113) | ✅ (74–93) |
| Gestão da entrega (Scrum, Kanban, PMBOK, COBIT, ITIL) | ✅ (67–70, 104–110) | ✅ (108–118) |
| Contratação e fiscalização de soluções de TI | ✅ (114–120) | ❌ |
| Integração com dados e IA (MLOps, IA generativa) | ✅ (90–96) | ❌ |
| Análise de dados (CRISP-DM, ferramentas, BI) | ✅ (77–89) | ✅ (106–107) |

### 5.2 Lacunas — tópicos do CGU 2026 **não** cobertos pelas provas analisadas

| Tópico do edital CGU 2026 | Observação |
|---|---|
| **Java, Spring Framework, Spring Boot, JPA, Spring Data** | ❌ Nenhuma das duas provas cobriu o stack Java/Spring — o coração do edital CGU 2026 |
| **OAuth 2.0, OpenID Connect, Spring Security, tokens** | ❌ Não cobrido |
| **Microsserviços, arquitetura orientada a eventos, mensageria** | ❌ Não cobrido (TCE RN 4 tocou arquitetura, mas não eventos/mensageria) |
| **Cloud, contêineres, serverless, observabilidade** | ❌ Não cobrido |
| **RAG, busca semântica, agentes, proteção contra prompt injection** | ⚠️ TCE RN 4 cobriu IA generativa/MLOps, mas não RAG/agentes |
| **ETL/ELT, Spring Batch, formatos Parquet** | ❌ Não cobrido |
| **Vue.js, JavaScript moderno (componentes, reatividade)** | ⚠️ DATAPREV 7 cobriu JavaScript básico, não Vue.js |
| **BPMN** | ⚠️ DATAPREV 7 cobriu BPMN; CGU 2026 não o menciona explicitamente |

</details>

## 6. Conclusões e Implicações para a Estratégia de Estudo

1. **Equilíbrio C/E é o padrão da Cebraspe** — em 140 itens de cargos de TI, 50% C vs 45% E. Não há viés sistemático de banca; a distribuição é controlada por bloco. **Não aposte em "chutar tudo C" ou "tudo E"** — o gabarito é balanceado.

2. **Padrão por tópico (direcional)**:
   - Tópicos de **segurança/arquitetura** tendem a **E** (enunciado descreve prática errada como correta).
   - Tópicos de **conceitos de ferramentas/infraestrutura** tendem a **C**.
   - Use isso como **heurística de leitura**, não como regra de chute.

3. **As provas Cebraspe de cargos similares NÃO cobrem o stack Java/Spring** — o edital CGU 2026 Cargo 4 é fortemente orientado a **Java, Spring Boot, JPA, Spring Data, OAuth/OIDC, microsserviços, cloud e RAG**. Esses tópicos não aparecem nas provas anteriores da Cebraspe para cargos de desenvolvimento. **Consequência**: para esses tópicos, o treino com provas Cebraspe não é suficiente — é preciso estudar o conteúdo teórico e treinar com provas de outras bancas (FGV, FCC, CESGRANRIO) ou questões específicas de Java/Spring.

4. **Tópicos com maior sobreposição** (onde provas Cebraspe ajudam a treinar): SQL/modelagem, testes/qualidade, padrões de projeto, Scrum/Kanban/PMBOK, COBIT/ITIL, segurança da informação, contratação de TI, análise de dados/IA.

5. **Recomendação prática**: priorize o estudo dos tópicos exclusivos do CGU 2026 (Java/Spring, OAuth, microsserviços, cloud, RAG) com material teórico + questões de outras bancas, e use as provas Cebraspe de TCE RN 4 e DATAPREV 7 como treino de leitura crítica e gestão de tempo nos tópicos sobrepostos.

## 7. Arquivos de Origem

- `cgu/analise_gabaritos.md` — análise estatística agregada (11 provas, 685 itens).
- `cgu/provas_anteriores.md` — curadoria de concursos Cebraspe com edital compatível.
- `cgu/edital_2026.md` — conteúdo programático completo do Cargo 4.
- PDFs oficiais: TCE RN 2025 (Cargo 4) e DATAPREV 2023 (Cargo 7), baixados do CDN da Cebraspe.
