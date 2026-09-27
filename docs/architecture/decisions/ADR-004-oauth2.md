# ADR-004 — OAuth 2.0 como framework de autorização

**Estado:** Aceito no nível de framework/protocolo; desenho de autenticação pendente
**Data:** 2026-09-27

## Contexto

O Cosmetics Hub precisa identificar usuários, aplicar permissões por empresa e proteger dados comerciais. A escolha comunicada para autenticação foi OAuth 2.0. A especificação antiga também mencionava email/senha, `password_hash`, sessão e cookie, mas esses detalhes não foram conciliados com a escolha e não são considerados vigentes.

## Decisão

Adotar **OAuth 2.0** como framework/protocolo de autorização. Esta decisão não define provedor, tipo de cliente, fluxo, scopes, token, cookie, sessão ou forma de login.

OAuth 2.0, isoladamente, não define uma identidade interoperável para login de pessoas. Se o produto precisar de login federado, o uso de **OpenID Connect (OIDC)** deve ser avaliado e explicitamente decidido. Não se presume que OIDC já tenha sido adotado.

## Consequências

- Os requisitos funcionais descrevem identidade e acesso sem impor credenciais locais.
- Não se deve implementar fluxo de autenticação antes de definir o caso de uso, cliente e provedor.
- A autorização por empresa e papel continua responsabilidade do backend, independentemente do provedor.
- O desenho deve seguir as práticas de segurança atuais, incluindo [RFC 9700](https://www.rfc-editor.org/rfc/rfc9700.html).
- No código atual não há autenticação implementada.

## Questões pendentes

Definir se OAuth 2.0 será usado para autorização de API, login federado ou ambos; decidir sobre OIDC e provedor; especificar clientes, tokens, logout, renovação, armazenamento e fluxo de onboarding. As perguntas estão em [questões em aberto](../../requirements/open-questions.md#oauth-20-e-identidade).
