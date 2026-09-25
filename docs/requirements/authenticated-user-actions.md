# Ações de um utilizador autenticado

Este documento define o que um utilizador pode fazer depois de iniciar sessão. As ações dependem do papel e da empresa ativa.

## Ações comuns

Todo utilizador autenticado e associado a pelo menos uma empresa pode:

- consultar as empresas às quais está associado;
- selecionar uma empresa ativa;
- consultar o próprio perfil;
- terminar a sessão;
- aceder apenas aos dados da empresa ativa;
- executar ações permitidas pelo seu papel.

## Administrador (`ADMIN`)

Dentro da empresa ativa, pode:

- gerir utilizadores associados;
- atribuir ou alterar papéis;
- gerir configurações básicas da empresa;
- criar, editar e inativar clientes;
- criar e editar categorias, produtos e preços;
- gerir entradas, saídas e ajustes de estoque;
- criar, confirmar e cancelar pedidos;
- consultar e gerir contas a receber;
- consultar o dashboard e a auditoria disponível.

## Operador (`OPERATOR`)

Dentro da empresa ativa, pode:

- criar, editar e inativar clientes;
- consultar categorias, produtos e preços autorizados;
- consultar estoque;
- criar e consultar pedidos;
- confirmar pedidos quando as regras permitirem;
- registrar operações de estoque permitidas;
- registrar pagamentos permitidos;
- consultar indicadores operacionais.

Não pode gerir utilizadores, papéis, configurações administrativas ou preços.

## Limites comuns

Nenhum utilizador autenticado pode:

- aceder a dados de outra empresa;
- alterar o `tenant_id` de uma operação para escapar ao isolamento;
- consultar dados para os quais não tem permissão;
- confiar apenas na validação do frontend;
- apagar definitivamente dados que precisam de histórico.

## Regra técnica

O backend deve validar autenticação, empresa ativa, associação ao tenant, papel, permissões e regras de negócio. A interface React apenas orienta o utilizador e não é uma camada de segurança.
