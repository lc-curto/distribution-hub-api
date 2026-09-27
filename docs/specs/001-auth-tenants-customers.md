# Spec 001 — Acesso, empresas e clientes

**Estado:** especificação documentada; fluxo não implementado. Esta spec descreve o comportamento pretendido sem fechar decisões técnicas de OAuth 2.0 que ainda estão em aberto.

## Objetivo

Permitir que uma pessoa autorizada opere no contexto de uma empresa e que usuários dessa empresa mantenham seus clientes comerciais, sem permitir acesso cruzado entre empresas.

## Escopo

A spec cobre identidade autenticada, associação entre usuário e empresa, escolha da empresa ativa, aplicação dos papéis `ADMIN` e `OPERATOR`, isolamento de dados e operações de consulta e manutenção de clientes. As regras completas estão em [regras de negócio](../requirements/business-rules.md); os atributos propostos estão no [modelo de dados](../database/data-model.md).

## Atores

- **Usuário não autenticado:** ainda não estabeleceu acesso válido.
- **`ADMIN`:** administra a própria empresa e suas operações autorizadas.
- **`OPERATOR`:** realiza operações diárias com permissões mais restritas.
- **Cliente comercial:** registro mantido pela empresa; não é usuário do sistema neste escopo.

## Fluxo de entrada e contexto da empresa

1. A pessoa estabelece identidade por um mecanismo compatível com a decisão de OAuth 2.0. O provedor, o uso de OIDC e o fluxo concreto ainda não estão definidos.
2. A API identifica o usuário local correspondente e lista somente as empresas às quais ele está associado.
3. Se houver uma única empresa, o produto pode selecioná-la automaticamente; se houver mais de uma, a pessoa escolhe uma empresa ativa.
4. Antes de cada operação protegida, o backend valida identidade, associação, empresa ativa, papel e permissão.
5. Uma pessoa sem associação não acessa áreas operacionais. O processo de entrada, criação de empresa ou convite ainda precisa ser validado.

Este fluxo é independente de cabeçalho, cookie, sessão ou formato de token. Esses mecanismos não foram decididos. Ver [autenticação](../requirements/authentication.md) e [questões em aberto](../requirements/open-questions.md).

## Fluxo de clientes

1. Um usuário autorizado acessa clientes no contexto de uma empresa ativa.
2. O sistema permite criar, consultar, pesquisar, editar e inativar clientes de sua própria empresa.
3. Um cliente inativo permanece disponível para consulta histórica, mas não pode ser usado em um novo pedido.
4. Os dados de um cliente não podem ser lidos ou alterados por usuário de outra empresa.
5. A exclusão normal é lógica/inativação; exclusão física não faz parte do fluxo documentado.

## Regras e restrições

- O papel pertence ao vínculo usuário–empresa.
- Cada empresa conserva ao menos um `ADMIN` ativo.
- Não se pode remover nem rebaixar o último administrador ativo.
- O backend é a autoridade para autorização e isolamento; a interface não substitui essas verificações.
- Operações de criação de empresa e vínculo administrativo devem ser atômicas, caso o fluxo seja confirmado.
- OAuth 2.0 foi escolhido em alto nível, mas não confirma login por email/senha, cookie, sessão nem provedor.

## Critérios de aceitação

| ID | Critério verificável |
|---|---|
| AC-001 | Uma requisição sem identidade válida não lê nem altera dados privados. |
| AC-002 | O usuário só recebe a lista de empresas às quais está associado. |
| AC-003 | Uma operação para empresa não associada é recusada pelo backend, mesmo que o cliente envie o identificador dessa empresa. |
| AC-004 | O papel é avaliado dentro da empresa ativa; ser `ADMIN` em uma empresa não concede permissão administrativa em outra. |
| AC-005 | Usuário autorizado cria, consulta, edita e inativa clientes no escopo de sua empresa. |
| AC-006 | Usuário de outra empresa não consegue consultar nem alterar um cliente. |
| AC-007 | Cliente inativo continua disponível no histórico e não pode ser selecionado para um novo pedido. |
| AC-008 | O último `ADMIN` ativo não pode ser removido nem rebaixado. |
| AC-009 | Se a criação de empresa e associação inicial for implementada, falha em qualquer etapa não deixa registros parciais. |

Todos os critérios estão **pendentes de implementação e teste**.

## Fora do escopo desta spec

Esta spec não define detalhes de OAuth/OIDC, convites por email, recuperação de acesso, políticas de senha, formato de token/cookie, cabeçalho de empresa ativa, campos finais do cadastro, importação em lote nem rotinas administrativas de recuperação do último `ADMIN`.

## Questões que bloqueiam implementação segura

Consulte as seções [OAuth 2.0 e identidade](../requirements/open-questions.md#oauth-20-e-identidade), [empresas e permissões](../requirements/open-questions.md#empresas-e-permissões) e [regras comerciais e dados](../requirements/open-questions.md#regras-comerciais-e-dados). Esta spec deve ser atualizada quando essas questões forem respondidas.