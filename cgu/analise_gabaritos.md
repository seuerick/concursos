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
