# Autenticação e autorização

## Escolha registrada

**OAuth 2.0 foi escolhido como framework/protocolo de autorização em alto nível.** A escolha não define, por si só, um login de pessoas, provedor de identidade ou implementação completa. O registro formal está em [ADR-004](../architecture/decisions/ADR-004-oauth2.md).

## O que essa escolha não define

Ainda não foram definidos o provedor, o tipo de cliente, o fluxo OAuth, a forma de representar identidade, o uso de OpenID Connect (OIDC), os scopes, a emissão e o ciclo de vida de tokens, cookies ou sessões, logout, renovação, armazenamento no navegador, recuperação de acesso, convite de usuários nem URL de retorno.

OAuth 2.0 (RFC 6749) trata de autorização de acesso. Quando o produto precisa autenticar uma pessoa por uma identidade interoperável, OIDC é uma especificação que acrescenta uma camada de identidade sobre OAuth 2.0. **A adoção de OIDC no Cosmetics Hub ainda não está decidida.**

## Capacidades de produto documentadas

O produto deve identificar quem está fazendo uma operação, limitar a pessoa às empresas às quais está associada, aplicar o papel dentro da empresa ativa e permitir encerrar o acesso. O backend é responsável por autenticação, autorização e isolamento; a interface pode orientar, mas não é uma fronteira de segurança.

A especificação antiga de email/senha, `password_hash`, sessão e cookie `HttpOnly` foi tratada como hipótese histórica e **não** é requisito vigente após a escolha de OAuth 2.0. Nenhum fluxo de autenticação está implementado no código atual.

## Próxima especificação necessária

A [Spec 001](../specs/001-auth-tenants-customers.md) e as [questões em aberto](open-questions.md#oauth-20-e-identidade) devem ser atualizadas quando o responsável pelo produto confirmar se o caso é autorização para uma API, login federado, ou ambos. Só então devem ser decididos os detalhes de clientes, tokens, sessão e configuração de segurança.

## Referências normativas

- [RFC 6749 — The OAuth 2.0 Authorization Framework](https://www.rfc-editor.org/rfc/rfc6749.html)
- [RFC 9700 — Best Current Practice for OAuth 2.0 Security](https://www.rfc-editor.org/rfc/rfc9700.html)
- [OpenID Connect Core 1.0](https://openid.net/specs/openid-connect-core-1_0.html)