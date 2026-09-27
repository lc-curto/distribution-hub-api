# Requisitos funcionais

**Estado geral:** requisitos especificados; nenhuma área comercial abaixo está implementada no código atual. A API tem apenas `GET /health`. As capacidades devem ganhar critérios de aceitação refinados antes de serem tratadas como entregues.

## Acesso e empresas

| ID | O sistema deve… | Estado |
|---|---|---|
| RF-001 | permitir que uma pessoa estabeleça acesso válido; o método concreto segue a decisão documentada em [autenticação](authentication.md). | Especificado |
| RF-002 | reconhecer o usuário autenticado em operações protegidas. | Especificado |
| RF-003 | permitir encerrar o acesso autenticado. | Especificado; mecanismo por definir |
| RF-004 | impedir acesso não autenticado a recursos privados. | Especificado |
| RF-005 | permitir o ingresso/cadastro de usuário de acordo com o fluxo de identidade e onboarding a definir. | Parcialmente especificado |
| RF-006 | suportar o processo de associação a uma empresa que for aprovado pelo produto; cadastro aberto, criação autônoma e convite ainda não foram escolhidos. | Por definir |
| RF-007 | quando um processo autorizado estabelecer a primeira associação administrativa da empresa, atribuir `ADMIN` no backend. | Especificado; não implementado |
| RF-008 | permitir acesso às áreas operacionais somente após conclusão do processo de acesso aprovado e validação de uma associação ativa. | Por definir; fluxo não implementado |
| RF-010 | listar as empresas às quais o usuário está associado. | Especificado |
| RF-011 | selecionar ou identificar a empresa ativa para operações posteriores. | Especificado; transporte técnico por definir |
| RF-012 | permitir ao `ADMIN` consultar, convidar, desativar e alterar o papel dos usuários da própria empresa, preservando o último administrador. | Especificado; convite precisa de detalhe |
| RF-013 | suportar `ADMIN` e `OPERATOR` por associação com a empresa. | Especificado |

## Clientes

| ID | O sistema deve… | Estado |
|---|---|---|
| RF-020 | criar clientes na empresa ativa para usuários autorizados. | Especificado |
| RF-021 | listar e consultar clientes somente da empresa ativa. | Especificado |
| RF-022 | permitir pesquisa, filtros, ordenação e paginação de clientes. | Especificado; filtros a detalhar |
| RF-023 | editar dados de cliente de acordo com permissões. | Especificado |
| RF-024 | inativar clientes sem apagar o histórico normal. | Especificado |

## Catálogo e preços

| ID | O sistema deve… | Estado |
|---|---|---|
| RF-030 | consultar categorias e permitir sua gestão conforme o papel definido. | Especificado; permissões de `OPERATOR` pendentes |
| RF-031 | criar, consultar, editar e inativar produtos. | Especificado; permissões pendentes |
| RF-032 | permitir ao `ADMIN` manter preços e permitir consulta/uso de preços autorizados. | Especificado; grupos e vigência por detalhar |
| RF-033 | pesquisar e filtrar produtos por nome, categoria e estado. | Especificado |

## Estoque

| ID | O sistema deve… | Estado |
|---|---|---|
| RF-040 | consultar saldo de estoque por produto. | Especificado |
| RF-041 | registrar entradas de estoque para pessoas autorizadas. | Especificado; papéis pendentes |
| RF-042 | registrar saídas somente quando houver saldo suficiente. | Especificado |
| RF-043 | registrar ajustes com justificativa. | Especificado |
| RF-044 | manter e permitir consultar o histórico dos movimentos. | Especificado |
| RF-045 | identificar produtos abaixo do nível mínimo configurado. | Especificado; definição do limite pendente |

## Pedidos

| ID | O sistema deve… | Estado |
|---|---|---|
| RF-050 | criar pedidos em estado `DRAFT`. | Especificado |
| RF-051 | permitir alterar itens, quantidades e descontos enquanto o pedido for `DRAFT`. | Especificado |
| RF-052 | calcular subtotal, desconto e total. | Especificado; regra monetária por detalhar |
| RF-053 | confirmar pedido somente após validar cliente, produtos, preços e estoque. | Especificado |
| RF-054 | efetuar confirmação e movimentação de estoque sem deixar atualização parcial. | Especificado |
| RF-055 | cancelar pedidos conforme as regras, exigindo justificativa e preservando histórico. | Especificado; reversão do estoque por definir |
| RF-056 | manter o histórico de mudanças de estado. | Especificado |

## Contas a receber e painel

| ID | O sistema deve… | Estado |
|---|---|---|
| RF-060 | criar um recebível após confirmação do pedido. | Especificado |
| RF-061 | consultar recebíveis abertos, parciais, pagos, vencidos e cancelados. | Especificado |
| RF-062 | registrar pagamentos parciais ou totais para usuários autorizados. | Especificado; papéis e meios de pagamento pendentes |
| RF-063 | atualizar saldo e estado após cada pagamento. | Especificado |
| RF-064 | identificar recebíveis vencidos com saldo pendente. | Especificado; calendário por detalhar |
| RF-070 | apresentar indicadores da empresa ativa: vendas do período, pedidos recentes, valores a receber e estoque baixo. | Especificado |
| RF-071 | filtrar indicadores por período. | Especificado; períodos e fuso por definir |

## Evidência de entrega

Um requisito só deve mudar para **Implementado** quando existir comportamento correspondente no repositório e verificação adequada. O [estado atual](../project-status.md) mostra que, no momento, estes requisitos são documentação de produto, não funcionalidade disponível.
