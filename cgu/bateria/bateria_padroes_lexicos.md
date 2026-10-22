# Bateria de Questões — Padrões Léxicos C/E (Cebraspe)

> **Objetivo:** testar se você internalizou os padrões léxicos de enunciados que tendem a **Certo** ou **Errado**, identificados na análise léxica (`cgu/analise_gabaritos.md`).
> **Fonte:** itens reais de **TCE/RN 2025 (Cargo 4)** e **DATAPREV 2023 (Cargo 7)** — concursos Cebraspe com edital compatível com o CGU 2026 (Cargo 4).
> **Como usar:** julgue cada item **C** ou **E** ANTES de abrir a resposta. Depois compare com o gabarito e leia a explicação do padrão aplicado.

---

## Como pontuar

- **Acertou e o padrão previa** → você entendeu o padrão. ✅
- **Acertou mas o padrão previa o contrário** → o padrão é heurística, não regra; o conteúdo técnico manda. ⚠️
- **Errou** → revise o padrão e o conteúdo. ❌

**Meta:** 4/5 (80%) ou mais. Abaixo disso, refaça a bateria após revisar a cola rápida.

---

## Cola rápida (resumo dos padrões)

| Padrão no enunciado | Tendência | Mecanismo |
|---|---|---|
| "pode(m)", "geralmente", "tende a", "em geral", "em regra" | **C** (~80–86%) | ressalva → afirmação defensável |
| "pode ser", "é possível", "permite" | **C** (~71%) | possibilidade → defensável |
| "sempre", "nunca", "todo", "nenhum", "qualquer" | **E** (~20–33% C) | absoluto → fácil de falsificar |
| "garante", "assegura" | **E** (~40% C) | promessa forte → fácil de falsificar |
| "desde que" (condição restritiva) | **E** (0%, n=3) | condição que limita a validade |
| "deve(m)" | neutro (~53%) | depende do conteúdo |
| Inversão de conceito/papel (troca A↔B) | **E** | pegadinha clássica |

> ⚠️ **Atenção:** o padrão é um **sinal de alerta**, não uma resposta automática. Itens com definições corretas e sem absolutos tendem a **C**, mesmo sem palavra-chave. Sempre valide pelo conteúdo.

---

## Bateria inicial (5 questões)

### Questão 1
**Enunciado:** Dados estruturados são organizados segundo um esquema rígido previamente definido, enquanto dados não estruturados não possuem modelo predefinido, sendo tipicamente armazenados em formatos como textos livres, imagens e vídeos.

**Sua resposta:** C / E

<details><summary>Gabarito e explicação</summary>

**Gabarito: C**

**Padrão aplicado:** definição correta, sem absoluto ("tipicamente") → tende a **C**.

**Justificativa técnica:** a distinção entre dados estruturados (esquema rígido) e não estruturados (sem modelo predefinido) está correta.

</details>

### Questão 2
**Enunciado:** A mitigação de viés em modelos de IA pode envolver técnicas como balanceamento de dados, regularização e avaliação de métricas de equidade.

**Sua resposta:** C / E

<details><summary>Gabarito e explicação</summary>

**Gabarito: C**

**Padrão aplicado:** "pode envolver" → modalização/possibilidade → tende a **C** (padrão mais forte: ~80–86%).

**Justificativa técnica:** a afirmação é defensável — essas são, de fato, técnicas usadas para mitigar viés.

</details>

### Questão 3
**Enunciado:** A utilização de índices compostos garante melhoria uniforme de desempenho para qualquer consulta que envolva pelo menos uma das colunas indexadas, independentemente da ordem dos atributos no índice.

**Sua resposta:** C / E

<details><summary>Gabarito e explicação</summary>

**Gabarito: E**

**Padrão aplicado:** "garante... qualquer... independentemente" → absoluto triplo → tende a **E**.

**Justificativa técnica:** índices compostos seguem o princípio do prefixo mais à esquerda (leftmost prefix); a ordem das colunas importa e o ganho não é uniforme para qualquer consulta.

</details>

### Questão 4
**Enunciado:** Enquanto o foco do processo incremental é aprimorar o que já foi entregue, o objetivo do processo iterativo é entregar nova funcionalidade.

**Sua resposta:** C / E

<details><summary>Gabarito e explicação</summary>

**Gabarito: E**

**Padrão aplicado:** inversão de conceito (troca A↔B) → tende a **E**.

**Justificativa técnica:** está invertido. O processo **iterativo** refina/aprimora o que já foi entregue; o **incremental** agrega nova funcionalidade.

</details>

### Questão 5
**Enunciado:** Para garantir uma correta compilação de um código escrito em JavaScript, é necessário que as variáveis sejam definidas e inicializadas antes de seu uso no código.

**Sua resposta:** C / E

<details><summary>Gabarito e explicação</summary>

**Gabarito: E**

**Padrão aplicado:** "necessário que... antes" → absoluto → tende a **E**.

**Justificativa técnica:** JavaScript é interpretado/JIT (não "compilado" nesse sentido) e possui **hoisting** — variáveis podem ser usadas antes da declaração (com `var`), sem erro de compilação.

</details>

---

## Gabarito consolidado

| # | Prova | Item | Gabarito | Padrão-chave |
|---|-------|------|----------|--------------|
| 1 | TCE/RN | 52 | C | definição correta, sem absoluto |
| 2 | TCE/RN | 95 | C | "pode envolver" (modalização) |
| 3 | TCE/RN | 58 | E | "garante... qualquer... independentemente" (absoluto) |
| 4 | TCE/RN | 64 | E | inversão de conceito |
| 5 | DATAPREV | 51 | E | "necessário que... antes" (absoluto) |

**Resultado: 2 C / 3 E**

---

## Análise do seu desempenho

- **Acertou a Q2 ("pode envolver" → C)?** → entendeu a modalização (padrão mais forte).
- **Acertou Q3 e Q5 (absolutos → E)?** → entendeu o gatilho de absoluto.
- **Acertou a Q4 (inversão → E)?** → entendeu a pegadinha clássica.
- **Errou a Q1 (C sem palavra-chave)?** → lembre: definição correta e sem absoluto também aponta para C.

> **Próximo passo sugerido:** refaça a bateria em 48h para fixar. Depois, monte um simulado completo com os itens persistidos em `cgu/bateria/prova_tce_rn_2025_cargo4.md` e `cgu/bateria/prova_dataprev_2023_cargo7.md`.
