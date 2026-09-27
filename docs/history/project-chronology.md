# Histórico do projeto

Esta página registra fatos verificáveis sobre a evolução da estrutura e da documentação. Não é um cronograma nem uma lista de entregas futuras.

## 27 de setembro de 2026 — Separação dos repositórios

O antigo repositório `cosmetics-hub` foi renomeado para [`cosmetics-hub-api`](https://github.com/lc-curto/cosmetics-hub-api). O frontend passou a ter seu repositório privado próprio, [`cosmetics-hub-web`](https://github.com/lc-curto/cosmetics-hub-web). A organização publicada ficou em exatamente dois repositórios, com a documentação comum no repositório da API.

A separação preservou o scaffold já existente: a API continua com `GET /health` e seu teste; a aplicação React continua como scaffold. Não foram implementados fluxos comerciais como parte da separação.

## 27 de setembro de 2026 — Documentação consolidada

Os documentos de produto, domínio, regras, requisitos, especificação de autenticação, modelo de dados e decisões foram organizados em pastas temáticas no repositório da API. As descrições foram alinhadas ao estado real do código. OAuth 2.0 ficou registrado como escolha de alto nível, sem inventar provedor, fluxo, token, cookie ou login local.

## Referência atual

Use [estado atual](../project-status.md) para saber o que existe no código e [índice documental](../README.md) para encontrar requisitos e decisões vigentes. Planos antigos que mencionam um monorepo ou caminhos `apps/api` e `apps/web` não descrevem mais a organização atual.