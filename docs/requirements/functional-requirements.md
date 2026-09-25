# Requisitos funcionais — MVP

**Produto:** Cosmetics Hub  
**Escopo:** MVP

Requisitos funcionais descrevem **o que o sistema deve fazer**. Cada requisito deve ser implementado, validado e ligado a testes ou critérios de aceitação.

<!-- ============================================================
     CONTEXTO: AUTENTICAÇÃO E ACESSO
     ============================================================ -->

## Autenticação

### RF-001 — Login

O sistema deve permitir que um utilizador entre com email e palavra-passe.

### RF-002 — Sessão

O sistema deve manter uma sessão autenticada e permitir consultar o utilizador atual.

### RF-003 — Logout

O sistema deve permitir terminar a sessão.

### RF-004 — Proteção de rotas

O sistema deve impedir que utilizadores não autenticados acedam a áreas privadas.

### RF-005 — Cadastro inicial

O sistema deve permitir que uma pessoa crie uma conta com nome, email e palavra-passe.

### RF-006 — Criação da primeira empresa

Durante o cadastro inicial, o sistema deve permitir informar o nome da primeira empresa.

### RF-007 — Associação automática

Após criar a empresa, o sistema deve associar o utilizador como `ADMIN`.

### RF-008 — Conclusão do onboarding

Após a criação bem-sucedida, o sistema deve iniciar a sessão e definir a empresa criada como empresa ativa.

<!-- ============================================================
     CONTEXTO: EMPRESAS E UTILIZADORES
     ============================================================ -->

## Empresas e utilizadores

### RF-010 — Empresas do utilizador

O sistema deve listar as empresas às quais o utilizador está associado.

### RF-011 — Empresa ativa

O sistema deve permitir selecionar uma empresa ativa.

### RF-012 — Utilizadores da empresa

O `ADMIN` deve poder consultar, convidar, desativar e alterar o papel de utilizadores da própria empresa, respeitando a proteção do último administrador.

### RF-013 — Papéis

O sistema deve suportar, no MVP, os papéis `ADMIN` e `OPERATOR`.

<!-- ============================================================
     CONTEXTO: CLIENTES
     ============================================================ -->

## Clientes

### RF-020 — Criar cliente

Utilizadores autorizados devem poder criar clientes na empresa ativa.

### RF-021 — Consultar clientes

Utilizadores autorizados devem poder listar e consultar clientes da empresa ativa.

### RF-022 — Pesquisar e filtrar clientes

O sistema deve permitir pesquisar, filtrar, ordenar e paginar clientes.

### RF-023 — Editar cliente

Utilizadores autorizados devem poder editar dados de um cliente.

### RF-024 — Inativar cliente

Utilizadores autorizados devem poder inativar um cliente. A exclusão física não faz parte do fluxo normal.

<!-- ============================================================
     CONTEXTO: CATÁLOGO
     ============================================================ -->

## Catálogo

### RF-030 — Categorias

Utilizadores autorizados devem poder consultar e, conforme o papel, criar e editar categorias.

### RF-031 — Produtos

Utilizadores autorizados devem poder criar, consultar, editar e inativar produtos.

### RF-032 — Preços

O `ADMIN` deve poder criar e alterar preços e grupos de preços. O `OPERATOR` pode consultar e utilizar preços previamente configurados.

### RF-033 — Pesquisa de produtos

O sistema deve permitir pesquisar e filtrar produtos por nome, categoria e estado.

<!-- ============================================================
     CONTEXTO: ESTOQUE
     ============================================================ -->

## Estoque

### RF-040 — Saldo

O sistema deve permitir consultar o saldo de estoque por produto.

### RF-041 — Entrada

Utilizadores autorizados devem poder registrar entradas de estoque.

### RF-042 — Saída

Utilizadores autorizados devem poder registrar saídas de estoque quando houver saldo suficiente.

### RF-043 — Ajuste

Utilizadores autorizados devem poder registrar ajustes, informando um motivo.

### RF-044 — Histórico

O sistema deve manter e consultar o histórico de movimentações de estoque.

### RF-045 — Estoque baixo

O sistema deve identificar produtos cujo saldo esteja abaixo do estoque mínimo configurado.

<!-- ============================================================
     CONTEXTO: PEDIDOS
     ============================================================ -->

## Pedidos

### RF-050 — Criar rascunho

Utilizadores autorizados devem poder criar um pedido em estado `DRAFT`.

### RF-051 — Editar rascunho

Enquanto estiver em `DRAFT`, o pedido deve permitir adicionar, remover e alterar itens, quantidades e desconto.

### RF-052 — Calcular pedido

O sistema deve calcular subtotal, desconto e total do pedido.

### RF-053 — Confirmar pedido

O sistema deve permitir confirmar o pedido depois de validar cliente, produtos ativos, preços e estoque.

### RF-054 — Movimentar estoque

A confirmação do pedido deve registrar as movimentações e atualizar o estoque numa transação.

### RF-055 — Cancelar pedido

Utilizadores autorizados devem poder cancelar pedidos conforme as regras do MVP, com motivo e histórico.

### RF-056 — Histórico do pedido

O sistema deve manter o histórico de estados do pedido.

<!-- ============================================================
     CONTEXTO: CONTAS A RECEBER
     ============================================================ -->

## Contas a receber

### RF-060 — Gerar recebível

A confirmação de um pedido deve gerar o respetivo recebível.

### RF-061 — Consultar recebíveis

Utilizadores autorizados devem poder consultar contas abertas, pagas, parcialmente pagas, vencidas e canceladas.

### RF-062 — Registrar pagamento

Utilizadores autorizados devem poder registrar pagamentos parciais ou totais.

### RF-063 — Atualizar saldo

O sistema deve recalcular o saldo e o estado do recebível após cada pagamento.

### RF-064 — Identificar vencidos

O sistema deve identificar recebíveis vencidos com saldo pendente.

<!-- ============================================================
     CONTEXTO: DASHBOARD
     ============================================================ -->

## Dashboard

### RF-070 — Resumo operacional

O sistema deve apresentar, para a empresa ativa, vendas do período, pedidos recentes, total a receber e produtos com estoque baixo.

### RF-071 — Filtro de período

O dashboard deve permitir consultar indicadores por período.

<!-- ============================================================
     CONTEXTO: ORDEM DE IMPLEMENTAÇÃO
     ============================================================ -->

## Ordem de implementação

Os requisitos serão implementados por fatias verticais, seguindo:

```text
spec → banco/migration → backend → testes da API → frontend → integração → revisão