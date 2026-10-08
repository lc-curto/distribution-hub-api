# Documentação do Distribution Hub

Documentação comum do produto, mantida no repositório da API. O frontend está em [distribution-hub-web](https://github.com/lc-curto/distribution-hub-web).

## Comece por aqui

- [Produto e escopo](product.md)
- [Domínio e regras essenciais](domain.md)
- [Requisitos e pendências](requirements.md)
- [Arquitetura](architecture.md)
- [API](api.md)
- [Roadmap de aprendizagem e desenvolvimento](learning-roadmap.md)
- [Spec 001 — acesso, empresas e clientes](specs/001-auth-tenants-customers.md)

## Estado atual

A API expõe atualmente `GET /health`, coberto por teste, mas ainda não possui endpoints comerciais. O frontend é um scaffold. PostgreSQL está configurado para desenvolvimento local; os modelos SQLAlchemy `User` e `Tenant` e migrations para `users` e `tenants` já existem. O vínculo `tenant_users`, os clientes e os fluxos comerciais continuam por implementar.

Os documentos distinguem:

- **Implementado:** existe no código e tem validação adequada.
- **Especificado:** comportamento pretendido, ainda não implementado.
- **Por definir:** decisão ou critério ainda pendente.

Requisitos e diagramas não são evidência de funcionalidade entregue.
