# Análise da Distribuição dos Gabaritos Cebraspe

> Estudo estatístico dos gabaritos oficiais definitivos de concursos Cebraspe com edital
> compatível com o **CGU 2026 — AFFC Cargo 4 (TI – Desenvolvimento de Sistemas)**.
> Objetivo: identificar padrões na distribuição das respostas para uso como **conferência de
> sanidade** na resolução de provas (não como estratégia de chute).

## 1. Metodologia

- **Fonte:** gabaritos oficiais definitivos (PDF) baixados do CDN da Cebraspe
  (`cdn.cebraspe.org.br/concursos/{ID}/arquivos/`).
- **Amostra C/E (Certo/Errado):** 11 provas · 685 itens válidos
  (TCU 25, DATAPREV 23, BCB 24, CGE RJ 23, TCDF 24).
- **Amostra A–E (múltipla escolha):** 8 provas · ~400 itens
  (TCE PR 24, SEFAZ RN 25, SEFAZ SE 25).
- **Tratamento:** itens anulados (X) excluídos das contagens de distribuição.

## 2. Distribuição Geral — Formato Certo/Errado

| Métrica | Valor |
|---|---|
| **Certo** | 336 (49,1%) |
| **Errado** | 349 (50,9%) |
| Faixa de %C por prova | 45,8% a 52,9% |
| Maior sequência de mesma resposta | 3 a 5 itens |

**Conclusão:** o gabarito C/E é **deliberadamente equilibrado** (~50/50). Nenhuma prova
ultrapassou 53% de um mesmo gabarito.

## 3. Distribuição por Disciplina

| Tipo de disciplina | Itens | %Certo |
|---|---|---|
| Conhecimentos Básicos | 185 | 48,0% |
| Conhecimentos Gerais | 97 | 48,5% |
| Conhecimentos Específicos | 158 | 49,4% |
| Especializados (P3) | 65 | 46,8% |

**Conclusão:** o equilíbrio ~50/50 se mantém **independentemente da disciplina** — não há
disciplina "mais certa" ou "mais errada".

## 4. Posição do Item

Comparação 1ª metade × 2ª metade de cada prova: variação de 44% a 57% de C, **sem viés
consistente** de posição. Exemplo (TCU 25 Básicos, blocos de 20 itens):

| Bloco | C | E |
|---|---|---|
| 1–20 | 10 | 10 |
| 21–40 | 10 | 10 |
| 41–60 | 8 | 11 |
| 61–80 | 9 | 9 |
| 81–100 | 10 | 10 |

**Conclusão:** o balanceamento é aplicado **por bloco**, não apenas no total da prova.

## 5. Transições — Padrão de Alternância (achado principal)

Probabilidade do item seguinte, dado o item atual (C/E):

| Item atual | Próximo C | Próximo E |
|---|---|---|
| **C** | 40% | **60%** |
| **E** | **58%** | 42% |

- **Taxa de alternância: 59,1%** (vs. 50% esperado ao acaso).
- **Significância:** z = 4,8 (erro padrão 1,91%) → **estatisticamente significativo**.
- **Sequências máximas:** 3 a 5 itens iguais seguidos (nunca mais que 5).

**Conclusão:** a Cebraspe **evita sequências longas e tende a alternar** C/E. Após um item
Certo, o próximo tende a ser Errado (60%); após Errado, tende a ser Certo (58%).

## 6. Itens Anulados (X)

- Distribuídos de forma **dispersa**, sem padrão posicional.
- Concentração maior em provas de Conhecimentos Específicos (ex.: TCU 25 Específicos com 12
  anulados em 100 itens).
- **Implicação:** ao conferir, itens anulados não contam — verifique sempre o gabarito
  definitivo (não o preliminar).

## 7. Formato Múltipla Escolha (A–E)

| Letra | A | B | C | D | E |
|---|---|---|---|---|---|
| % | 16,3% | 19,8% | 18,8% | 22,1% | 23,1% |

- Leve viés para **D/E** (22–23%) e menor presença de **A** (16%).
- **Transições:** troca de letra em 80,3% — compatível com o esperado ao acaso (4/5 = 80%),
  ou seja, **sem padrão de alternância** no formato A–E.

## 8. Conclusões e Implicações para o CGU 2026

1. **Gabarito equilibrado:** espere ~50% C e ~50% E no total e por bloco de ~20 itens.
2. **Sem sequências longas:** se você marcou 4+ respostas iguais seguidas, revise — há alta
   chance de erro.
3. **Alternância:** após um C, o próximo tende a E (60%); após E, tende a C (58%). Use como
   conferência, não como regra.
4. **⚠️ Penalização:** o CGU 2026 desconta erros (P1/P2: −1; P3: −2). **Chutar com base no
   padrão é matematicamente desvantajoso.** O padrão serve apenas para **revisar** respostas
   já marcadas com base no conhecimento.
5. **Gabarito definitivo:** sempre confira o gabarito definitivo (itens anulados são comuns em
   provas específicas).

> **Uso recomendado:** após resolver uma prova, confira se sua distribuição de C/E está
> próxima de 50/50 e se não há sequências longas — desvios grandes indicam erros prováveis
> em itens que você marcou "no chute" ou por padrão.

---

## Aprofundamento por disciplina

A análise por **disciplina/tópico** (TCE RN 2025 Cargo 4 e DATAPREV 2023 Cargo 7) e a
comparação com o conteúdo programático do CGU 2026 Cargo 4 estão em
[`analise_disciplinas.md`](analise_disciplinas.md).

