# Domínio e regras essenciais

> O domínio de negócio abaixo é, em grande parte, especificado e ainda não exposto por endpoints. Os modelos SQLAlchemy `User` e `Tenant` e as migrations de `users` e `tenants` já existem. A associação `tenant_users`, os clientes e os restantes módulos comerciais continuam por implementar.

## Conceitos

- **Usuário:** pessoa que tem ou poderá ter acesso.
- **Empresa:** organização que usa a plataforma e separa seus dados.
- **Associação:** vínculo usuário–empresa que contém papel e estado de acesso.
- **Cliente:** pessoa ou organização atendida comercialmente; não é usuário do sistema neste escopo.

Uma pessoa pode estar em várias empresas e ter papéis diferentes em cada uma.

## Atores e permissões previstas

| Área | `ADMIN` | `OPERATOR` |
|---|---|---|
| Usuários, papéis e configurações | Gerenciar | Sem permissão |
| Clientes | Criar, consultar, editar e inativar | Criar, consultar, editar e inativar |
| Catálogo e preços | Gerenciar | Consultar e usar preços permitidos |
| Estoque | Gerenciar operações | Consultar e registrar operações permitidas |
| Pedidos | Criar, confirmar e cancelar conforme regras | Criar e consultar; confirmação por validar |
| Recebíveis e pagamentos | Gerenciar conforme regras | Registrar operações permitidas |

A matriz ainda não está pronta para implementação: há divergências sobre permissões de `OPERATOR` em produtos, estoque e pagamentos.

## Regras que orientam a implementação

1. O papel pertence à associação com a empresa, não à conta global.
2. O backend aplica autorização e isolamento; a interface não é uma barreira de segurança.
3. Toda operação protegida ocorre em empresa ativa e autorizada.
4. Uma empresa mantém pelo menos um `ADMIN` ativo.
5. O último `ADMIN` não pode ser removido nem rebaixado.
6. Clientes pertencem a uma empresa, são inativados em vez de apagados e não podem entrar em novos pedidos quando inativos.
7. Pedidos confirmados validam cliente, produtos, preços e estoque atomicamente.
8. Operações relevantes preservam autor, empresa, data e contexto para auditoria.

Catálogo, estoque, pedidos, recebíveis e indicadores ainda não têm implementação. Questões pendentes e requisitos verificáveis estão em [requisitos](requirements.md).