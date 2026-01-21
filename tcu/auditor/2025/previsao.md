# 🛡️ RECUPERAÇÃO DE DESASTRES (DR) - TCU 2025

---

## ✅ 1. Alta Disponibilidade e Recuperação de Desastres (DR)

### 📝 Questão 1 – CEBRASPE 2024 – TCE-AC – Analista de TI

> "Mediante um plano de recuperação de desastres, deve-se buscar eliminar qualquer possibilidade de desastre ou perda de dados provocados por incidentes de segurança nos serviços de TI de uma instituição."

| Aspecto | Detalhe |
|---------|---------|
| **Ponto Cobrado** | Diferença entre eliminação de riscos × mitigação |
| **Gabarito** | ❌ **ERRADO** |
| **Explicação** | Planos de DR não eliminam desastres; reduzem impactos e recuperam dentro de RTO/RPO aceitáveis |
| **Fonte** | tecconcursos.com.br |

---

### 📝 Questão 2 – CEBRASPE 2025 – EMBRAPA – Analista de TI

> "Uma estratégia abrangente de recuperação de desastres deve incluir a métrica objetivo do ponto de recuperação (RPO), que corresponde ao período máximo aceitável em que os sistemas podem permanecer indisponíveis."

| Aspecto | Detalhe |
|---------|---------|
| **Ponto Cobrado** | Confusão proposital entre **RPO × RTO** |
| **Gabarito** | ❌ **ERRADO** |
| **Diferenciação** | • **RPO** → quantidade de dados que pode ser perdida<br/>• **RTO** → tempo máximo de indisponibilidade |
| **Fonte** | estudegratis.com.br |

---

## ✅ 2. Clusters de Alta Disponibilidade e Balanceamento de Carga

### 📝 Questão 3 – CEBRASPE 2025 – BDMG – Infraestrutura e Segurança

> "Em ambientes de alta disponibilidade, o uso de clusters elimina completamente a necessidade de balanceadores de carga externos."

| Aspecto | Detalhe |
|---------|---------|
| **Ponto Cobrado** | Complementaridade entre cluster e load balancer |
| **Gabarito** | ❌ **ERRADO** |
| **Diferenciação** | • **Clusters** → resiliência interna<br/>• **Load Balancers** → distribuição de requisições e health checks |
| **Fonte** | estudegratis.com.br |

---

### 📝 Questão 4 – CEBRASPE 2023/2024 – Bancas Recorrentes

> "Em um cluster ativo-ativo, todos os nós processam cargas simultaneamente, o que aumenta desempenho e tolerância a falhas."

| Aspecto | Detalhe |
|---------|---------|
| **Ponto Cobrado** | Diferença entre **ativo-ativo × ativo-passivo** |
| **Gabarito** | ✅ **CERTO** |
| **Fonte** | unirios.edu.br |

---

## ✅ 3. Failover, Heartbeat e Fencing

### 📝 Questão 5 – CEBRASPE 2023/2024 – Infraestrutura

> "Heartbeat é o mecanismo utilizado em clusters para detecção de falhas entre nós, permitindo a execução automática de failover."

| Aspecto | Detalhe |
|---------|---------|
| **Ponto Cobrado** | Correlação: **heartbeat → detecção de falha → failover** |
| **Gabarito** | ✅ **CERTO** |
| **Fonte** | learn.microsoft.com |

---

### 📝 Questão 6 – CEBRASPE 2024/2025 – Estilo Típico

> "O mecanismo de fencing garante que um nó com falha seja isolado, evitando corrupção de dados em ambientes com armazenamento compartilhado."

| Aspecto | Detalhe |
|---------|---------|
| **Gabarito** | ✅ **CERTO** |
| **Essência da Cobrança** | • **Split-brain** (evita)<br/>• **Integridade de dados**<br/>• **Isolamento físico/lógico** do nó defeituoso |
| **Fonte** | learn.microsoft.com |

---

## ✅ 4. Plano de Continuidade de Negócios (PCN/BCP) e Testes de DR

### 📝 Questão 7 – CEBRASPE 2022 – APEX Brasil

> "O plano de continuidade de negócios deve passar por manutenção periódica e ser atualizado em função de mudanças no negócio, legislação e infraestrutura de TI."

| Aspecto | Detalhe |
|---------|---------|
| **Ponto Cobrado** | Ciclo PDCA da continuidade: planejar → testar → manter → revisar |
| **Gabarito** | ✅ **CERTO** |
| **Fonte** | tecconcursos.com.br |

---

### 📝 Questão 8 – CEBRASPE 2024 – APEX / Segurança da Informação

> "Os testes do plano de continuidade de negócios devem garantir que apenas uma fração da equipe conheça seus procedimentos, a fim de preservar sigilo."

| Aspecto | Detalhe |
|---------|---------|
| **Gabarito** | ❌ **ERRADO** |
| **Motivo** | Conhecimento amplo e treinamento são **essenciais** para resposta efetiva |
| **Aprendizado** | CEBRASPE valoriza equipes bem-treinadas |
| **Fonte** | qconcursos.com |

---

### 📝 Questão 9 – CEBRASPE 2025 – FUNPRESP-EXE

> "Os testes de recuperação de desastres permitem validar RTO, RPO, procedimentos e capacidade real de resposta organizacional."

| Aspecto | Detalhe |
|---------|---------|
| **Gabarito** | ✅ **CERTO** |
| **Fonte** | estudegratis.com.br |

