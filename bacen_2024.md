# Título do Documento

## Conteúdo do Accordion

<details>
  <summary>FUNDAMENTOS DE MACROECONOMIA E MICROECONOMIA (30): I MACROECONOMIA:</summary>
  <br>

  1. Contas nacionais
  2. Agregados monetários
  3. Multiplicador monetário, criação e destruição de moeda
  4. Contas do sistema monetário
  5. Balanço de pagamentos

</details>

<details>
  <summary>II MICROECONOMIA:</summary>
  <br>

  1. Estrutura de mercado:
      - Formas de organização da atividade econômica, o papel dos preços, custo de oportunidade e fronteiras das possibilidades de produção
  2. Oferta e demanda:
      - Curvas de indiferença
      - Restrição orçamentária
      - Equilíbrio do consumidor
      - Efeitos preço, renda e substituição
      - Curva de demanda
      - Elasticidade da demanda

</details>

<script>
// Script para o funcionamento do accordion
document.addEventListener("DOMContentLoaded", function() {
  const details = document.querySelectorAll("details");

  details.forEach(detail => {
    detail.addEventListener("toggle", function() {
      this.classList.toggle("active", this.open);
    });
  });
});
</script>
