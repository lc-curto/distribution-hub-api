# Spec 001 — Acesso, empresas e clientes

**Estado:** especificação documentada; fluxo não implementado. OAuth 2.0 ainda não tem desenho técnico fechado.

## Objetivo

Permitir que uma pessoa autorizada opere no contexto de uma empresa e mantenha clientes comerciais sem acesso cruzado entre empresas.

## Escopo

Identidade autenticada, associação usuário–empresa, empresa ativa, papéis `ADMIN` e `OPERATOR`, isolamento e manutenção de clientes. Regras gerais estão em [domínio](../domain.md) e pendências em [requisitos](../requirements.md).

## Fluxo de entrada

1. A pessoa estabelece identidade por mecanismo compatível com OAuth 2.0; provedor, OIDC e fluxo ainda não estão definidos.
2. A API identifica o usuário local e lista somente empresas associadas.
3. Uma empresa pode ser selecionada automaticamente se houver apenas uma; caso contrário, a pessoa escolhe a ativa.
4. Antes de cada operação, o backend valida identidade, associação, empresa ativa, papel e permissão.
5. Pessoa sem associação não acessa áreas operacionais.

O fluxo não define cabeçalho, cookie, sessão ou formato de token.

## Fluxo de clientes

Usuário autorizado pode criar, consultar, pesquisar, editar e inativar clientes da empresa ativa. Cliente inativo permanece no histórico, não pode ser usado em novo pedido e não é apagado fisicamente. Outra empresa não pode ler nem alterar seus dados.

## Critérios de aceitação

- Requisição sem identidade válida não acessa dados privados.
- O usuário recebe apenas suas empresas.
- A API recusa operações para empresa não associada.
- O papel é avaliado dentro da empresa ativa.
- Usuário autorizado mantém clientes da própria empresa.
- Usuário de outra empresa não acessa o cliente.
- Cliente inativo não entra em novo pedido.
- O último `ADMIN` ativo não pode ser removido ou rebaixado.
- Falhas no onboarding não deixam registros parciais, se esse fluxo for aprovado.

Todos os critérios estão pendentes de implementação e teste.

## Fora do escopo

Detalhes de OAuth/OIDC, convites, recuperação de acesso, políticas de senha, tokens/cookies, campos finais, importação em lote e rotinas administrativas de recuperação do último `ADMIN`.
