# Regras de negócio — MVP

**Produto:** Cosmetics Hub  
**Escopo:** MVP  
**Estado:** versão inicial consolidada

Estas regras orientam banco de dados, backend, frontend e testes. Cada regra deve ser implementável e testável.

## Empresas e isolamento

### RN-001 — Utilizador em várias empresas
Um utilizador pode pertencer a várias empresas.

### RN-002 — Papel por empresa
O papel é definido no vínculo entre utilizador e empresa. O mesmo utilizador pode ser `ADMIN` numa empresa e `OPERATOR` noutra.

### RN-003 — Isolamento
Um utilizador só pode aceder aos dados das empresas às quais está associado. O backend deve garantir o isolamento independentemente dos parâmetros enviados pelo frontend.

### RN-004 — Empresa ativa
Depois do login, o utilizador seleciona uma empresa ativa. As operações seguintes usam esse contexto.

### RN-005 — Sem empresa ativa
As áreas operacionais ficam bloqueadas sem uma empresa ativa válida.

## Papéis

### RN-010 — Administrador
`ADMIN` gere utilizadores, papéis, configurações básicas, clientes, catálogo, estoque, pedidos e recebíveis da própria empresa.

### RN-011 — Operador
`OPERATOR` executa operações comerciais diárias, como clientes, consulta de catálogo/estoque e criação de pedidos. Não gere utilizadores, papéis, configurações administrativas ou preços.

### RN-012 — Último administrador
O sistema não pode remover nem despromover o último `ADMIN` ativo de uma empresa.

## Clientes

### RN-020 — Cliente sem acesso
O cliente é uma entidade de negócio e não possui login no MVP.

### RN-021 — Gestão de clientes
`ADMIN` e `OPERATOR` podem criar, editar e inativar clientes da empresa ativa.

### RN-022 — Exclusão
A regra padrão é inativar clientes. Exclusão física fica fora do fluxo normal.

## Produtos, categorias e preços

### RN-030 — Produtos
`ADMIN` e `OPERATOR` podem gerir dados operacionais dos produtos.

### RN-031 — Categorias
Categorias pertencem à empresa ativa.

### RN-032 — Preços
A gestão de preços é reservada ao `ADMIN`. O `OPERATOR` pode utilizar preços previamente configurados.

### RN-033 — Produtos inativos
Produtos inativos não podem ser adicionados a novos pedidos.

## Estoque

### RN-040 — Movimentação
Toda entrada, saída ou ajuste gera um movimento de estoque identificado pelo produto, utilizador, empresa, data e tipo.

### RN-041 — Estoque negativo
O estoque nunca pode ficar negativo no MVP. A operação deve ser rejeitada se não houver saldo suficiente.

### RN-042 — Ajuste
Um ajuste manual exige motivo.

### RN-043 — Saldo e histórico
O saldo serve para consulta rápida e os movimentos preservam o histórico operacional.

## Pedidos

### RN-050 — Criação
`ADMIN` e `OPERATOR` podem criar pedidos para clientes da empresa ativa.

### RN-051 — Estados
O pedido possui, no MVP, os estados `DRAFT`, `CONFIRMED` e `CANCELLED`.

### RN-052 — Rascunho
Pedidos em `DRAFT` podem ser alterados e não movimentam estoque.

### RN-053 — Confirmação
Ao confirmar, o sistema valida cliente, produtos ativos, preços e estoque. A confirmação movimenta o estoque numa transação.

### RN-054 — Pedido confirmado
Pedidos `CONFIRMED` não podem ser editados no MVP.

### RN-055 — Cancelamento
O cancelamento exige motivo e registra histórico. A reversão de estoque ocorre conforme o fluxo definido para cancelamento.

### RN-056 — Desconto
O desconto não pode deixar o total negativo. Limites avançados de desconto ficam fora do MVP.

## Contas a receber

### RN-060 — Geração
Um pedido confirmado gera um recebível.

### RN-061 — Estados
Um recebível pode estar `OPEN`, `PARTIALLY_PAID`, `PAID`, `OVERDUE` ou `CANCELLED`.

### RN-062 — Pagamento parcial
O sistema permite pagamentos parciais e atualiza o saldo pendente.

### RN-063 — Pagamento excedente
Um pagamento não pode ultrapassar o saldo pendente no MVP. Crédito de cliente fica para uma versão futura.

### RN-064 — Vencimento
O sistema identifica recebíveis vencidos com base na data de vencimento e no saldo pendente.

### RN-065 — Cancelamento de pedido
Ao cancelar um pedido confirmado, o saldo ainda não pago é cancelado. Pagamentos já registrados permanecem no histórico; reembolsos ficam fora do MVP.

## Auditoria mínima

### RN-070 — Operações críticas
Confirmações, cancelamentos, ajustes de estoque, pagamentos e alterações administrativas devem registrar utilizador, empresa, data, operação e contexto suficiente para investigação.

### RN-071 — Histórico
Registros necessários para histórico operacional e financeiro não devem ser apagados no fluxo normal.

## Dashboard

### RN-080 — Indicadores
O dashboard pode apresentar vendas do período, pedidos recentes, total a receber e produtos com estoque baixo.

### RN-081 — Isolamento
Os indicadores consideram apenas dados da empresa ativa.

## Princípio de implementação

As regras de segurança e negócio devem ser validadas principalmente no backend e, quando necessário, protegidas também por constraints e transações do banco. O frontend pode validar e orientar, mas não é uma camada de segurança.

## Regras fora deste MVP

Aprovações, limites avançados, versionamento, snapshots, margem, custos, notificações avançadas, crédito de cliente, cobrança, juros, multas, aprovação em lote e multi-armazéns avançados estão documentados em `business-rules-future.md`.

## Testes prioritários

- [ ] Isolamento por tenant
- [ ] Proteção do último administrador
- [ ] Produto inativo não entra em pedido
- [ ] Estoque nunca fica negativo
- [ ] Confirmação de pedido é transacional
- [ ] Pedido confirmado não pode ser alterado
- [ ] Pedido confirmado gera recebível
- [ ] Pagamento não ultrapassa saldo
