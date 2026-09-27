# Atores e papéis

Este documento descreve os atores da especificação do produto. **As permissões abaixo ainda não são aplicadas pelo código**, conforme o [estado atual](../project-status.md).

## Atores

### Administrador da empresa (`ADMIN`)

Pessoa responsável pela gestão da empresa no Cosmetics Hub. A especificação lhe atribui gestão de usuários, papéis, configurações básicas, clientes, catálogo, preços, estoque, pedidos e valores a receber, sempre dentro da empresa ativa.

### Operador da empresa (`OPERATOR`)

Pessoa que executa operações comerciais diárias. A especificação lhe atribui gestão de clientes, consulta de catálogo e estoque, criação e consulta de pedidos e registro de operações permitidas. Não deve administrar usuários, papéis ou configurações administrativas.

### Usuário não autenticado

Pessoa que ainda não estabeleceu acesso válido. Não pode consultar ou alterar dados privados. O mecanismo de autenticação está descrito em [autenticação](../requirements/authentication.md).

### Cliente comercial

Pessoa ou organização cadastrada por uma empresa. No escopo documentado, cliente comercial é um registro do domínio e não um usuário que entra no sistema.

## Papel e empresa

O papel pertence à associação entre usuário e empresa, não à conta global do usuário. A mesma pessoa pode ter `ADMIN` em uma empresa e `OPERATOR` em outra. O backend deverá aplicar as permissões; esconder ações na interface não substitui autorização no servidor.

## Matriz resumida documentada

| Área | `ADMIN` | `OPERATOR` |
|---|---|---|
| Usuários, papéis e configurações administrativas | Gerenciar | Sem permissão |
| Clientes | Criar, consultar, editar e inativar | Criar, consultar, editar e inativar |
| Catálogo | Gerenciar catálogo e preços | Consultar e usar preços permitidos |
| Estoque | Gerenciar operações | Consultar e registrar operações permitidas |
| Pedidos | Criar, confirmar e cancelar conforme regras | Criar e consultar; confirmar quando permitido |
| Contas a receber e pagamentos | Consultar e gerenciar conforme regras | Registrar pagamentos permitidos; detalhes por validar |
| Custos, margens e lucros | Acesso conforme configuração administrativa | Sem acesso |

## Ponto que exige validação

Os textos preservados divergem sobre se `OPERATOR` pode criar ou editar produtos e categorias, e sobre quais movimentos de estoque ou pagamentos pode registrar. Até essa divergência ser resolvida, a tabela é uma síntese dos documentos, não uma matriz de autorização pronta para implementação. Veja [questões em aberto](../requirements/open-questions.md#permissões-do-papel-operator).