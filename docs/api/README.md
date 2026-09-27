# API e contrato HTTP

## Estado disponível

A aplicação FastAPI atual disponibiliza:

| Método | Caminho | Resposta | Estado |
|---|---|---|---|
| `GET` | `/health` | `200` com `{"status":"ok"}` | Implementado e coberto por teste |

Não há endpoints documentados ou implementados para autenticação, empresas, clientes, catálogo, estoque, pedidos ou recebíveis.

## OpenAPI

FastAPI gera `/openapi.json` a partir das rotas e schemas existentes e oferece a documentação interativa em `/docs`. Portanto, no estado atual, o contrato descreve somente o endpoint de saúde. Não há uma cópia manual de OpenAPI versionada aqui.

Quando endpoints de negócio forem implementados, mantenha o contrato gerado alinhado com a API e defina como será validado pelo frontend no repositório separado. A decisão sobre formato de cliente compartilhado e versionamento ainda está em aberto; consulte [questões em aberto](../requirements/open-questions.md#qualidade-privacidade-e-operação).