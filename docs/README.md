# Documentação do Cosmetics Hub

Documentação comum do produto, mantida no repositório da API. O frontend está em [cosmetics-hub-web](https://github.com/lc-curto/cosmetics-hub-web).

## Comece por aqui

- [Produto e escopo](product.md)
- [Domínio e regras essenciais](domain.md)
- [Requisitos e pendências](requirements.md)
- [Arquitetura](architecture.md)
- [API](api.md)
- [Spec 001 — acesso, empresas e clientes](specs/001-auth-tenants-customers.md)

## Estado atual

A API possui apenas `GET /health`, coberto por teste. O frontend é um scaffold. PostgreSQL está configurado para desenvolvimento local, mas não há modelos, migrations ou fluxos comerciais implementados.

Os documentos distinguem:

- **Implementado:** existe no código e tem validação adequada.
- **Especificado:** comportamento pretendido, ainda não implementado.
- **Por definir:** decisão ou critério ainda pendente.

Requisitos e diagramas não são evidência de funcionalidade entregue.