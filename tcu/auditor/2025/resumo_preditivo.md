# Resumo Preditivo – TCU AUFC TI (Cebraspe)

Sumário
- [Definições rápidas por tema](#definições-rápidas-por-tema)
- [Questões de treino (Certo/Errado)](#questões-de-treino-certoerrado)

## Definições rápidas por tema

- **Segurança da Informação**: CIA = confidencialidade (acesso só a autorizados), integridade (dados não alterados indevidamente), disponibilidade (acesso quando necessário); autenticidade confirma origem; não repúdio impede negar autoria; MFA combina fatores; TLS provê conf+int+autenticidade na sessão; ataques comuns: DoS/DDoS, spoofing (IP/ARP), XSS/SQLi em aplicações.
- **Criptografia**: em trânsito (TLS) protege canal; em repouso protege armazenado; assinatura digital assegura integridade+autenticidade+não repúdio; criptografia simétrica usa chave única, assimétrica usa par de chaves.
- **Infra/Virtualização/OS**: paravirtualização expõe hiperchamadas ao convidado, reduz overhead; hipervisores tipo 1 bare-metal, tipo 2 hospedado; RAID 0 só performance, sem redundância; RAID 1 espelha; RAID 5 paridade distribuída; WSL executa Linux sobre Windows sem dual boot.
- **Redes**: VLAN segmenta broadcast; STP evita loop; QoS prioriza tráfego; BGP roteia entre sistemas autônomos; OSPF roteia intra-domínio; wireless corporativo usa WPA3; segmentação e ACLs mitigam lateralização.
- **Cloud/IAM/K8s**: IaaS/PaaS/SaaS diferem na pilha gerenciada; IAM controla identidades e permissões (RBAC, least privilege); Zero Trust = nunca confiar, sempre verificar; Kubernetes orquestra contêineres (pods, deployments, services); multicloud/híbrida combinam provedores e datacenter.
- **DevOps/CI-CD/Observabilidade**: pipeline CI/CD automatiza build, testes e deploy; versionamento (Git) rastreia código/infra; observabilidade = métricas, logs, traces; feature flags liberam gradualmente; IaC (Terraform) descreve infra como código.
- **Arquitetura/Integração/Ágil**: monolito = único deploy; microserviços = serviços pequenos, acoplamento fraco; event-driven usa mensageria; API Gateway centraliza autenticação/quotas; BPMN 2.0 modela processos; Scrum: sprints, backlog, PO, SM, dev team.
- **Dados/IA/MLOps**: ETL extrai-transforma-carrega; datalake armazena dados brutos; lakehouse une lake + estrutura; NoSQL (Mongo, Elastic) flexível; ML supervisionado usa rótulos, não supervisionado identifica padrões; validação cruzada mede generalização; MLOps versiona dados/modelos e automatiza treino/deploy.
- **ITIL/COBIT/Governança**: incidente = interrupção ou degradação não planejada; problema = causa raiz; mudança = alteração controlada; SLA define níveis de serviço; COBIT 2019 orienta governança de TI por objetivos.
- **Contratações de TI (Lei 14.133 + IN SGD/ME)**: ETP estuda viabilidade; TR/Projeto Básico detalha solução; gestão e fiscalização: gestor, fiscal técnico e administrativo; riscos mapeados em matriz; SLAs e penalidades contratualmente definidos; pesquisa de preços conforme IN.

## Questões de treino (Certo/Errado)
1. Em TLS autenticado, confidencialidade, integridade e autenticidade do canal são garantidas simultaneamente.
2. RAID 0 melhora desempenho mas não oferece qualquer tolerância a falhas.
3. Na paravirtualização, o sistema convidado precisa ser adaptado para chamar o hipervisor diretamente.
4. BGP é protocolo típico de roteamento interno (intra-AS) e substitui OSPF em redes corporativas locais.
5. VLANs segmentam domínio de broadcast e, sozinhas, impedem completamente ataques de ARP spoofing.
6. Kubernetes abstrai contêineres por meio de pods e usa services para expor aplicações de forma estável.
7. Em CI/CD, testes automatizados devem rodar após o deploy em produção para não impactar o lead time.
8. Observabilidade requer métricas, logs e traces para permitir diagnóstico de causa raiz em produção.
9. Em arquitetura event-driven, o acoplamento é reduzido porque produtores e consumidores comunicam-se por eventos e filas.
10. BPMN 2.0 permite modelar gateways de decisão e paralelismo; ausência de start event implica execução sequencial única.
11. Scrum define papéis de Product Owner, Scrum Master e Time de Desenvolvimento; o PO prioriza o backlog.
12. Validação cruzada K-fold mede generalização dividindo o conjunto em K partições e alternando treino/teste.
13. MLOps inclui versionamento de dados/modelos e automação de pipeline de treino, validação e deploy.
14. Na gestão de incidentes (ITIL v4), o objetivo é restaurar serviço rapidamente; gestão de problemas busca causa raiz.
15. SLAs em contratos de TI devem ser medíveis e vinculados a penalidades; a matriz de risco define responsabilidades.
16. A Lei 14.133/2021 exige Estudo Técnico Preliminar para contratações de TI e admite o uso de Termo de Referência.
17. Zero Trust pressupõe perímetro confiável interno; por isso dispensa reautenticação interna entre serviços.
18. API Gateway centraliza autenticação, rate limiting e roteamento, mas não deve realizar qualquer transformação em payloads.
19. Em datalake, dados são armazenados apenas já estruturados; dados brutos devem ser rejeitados para manter esquema.
20. NoSQL como MongoDB e Elasticsearch permitem esquemas flexíveis e escalam horizontalmente, mas não suportam consultas complexas.