---

## Padrões léxicos: palavras e frases que tendem a Certo/Errado

> **Pergunta**: existe padrão de palavra/frase/trecho de enunciado que tende a C ou E?
> **Fonte**: 133 itens com resposta C/E (70 C, 63 E) das provas TCE RN 2025 Cargo 4 e
> DATAPREV 2023 Cargo 7 (itens 51–120), extraídos dos PDFs oficiais e cruzados com os
> gabaritos definitivos.

### 1. Resultado principal

A Cebraspe segue o padrão clássico de bancas C/E:

- **Enunciados "hedged" (possibilidade/ressalva) → tendem a CERTA (C)**.
- **Enunciados absolutos/universais (garantia/totalidade) → tendem a ERRADA (E)**.

O mecanismo é lógico: afirmações absolutas são fáceis de falsificar (basta um
contraexemplo), então a banca as usa em itens **E**; afirmações com ressalva são difíceis
de falsificar, então aparecem em itens **C**.

### 2. Tabela de padrões (n ≥ 5, ordenado por força)

| Padrão | Exemplo de palavra/frase | C | E | n | % C | Consistência |
|---|---|---|---|---|---|---|
| **Possibilidade** | **pode, podem** | 12 | 2 | 14 | **86%** | ✅ TCE RN 78% / DATAPREV 100% |
| **Modalização** | pode, geralmente, tende a, em geral, em regra | 12 | 3 | 15 | **80%** | ✅ 70% / 100% |
| **Possibilidade (frase)** | pode ser, é possível, permite, possibilita | 10 | 4 | 14 | **71%** | ✅ 67% / 100% |
| **Universal** | **qualquer** | 1 | 4 | 5 | **20%** | ✅ 25% / 0% |
| **Garantia** | **garante, assegura** | 2 | 3 | 5 | **40%** | ✅ direcional |
| **Universal (grupo)** | sempre, nunca, todo(s), toda(s), nenhum(a) | 4 | 8 | 12 | **33%** | ⚠️ inconsistente por prova |
| **Obrigação** | deve, devem | 10 | 9 | 19 | 53% | neutro |

### 3. Padrões com amostra pequena (n < 5, apenas direcionais)

| Padrão | C | E | n | % C |
|---|---|---|---|---|
| **desde que** (condição) | 0 | 3 | 3 | 0% |
| **exceto / salvo** | 0 | 2 | 2 | 0% |
| **somente / apenas / exclusivamente** | 1 | 2 | 3 | 33% |
| **não deve(m)** | 0 | 1 | 1 | 0% |
| **dispensa / elimina** | 0 | 2 | 2 | 0% |

### 4. O que NÃO é preditivo

- **"não" isolado**: 53% C (n=15) — negação sozinha não prediz nada.
- **"deve(m)"**: 53% C (n=19) — neutro.
- **"sem"**: 60% C (n=5) — fraco.

### 5. Exemplos reais

<details><summary>Expandir exemplos</summary>

**"pode" → C (86%):**
- TCE RN 4 #62 (C): "A execução de comandos DML, como UPDATE e DELETE, sem cláusula WHERE
  **pode resultar** em operações em massa que afetam toda a tabela..."
- TCE RN 4 #74 (C): "Sob o mesmo namespace, diversos contêineres Docker **podem ser**
  executados e interagir entre si..."

**"qualquer" → E (20%):**
- TCE RN 4 #58 (E): "A utilização de índices compostos garante melhoria uniforme de
  desempenho para **qualquer** consulta que envolva pelo menos uma das colunas indexadas..."
- TCE RN 4 #59 (E): "O particionamento de tabelas elimina a necessidade de índices
  secundários, pois a divisão física dos dados já garante acesso eficiente em **qualquer**
  situação..."

**"garante" → E (40%):**
- TCE RN 4 #60 (E): "...a definição de restrições de chave estrangeira **garante** que
  operações de inserção e de atualização ocorram com melhor desempenho..."
- TCE RN 4 #61 (C): "A integridade referencial **garante** que valores de chave estrangeira
  em uma tabela correspondam a valores válidos de chave primária..." (definição correta)

**"desde que" → E (0%, n=3):**
- TCE RN 4 #120 (E): "...serão admitidas condições decorrentes de acordos internacionais
  **desde que** aprovadas..." (condição restritiva falsa)

</details>

### 6. Como usar (e como NÃO usar)

1. **Use como heurística de leitura crítica**: ao ver "qualquer", "sempre", "nunca",
   "todo", "garante", "única forma", desconfie — procure o contraexemplo (tende a E). Ao
   ver "pode", "é possível", "permite", "geralmente", "tende a", a afirmação costuma ser
   defensável (tende a C).
2. **⚠️ Não use para chutar**: o CGU 2026 desconta erros (P1/P2: −1; P3: −2). Chutar com
   base em padrão é matematicamente desvantajoso. O padrão serve para **revisar** respostas
   já marcadas com base no conhecimento — se você marcou C num item com "qualquer", revise.
3. **Amostra**: 133 itens de 2 provas de TI. Os padrões fortes (pode→C, qualquer→E) são
   consistentes entre as duas provas; os demais são direcionais e precisam de mais dados.
4. **Limitação**: a análise é léxica (palavras), não semântica. Um item com "pode" pode ser
   E se o conteúdo técnico estiver errado (ex.: TCE RN 4 #53, "não podem ser indexados").
   O padrão é um **sinal**, não uma garantia.
