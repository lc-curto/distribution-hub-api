# Papéis iniciais do sistema

## ADMIN

Administrador da empresa dentro do Cosmetics Hub.

Pode:

- gerir utilizadores associados à empresa;
- atribuir e alterar papéis;
- gerir configurações básicas da empresa;
- gerir clientes, produtos, categorias e preços;
- gerir estoque, pedidos e contas a receber;
- consultar o dashboard e a auditoria disponível.

O sistema não pode remover nem despromover o último `ADMIN` ativo da empresa.

## Criação do primeiro ADMIN

O primeiro `ADMIN` não é criado manualmente por outro administrador.

Ele é criado automaticamente quando o primeiro utilizador conclui o cadastro
de uma nova empresa.

Utilizador cria conta
- Empresa é criada
- Vínculo utilizador–empresa é criado
- role = ADMIN.


## OPERATOR

Utilizador responsável pelas operações diárias da empresa.

Pode:

- criar, editar e inativar clientes;
- consultar produtos, categorias e preços autorizados;
- consultar estoque;
- criar e consultar pedidos;
- confirmar pedidos quando as regras permitirem;
- registrar operações de estoque permitidas;
- registrar pagamentos permitidos;
- consultar indicadores operacionais.

Não pode:

- gerir utilizadores ou papéis;
- alterar configurações administrativas;
- gerir tabelas de preços;
- consultar custos, margens ou lucros;
- executar operações administrativas não autorizadas.

## Regra de aplicação

O papel pertence ao vínculo entre utilizador e empresa. O mesmo utilizador pode ser `ADMIN` numa empresa e `OPERATOR` noutra.

O backend deve validar o papel dentro da empresa ativa. O frontend pode esconder ações não permitidas, mas não substitui a autorização do backend.
