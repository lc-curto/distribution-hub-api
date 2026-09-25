# Ações de um utilizador autenticado

Este documento define o que um utilizador pode fazer depois de iniciar
sessão. As ações dependem do papel e da empresa ativa.

## Primeiro acesso

Um utilizador que ainda não pertence a nenhuma empresa deve concluir o
onboarding antes de aceder às áreas operacionais.

O onboarding recolhe:

- nome do utilizador;
- email;
- palavra-passe;
- nome da empresa.

O fluxo é:

1. Validar os dados informados.
2. Criar o utilizador.
3. Criar a empresa.
4. Criar o vínculo entre utilizador e empresa.
5. Atribuir `role = ADMIN`.
6. Iniciar a sessão.
7. Definir a empresa criada como ativa.
8. Encaminhar o utilizador para o dashboard.

A criação do utilizador, da empresa e do vínculo `ADMIN` deve ocorrer na
mesma transação. Se alguma etapa falhar, nenhum registro deve permanecer.

## Utilizador autenticado sem empresa

Um utilizador autenticado sem empresas associadas deve ser encaminhado
para o onboarding.

Enquanto não criar ou aceitar uma associação a uma empresa, não pode
aceder às áreas operacionais.

## Acessos seguintes

Depois do login, o sistema deve:

1. Listar as empresas associadas ao utilizador.
2. Selecionar automaticamente a empresa se houver apenas uma.
3. Pedir a seleção de uma empresa ativa se houver mais de uma.
4. Bloquear as áreas operacionais se não existir uma empresa ativa válida.

## Ações comuns

Todo utilizador autenticado e associado a uma empresa pode:

- consultar as empresas às quais está associado;
- selecionar uma empresa ativa;
- consultar o próprio perfil;
- terminar a sessão;
- aceder somente aos dados da empresa ativa;
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

A empresa deve manter pelo menos um `ADMIN` ativo.

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

Não pode:

- gerir utilizadores;
- gerir papéis;
- alterar configurações administrativas;
- gerir preços;
- consultar custos, margens ou lucros;
- executar operações administrativas não autorizadas.

## Limites comuns

Nenhum utilizador autenticado pode:

- aceder a dados de outra empresa;
- alterar o `tenant_id` para escapar ao isolamento;
- consultar dados sem permissão;
- confiar apenas na validação do frontend;
- apagar definitivamente dados que precisam de histórico.

## Regra técnica

O backend deve validar:

- autenticação;
- empresa ativa;
- associação do utilizador ao tenant;
- papel;
- permissões;
- regras de negócio;
- isolamento dos dados.

A interface React pode orientar e ocultar ações não permitidas, mas não é
uma camada de segurança.
