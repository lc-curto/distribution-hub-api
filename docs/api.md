# API

## Estado atual

| Método | Caminho | Resposta | Estado |
|---|---|---|---|
| `GET` | `/health` | `200` com `{"status":"ok"}` | Implementado e testado |

Não existem endpoints de autenticação, empresas, clientes, catálogo, estoque, pedidos ou recebíveis.

## OpenAPI

FastAPI gera o contrato em `/openapi.json` e a documentação interativa em `/docs`. No estado atual, o contrato descreve apenas as rotas existentes, essencialmente `/health`.

Quando as áreas comerciais forem implementadas, o contrato deverá evoluir junto com os testes da API e a integração do frontend. Versionamento e validação entre os dois repositórios ainda são pendências.