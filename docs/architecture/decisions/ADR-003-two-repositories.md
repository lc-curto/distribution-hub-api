# ADR-003 — Frontend e API em dois repositórios

**Estado:** Aceito e refletido no GitHub
**Data:** 2026-09-27

## Contexto

O projeto precisava separar o frontend e o backend, mantendo a documentação do produto acessível e evitando um terceiro repositório apenas documental.

## Decisão

Manter exatamente dois repositórios privados:

1. [`cosmetics-hub-web`](https://github.com/lc-curto/cosmetics-hub-web) para a aplicação React.
2. [`cosmetics-hub-api`](https://github.com/lc-curto/cosmetics-hub-api) para a API FastAPI e a documentação comum de produto, domínio, requisitos e arquitetura.

O frontend aponta para a documentação e contrato publicados no repositório da API. A fronteira de integração entre os repositórios é a API HTTP, não importação direta de código entre eles.

## Consequências

- Cada aplicação tem histórico, CI e dependências próprios.
- Mudanças da API devem ser documentadas pelo contrato OpenAPI e coordenadas com o frontend.
- Não existe um terceiro repositório de documentação.
- A separação de repositórios não implica microserviços nem autonomia de deploy já configurada.
- A estrutura publicada contém scaffolds; não implementa as áreas comerciais do produto.

## Reavaliação

Reavaliar apenas se a propriedade da documentação ou a organização das aplicações mudar de forma material.
