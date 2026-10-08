# Documentação do Distribution Hub

Documentação comum do produto, mantida no repositório da API. O frontend está em [distribution-hub-web](https://github.com/lc-curto/distribution-hub-web ).

## Comece por aqui

- [Produto e escopo](product.md)
- [Domínio e regras essenciais](domain.md)
- [Requisitos e pendências](requirements.md)
- [Arquitetura](architecture.md)
- [API](api.md)
- [Roadmap de aprendizagem e desenvolvimento](learning-roadmap.md)
- [Spec 001 — acesso, empresas e clientes](specs/001-auth-tenants-customers.md)

## Estado atual

A API possui apenas `GET /health`, coberto por teste.

A fundação de persistência já foi preparada:

- PostgreSQL configurado para desenvolvimento local com Docker Compose;
- configuração carregada através de `.env`;
- SQLAlchemy configurado;
- modelo inicial `User`;
- tabela `users`;
- Alembic configurado;
- primeira migration criada e aplicada;
- testes existentes aprovados.

Ainda não existem endpoints de usuários, autenticação, empresas, clientes ou fluxos comerciais.

O frontend é um scaffold sem fluxos comerciais implementados.

Os documentos distinguem:

- **Implementado:** existe no código e tem validação adequada.
- **Especificado:** comportamento pretendido, ainda não implementado.
- **Por definir:** decisão ou critério ainda pendente.

Requisitos, diagramas e especificações não são evidência de funcionalidade entregue.
