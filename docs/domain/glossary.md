# Glossário do domínio

| Termo | Significado neste produto |
|---|---|
| **Empresa** (`tenant`) | Organização que usa o Cosmetics Hub. Os dados comerciais são separados por empresa. |
| **Usuário** (`user`) | Pessoa com uma conta de acesso ao sistema. Não é o mesmo que um cliente comercial. |
| **Associação** (`tenant_user`) | Vínculo entre um usuário e uma empresa. Guarda o papel e o estado do acesso naquela empresa. |
| **Papel** | Conjunto de permissões de uma pessoa dentro de uma empresa. Os papéis documentados são `ADMIN` e `OPERATOR`. |
| **Empresa ativa** | Empresa selecionada para o contexto da operação atual. A seleção e o mecanismo de transporte ainda precisam de especificação técnica. |
| **Cliente** (`customer`) | Pessoa ou organização para quem a empresa vende. No escopo documentado, não possui conta de acesso ao Cosmetics Hub. |
| **Catálogo** | Produtos e categorias que a empresa disponibiliza para suas operações comerciais. |
| **Movimento de estoque** | Registro de entrada, saída ou ajuste que afeta o saldo de um produto. |
| **Pedido** | Registro de uma venda solicitada por um cliente, com itens e um estado de processamento. |
| **Conta a receber** (`receivable`) | Valor devido à empresa, normalmente associado a um pedido confirmado. |
| **OAuth 2.0** | Framework de autorização escolhido em alto nível. Sozinho, não especifica a autenticação interoperável de uma pessoa. |
| **OpenID Connect (OIDC)** | Camada de identidade sobre OAuth 2.0. Sua adoção no Cosmetics Hub ainda não foi confirmada. |
| **API** | Interface pela qual uma aplicação solicita dados ou operações a outra. Neste projeto, a API é implementada com FastAPI. |
| **Monólito modular** | Uma aplicação implantável organizada em módulos internos; não é uma coleção de microserviços. |
| **ADR** | *Architecture Decision Record*: registro curto do contexto, decisão técnica e consequências. |
| **OpenAPI** | Formato para descrever uma API HTTP e seus contratos. FastAPI pode gerar a especificação a partir dos endpoints implementados. |

Quando um termo tiver definição específica em uma regra, requisito ou spec, aquela definição específica prevalece.