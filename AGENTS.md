# AGENTS.md — Guia de Concursos Cebraspe (Organizadora)

> Documento de referência para agentes de IA que trabalham com materiais de estudo de concursos
> organizados pelo **Cebraspe** (Centro Brasileiro de Pesquisa em Avaliação e Seleção e de Promoção de Eventos),
> antigo Cespe/UnB. Foco no perfil de candidato **desenvolvedor de software**.
> Última atualização: 22/10/2026.

## 1. Sobre a Organizadora (Cebraspe)

- **Nome completo**: Centro Brasileiro de Pesquisa em Avaliação e Seleção e de Promoção de Eventos.
- **Marca histórica**: Cespe/UnB (Universidade de Brasília). O Cebraspe é o detentor exclusivo do **Método Cespe** de avaliação.
- **Site de concursos**: https://www.cebraspe.org.br/concursos/
- **API pública (não documentada, descoberta por engenharia reversa)**:
  - Base: `https://apis.cebraspe.org.br/cebraspe/`
  - Detalhe de um concurso: `GET /eventos/{IDENTIFICADOR}` (ex.: `CGU_26_AFFC`)
  - Lista de concursos em andamento: `GET /eventos/tipo/concursos/fase/em-andamento`
  - Lista de concursos encerrados: `GET /eventos/tipo/concursos/fase/encerrado`
  - Arquivos (editais, comunicados): `https://cdn.cebraspe.org.br/concursos/{IDENTIFICADOR}/arquivos/{nomeArquivo}`
- **Área do candidato**: https://areadocandidato.cebraspe.org.br/

## 2. O Método Cespe (Padrão de Prova)

- **Itens de julgamento "Certo ou Errado" (C/E)**: marcação binária na folha de respostas (campos C e E).
- **Pontuação negativa**: item errado desconta pontos (típico: +1,00 / −1,00 ou +2,00 / −2,00 conforme a prova).
- **Item sem marcação ou com marcação dupla (C e E)**: vale 0,00 ponto.
- **Provas objetivas**: eliminatórias e classificatórias, corrigidas por processamento eletrônico da folha de respostas.
- **Prova discursiva**: texto manuscrito com caneta esferográfica de tinta preta transparente; avalia conteúdo + domínio da modalidade escrita (erros gramaticais descontam pontos via fórmula com NE ÷ TL).
- **Recursos**: interpostos exclusivamente pela Área do Candidato, em janelas curtas (geralmente 2 dias, das 10h às 18h).
- **Gabaritos preliminares**: divulgados à noite (19h) no site do concurso; recursos em seguida.
- **Cronograma típico**: inscrições ~1 mês → provas ~2 meses após o fim das inscrições → resultado final ~4 meses após as provas.

## 3. Estrutura Típica de um Concurso Cebraspe (nível superior)

1. **Edital de abertura** (Edital nº 1) + retificações (Edital nº 2, nº 3...).
2. **Inscrições** com isenção de taxa (período anterior) e pagamento via GRU/PagTesouro (Pix ou cartão).
3. **Provas objetivas** (manhã) e **prova discursiva** (tarde), nas 27 capitais.
4. **Gabaritos preliminares** → recursos → gabaritos definitivos.
5. **Resultado final nas objetivas** → correção das discursivas dos aprovados.
6. **Procedimentos de heteroidentificação** (negros, indígenas, quilombolas) e **caracterização de deficiência** (etapa documental + presencial).
7. **Resultado final** e convocação para posse.

## 4. Reservas de Vagas (padrão federal)

- **PcD**: 5% (Lei 13.146/2015, Decreto 9.508/2018, IN Conjunta MGI/MDHC 260/2025).
- **PP (pretos e pardos)**: percentual conforme Decreto 9.739/2019 (tipicamente 20%).
- **PI (indígenas)** e **PQ (quilombolas)**: conforme Decreto 11.785/2023 (Programa Federal de Ações Afirmativas).
- **Equilíbrio de gênero**: aprovação adicional de mulheres quando o percentual feminino for < 50% (Lei 15.142/2025).

## 5. Concursos Interligados Relevantes para Perfil de Desenvolvedor de Software

Concursos Cebraspe (em andamento ou recentes) com cargos de TI/desenvolvimento — úteis como **fonte de questões e referência de conteúdo**:

| Concurso | Ano | Cargo(s) de TI | Salário máx. | Status |
|---|---|---|---|---|
| **CGU 26 AFFC** | 2026 | AFFC – TI: Ciência de Dados; Infraestrutura de TI; **Desenvolvimento de Sistemas** | R$ 20.000,00 | Em andamento (provas 13/12/2026) |
| **TCU 25 AUFC** | 2025 | Auditor de Controle Externo – Auditoria de TI | R$ 26.159,01 | Em andamento |
| **PF 25** | 2025 | Perito Criminal Federal – Informática Forense | R$ 26.800,00 | Em andamento |
| **SERPRO 23** | 2023 | Analista – Especialização: Tecnologia | R$ 9.025,73 | Encerrado |
| **DATAPREV 23** | 2023 | Analista de TI – Desenvolvimento e Software; Engenheiro de Dados; Segurança Cibernética; etc. | R$ 8.747,61 | Encerrado |
| **TC DF 26 Analista** | 2026 | Analista de Controle Externo (área de gestão) | R$ 14.990,41 | Em andamento |
| **Câmara dos Deputados 26 PLF** | 2026 | Técnico Legislativo – Policial Legislativo | — | Em andamento |

### Observações estratégicas
- **CGU 26 AFFC** é o concurso com o cargo de **Desenvolvimento de Sistemas** mais alinhado ao perfil de engenheiro de software (Java, Spring, Vue.js, SQL, arquitetura, DevSecOps).
- **TCU 25 AUFC** (Auditoria de TI) e **PF 25** (Informática Forense) são concursos interligados com forte conteúdo de TI — boas fontes de questões Cebraspe de tecnologia.
- **SERPRO 23** e **DATAPREV 23** são referências de provas de TI de empresas públicas federais (estilo Cebraspe).
- O conteúdo de **conhecimentos básicos/complementares** (Estado, ética, governança, transparência, direito público) é **comum entre concursos federais Cebraspe** — estudar uma vez serve para vários certames.

## 6. Convenções de Conteúdo (seguir nos materiais)

- Idioma: **português**.
- Seções colapsáveis `<details><summary>...</summary>` para organização de tópicos.
- Numeração hierárquica (1., 1.1, 1.1.1).
- Incluir justificativas para questões de exemplo.
- Nomenclatura de arquivos: `edital_{ano}.md`, `prova_{ano}.md`, `desempenho.md`.
- Estrutura de pastas: `instituicao/cargo/ano/` (ex.: `cgu/auditor/2026/`).
- Atualizar `index.html` ao adicionar categorias de nível superior.

## 7. Fontes de Dados

- Site oficial de concursos: https://www.cebraspe.org.br/concursos/
- API de eventos (detalhe por identificador): `https://apis.cebraspe.org.br/cebraspe/eventos/{ID}`
- CDN de arquivos (editais em PDF/HTML): `https://cdn.cebraspe.org.br/concursos/{ID}/arquivos/{arquivo}`
- Diário Oficial da União (DOU): publicações oficiais de editais e resultados.