---

## 🎯 Como o CEBRASPE Costuma Cobrar

### 📊 Pegadinhas de Alta Recorrência

```
❌ Pegadinhas clássicas:
  • Pegadinhas RTO × RPO (MUITO COBRADO!)
  • Confusão entre HA ≠ DR
  • Clusters não eliminam falhas, apenas reduzem impacto
  • Papel do fencing (SUPER IMPORTANTE!)
  • Testes são opcionais (FALSO - são obrigatórios!)
```

---

## 📚 DR, DRP, RPO e RTO - DEFINIÇÕES CLARAS

### 🔹 DR – Disaster Recovery (Recuperação de Desastres)

**O que é:**
Conjunto de estratégias, práticas e recursos usados para restaurar sistemas de TI após um desastre.

👉 **É o conceito, a capacidade de recuperar.**

**Exemplos de desastre:**
- ❌ Falha grave de servidor ou storage
- ❌ Ataque de ransomware
- ❌ Incêndio no data center
- ❌ Falha elétrica prolongada

> 📌 **IMPORTANTE PARA PROVA:** DR ≠ Backup. Backup é uma ferramenta dentro do DR.

---

### 🔹 DRP – Disaster Recovery Plan (Plano de Recuperação de Desastres)

**O que é:**
Documento/plano formal que descreve como o DR será executado.

👉 **É o plano escrito, operacional.**

**O DRP costuma conter:**
- ✓ Procedimentos de restauração
- ✓ Responsáveis e equipes
- ✓ Prioridade dos sistemas
- ✓ Locais alternativos (site backup)
- ✓ Valores de RTO e RPO
- ✓ Procedimentos de teste

> 📌 **DIFERENÇA-CHAVE DO CEBRASPE:**
> - **DR** = capacidade/estratégia
> - **DRP** = plano documentado

> 🔴 **DICA:** Se falar em documento, procedimentos, roteiros → pense em **DRP**

---

### 🔹 RTO – Recovery Time Objective (Tempo ⏱️)

**O que é:**
Tempo máximo aceitável para que um sistema fique fora do ar após um desastre.

👉 **Mede TEMPO de indisponibilidade.**

**Exemplo prático:**
```
RTO = 4 horas
✅ O sistema pode ficar fora do ar por até 4 horas (no máximo)
```

> 📌 **REGRA DE OURO:** RTO = **T**empo

---

### 🔹 RPO – Recovery Point Objective (Dados 💾)

**O que é:**
Quanto de dados pode ser perdido, medido em tempo entre o último backup e o desastre.

👉 **Mede PERDA DE DADOS aceitável.**

**Exemplo prático:**
```
RPO = 30 minutos
✅ A empresa aceita perder até 30 minutos de dados
```

> 📌 **REGRA DE OURO:** RPO = **Ponto** de dados

---

## 📋 Tabela Comparativa (Estilo Prova)

| Sigla | É o quê? | Mede | Palavra-chave |
|-------|----------|------|---------------|
| **DR** | Capacidade de recuperação | — | Estratégia |
| **DRP** | Plano documentado | — | Procedimentos |
| **RTO** | Tempo máximo para restauração | Tempo ⏱️ | Indisponibilidade |
| **RPO** | Perda máxima de dados aceitável | Dados 💾 | Backup |

---

## 🚨 Pegadinhas Clássicas do CEBRASPE

### ❌ FALSAS (Errado)

```
❌ "O RPO define o tempo máximo de indisponibilidade do sistema."
   ➡️ ERRADO (isso é RTO)

❌ "O DRP elimina a possibilidade de desastres."
   ➡️ ERRADO (ele mitiga impactos, não elimina)

❌ "Clusters eliminam completamente a necessidade de backup."
   ➡️ ERRADO (backup é essencial mesmo com HA)

❌ "O fencing é opcional em ambientes com armazenamento compartilhado."
   ➡️ ERRADO (é crítico para evitar split-brain)
```

---

### ✅ VERDADEIRAS (Certo)

```
✅ "O DRP deve ser testado e atualizado periodicamente."
   ➡️ CERTO (ciclo PDCA contínuo)

✅ "RTO e RPO são métricas fundamentais de recuperação de desastres."
   ➡️ CERTO (sempre aparecem juntas)

✅ "O heartbeat permite detecção automática de falhas em clusters."
   ➡️ CERTO (função específica do heartbeat)

✅ "Todos os membros da equipe devem conhecer os procedimentos de DR."
   ➡️ CERTO (treinamento amplo é essencial)
```

---

## 🧠 Dicas de Memorização Rápida

```
T  O  = Tempo    → RTO  ⏱️
P  O  = Ponto    → RPO  📊

Heartbeat → Detecção → Failover → Isolamento (Fencing)
            🫀         🔄         🚪

DR = Estratégia
DRP = Documento (Plan)
```

---

## 📌 Resumo Executivo para Prova

| Conceito | Lembre-se de | Pegadinha |
|----------|--------------|-----------|
| **DR** | Conjunto de estratégias | ≠ Backup |
| **DRP** | Plano documentado e testado | Deve ser atualizado sempre |
| **RTO** | Tempo máximo **indisponível** | ≠ RPO |
| **RPO** | Dados que **podem ser perdidos** | ≠ RTO |
| **Failover** | Comutação automática | Precisa de heartbeat + fencing |
| **Fencing** | Isolamento do nó defeituoso | Previne split-brain |
