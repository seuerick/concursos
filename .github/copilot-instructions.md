# Materiais de Estudo para Concursos - Diretrizes para Agentes de IA

## Visão Geral do Projeto
Este repositório contém materiais de estudo para concursos públicos brasileiros, organizados por instituição e ano de exame. É um site de documentação estático com arquivos markdown e um navegador HTML simples.

## Organização de Arquivos
- **Pastas de instituições**: `bacen/`, `pf/`, `tcu/`, `tse/` (Banco Central, Polícia Federal, TCU, TSE)
- **Subpastas**: Por cargo (`auditor/`, `tecnico/`) e ano (`2025/`, `2021/`, etc.)
- **Tipos de arquivos principais**:
  - `edital_*.md`: Editais de exames/notificações
  - `prova_*.md`: Questões e conteúdo de exames
  - `desempenho.md`: Análise de desempenho
  - `*_conteudo.html`: Versões HTML do conteúdo

## Padrões de Conteúdo
- Use seções colapsáveis `<details>` para organização de tópicos (ex.: `<details><summary>PORTUGUÊS</summary>`)
- Estruture exames com numeração hierárquica (1., 1.1, 1.1.1)
- Inclua justificativas para questões de exemplo quando fornecidas
- Mantenha o idioma português em todo o conteúdo

## Adicionando Novos Materiais
1. Crie a estrutura de pastas instituição/ano/cargo se necessário
2. Siga a nomenclatura: `edital_{ano}.md`, `prova_{ano}.md`
3. Use formatação markdown consistente com seções colapsáveis
4. Atualize `index.html` se adicionar novas categorias de nível superior

## Agentes Especializados
- Preparação para exame do TCU usa `.github/agents/TCU.agent.md` para planejamento de estudos coordenado
- Foco em questões estilo Cebraspe Certo/Errado e peças discursivas

## Referências Principais
- [tcu/auditor/2025/edital_2025.md](tcu/auditor/2025/edital_2025.md) - Exemplo completo de estrutura de exame
- [pf/perito_2025.md](pf/perito_2025.md) - Detalhamento de tópicos
- [index.html](index.html) - Integração com API do GitHub para navegação</content>
<parameter name="filePath">/workspaces/concursos/.github/copilot-instructions.md