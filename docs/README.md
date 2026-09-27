# Documentação do Cosmetics Hub

Esta documentação descreve o produto, suas regras, requisitos, arquitetura e estado implementado. A fonte comum fica neste repositório da API; o frontend está em [cosmetics-hub-web](https://github.com/lc-curto/cosmetics-hub-web).

## Como ler

- **Visão geral:** [visão do produto](product/vision.md), [escopo](product/scope.md) e [estado atual](project-status.md).
- **Domínio:** [glossário](domain/glossary.md), [atores e papéis](domain/actors-and-roles.md), [modelo de domínio](domain/domain-model.md) e [modelo de dados](database/data-model.md).
- **Requisitos:** [requisitos funcionais](requirements/functional-requirements.md), [regras de negócio](requirements/business-rules.md), [qualidade e segurança](requirements/non-functional-requirements.md), [autenticação](requirements/authentication.md) e [questões em aberto](requirements/open-questions.md).
- **Especificação funcional:** [Spec 001 — autenticação, empresas e clientes](specs/001-auth-tenants-customers.md).
- **Arquitetura:** [visão da arquitetura](architecture/overview.md), [diagrama de contexto](architecture/diagrams/system-context.mmd) e [registros de decisão (ADRs)](architecture/decisions/README.md).
- **API:** [contrato e endpoints disponíveis](api/README.md).
- **Desenvolvimento:** [fluxo de trabalho para mudanças](development-workflow.md).
- **Método documental:** [princípios usados nesta documentação](documentation-principles.md).
- **Histórico:** [registro de evolução arquitetural e documental](history/project-chronology.md).

## Como interpretar o estado

- **Implementado:** confirmado no código e, quando aplicável, coberto por teste.
- **Especificado:** aparece nos documentos como comportamento pretendido; ainda não significa que esteja implementado ou aprovado para entrega.
- **Aceito:** escolha de produto ou arquitetura registrada como decisão vigente.
- **Por definir:** falta uma decisão de produto ou técnica; não se deve presumir uma resposta.

O [estado atual](project-status.md) é a referência para distinguir documentação de implementação. Requisitos sem validação explícita do responsável pelo produto são tratados como especificados, não como compromissos de entrega.

## Princípios de manutenção

Atualize o documento correspondente quando o comportamento, uma regra ou uma decisão mudar. Uma ADR registra uma decisão técnica significativa; uma regra de negócio não deve ser usada para esconder uma escolha de implementação. Mantenha este índice curto e direcione cada público ao nível de detalhe adequado.
