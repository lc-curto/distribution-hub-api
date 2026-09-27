# Regras de negócio

**Escopo:** primeira entrega comercial documentada. **Estado:** especificadas em documentação; ainda não implementadas no código. Estas regras consolidam o material preservado e não substituem validação do responsável pelo produto.

## Empresas, usuários e isolamento

| ID | Regra documentada |
|---|---|
| RN-001 | Uma pessoa pode estar associada a mais de uma empresa. |
| RN-002 | O papel é definido por associação entre pessoa e empresa; a mesma pessoa pode ter papéis diferentes em empresas diferentes. |
| RN-003 | Um usuário só pode acessar dados de empresas às quais está associado. O backend deve garantir o isolamento, independentemente dos dados enviados pela interface. |
| RN-004 | Operações protegidas ocorrem no contexto de uma empresa ativa válida. O mecanismo técnico que transmite esse contexto ainda está por definir. |
| RN-005 | Sem empresa ativa e autorizada, áreas operacionais ficam bloqueadas. |
| RN-006 | A forma como uma pessoa passa a pertencer à primeira empresa — cadastro aberto, criação autônoma ou convite — ainda depende de decisão do produto; nenhuma dessas opções está definida como fluxo vigente. |
| RN-007 | Quando um processo autorizado estabelecer a primeira associação administrativa de uma empresa, o vínculo recebe `ADMIN`. O backend valida e atribui esse papel. |
| RN-008 | Se o fluxo aprovado criar ou associar registros locais em conjunto, a operação deve ser atômica e não deixar registros parciais. O fluxo aprovado e a relação com a identidade externa ainda estão por definir. |
| RN-009 | Cada empresa deve manter pelo menos um `ADMIN` ativo. |
| RN-010 | O sistema não pode remover nem rebaixar o último `ADMIN` ativo da empresa. |

## Papéis

| ID | Regra documentada |
|---|---|
| RN-011 | `ADMIN` administra usuários, papéis e configurações básicas de sua empresa, além das operações comerciais autorizadas. |
| RN-012 | `OPERATOR` executa operações comerciais diárias, mas não administra usuários, papéis ou configurações administrativas. |
| RN-013 | A permissão é verificada no backend dentro da empresa ativa. A interface não é uma barreira de segurança. |

A matriz resumida está em [atores e papéis](../domain/actors-and-roles.md). Há divergência documental sobre edição de produtos, estoque e pagamentos pelo operador; consulte [questões em aberto](open-questions.md#permissões-do-papel-operator).

## Clientes

| ID | Regra documentada |
|---|---|
| RN-020 | Um cliente comercial não possui conta de acesso ao sistema no escopo atual. |
| RN-021 | Usuários autorizados podem criar, consultar, editar e inativar clientes da empresa ativa. |
| RN-022 | A operação normal inativa clientes em vez de apagá-los fisicamente. Clientes inativos permanecem disponíveis no histórico, mas não podem ser usados em novos pedidos. |
| RN-023 | Uma empresa não pode consultar ou alterar clientes pertencentes a outra empresa. |
| RN-024 | `customer_code`, quando informado, é único dentro da empresa. |

## Catálogo e preços

| ID | Regra documentada |
|---|---|
| RN-030 | Categorias e produtos pertencem à empresa que os administra. |
| RN-031 | `ADMIN` gerencia preços; `OPERATOR` pode consultar e usar preços que lhe sejam autorizados. |
| RN-032 | Produtos inativos não podem ser adicionados a novos pedidos; seu uso no histórico é preservado. |
| RN-033 | As permissões exatas de criação e edição de produto/categoria pelo operador ainda precisam de validação. |

## Estoque

| ID | Regra documentada |
|---|---|
| RN-040 | Cada entrada, saída ou ajuste gera um movimento identificável por empresa, produto, usuário responsável, data e tipo. |
| RN-041 | O saldo não pode ficar negativo; uma saída sem saldo suficiente é rejeitada. |
| RN-042 | Um ajuste manual exige justificativa. |
| RN-043 | Movimentos mantêm histórico; o saldo pode ser consultado sem apagar esse histórico. |

A autorização por papel para cada tipo de movimento ainda está por confirmar.

## Pedidos

| ID | Regra documentada |
|---|---|
| RN-050 | Um usuário autorizado pode criar pedidos para clientes da empresa ativa. |
| RN-051 | Os estados documentados são `DRAFT`, `CONFIRMED` e `CANCELLED`. |
| RN-052 | Um pedido `DRAFT` pode ser alterado e não movimenta estoque. |
| RN-053 | Antes de confirmar, o sistema valida cliente, produtos ativos, preços e saldo de estoque. A confirmação e os movimentos correspondentes são atômicos. |
| RN-054 | Um pedido `CONFIRMED` não pode ser editado no escopo atual. |
| RN-055 | O cancelamento exige justificativa e registro histórico. A regra exata de reversão do estoque ainda não está definida. |
| RN-056 | Desconto não pode tornar o total negativo. Limites avançados de desconto não fazem parte do escopo atual. |

## Contas a receber e pagamentos

| ID | Regra documentada |
|---|---|
| RN-060 | Um pedido confirmado gera um valor a receber associado. |
| RN-061 | Os estados documentados são `OPEN`, `PARTIALLY_PAID`, `PAID`, `OVERDUE` e `CANCELLED`. |
| RN-062 | São permitidos pagamentos parciais e totais; cada pagamento recalcula o saldo pendente. |
| RN-063 | O total pago não pode superar o saldo pendente. Crédito excedente de cliente não faz parte do escopo atual. |
| RN-064 | Um valor a receber é considerado vencido quando passou da data de vencimento e ainda tem saldo pendente. A regra de fuso/calendário não foi definida. |
| RN-065 | Ao cancelar pedido confirmado, o saldo não pago é cancelado. Pagamentos já registrados permanecem no histórico; reembolsos ficam fora do escopo atual. |

## Histórico, auditoria e indicadores

| ID | Regra documentada |
|---|---|
| RN-070 | Confirmações, cancelamentos, ajustes de estoque, pagamentos e alterações administrativas devem registrar quem fez, em qual empresa, quando e o contexto necessário para investigação. |
| RN-071 | Dados necessários ao histórico operacional e financeiro não são apagados no fluxo normal. Prazos legais de retenção ainda não estão especificados. |
| RN-080 | O painel pode resumir vendas do período, pedidos recentes, valores a receber e produtos com estoque baixo. |
| RN-081 | Indicadores são limitados à empresa ativa e ao período selecionado. |

## Ideias fora do escopo atual

Foram listadas para possível evolução, sem compromisso de entrega: limites e aprovações avançados, versionamento e restauração de pedidos, snapshots, custos e margens, notificações avançadas, crédito de cliente, juros e multas, cobrança, compras e devoluções complexas, múltiplos armazéns avançados, marketplace e integração bancária. Cada item precisa de requisitos e decisão próprios antes de entrar no escopo.
