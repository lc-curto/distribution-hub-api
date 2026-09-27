# Estado atual do projeto

**Verificado em:** 27 de setembro de 2026. Este registro descreve o conteúdo versionado nos dois repositórios nessa data.

## Repositórios

| Repositório | Conteúdo | Estado |
|---|---|---|
| [cosmetics-hub-api](https://github.com/lc-curto/cosmetics-hub-api) | API FastAPI, configuração local e documentação comum | Privado; branch principal `main` |
| [cosmetics-hub-web](https://github.com/lc-curto/cosmetics-hub-web) | Scaffold React, TypeScript e Vite | Privado; branch principal `main` |

São **dois repositórios**, não três. A documentação do produto e o contrato da API ficam junto ao repositório da API; não há um repositório separado de documentação.

## Implementação confirmada

| Área | O que existe no repositório | O que ainda não existe |
|---|---|---|
| API | Aplicação FastAPI e `GET /health`, que responde `{"status":"ok"}` | Endpoints de autenticação, empresas, clientes ou outras áreas comerciais |
| Web | Aplicação React/TypeScript/Vite com página de scaffold | Fluxos e telas funcionais de produto |
| Banco local | Serviço PostgreSQL 16 em Docker Compose | Modelos de domínio, schema da aplicação, migrations ou dados de negócio |
| Testes | Teste automatizado do endpoint `/health` | Testes de regras comerciais, autorização, isolamento por empresa ou fluxos ponta a ponta |
| CI | GitHub Actions instala dependências e executa o teste da API e o build web, em seus respectivos repositórios | Pipeline de integração entre aplicações ou testes de contrato |
| Documentação | Fundamentos e especificações listados neste diretório | Sincronização automática do contrato OpenAPI com um cliente web |

Dependências de banco ou autenticação presentes nos arquivos de configuração não significam, por si só, que esses fluxos estejam implementados.

## Escopo documentado, ainda não implementado

Autenticação e autorização, empresas e papéis, clientes, catálogo e preços, estoque, pedidos, contas a receber e dashboard aparecem nos requisitos e regras de negócio. **Nenhuma dessas áreas comerciais está implementada no código atual.** Consulte [escopo do produto](product/scope.md) e [requisitos](requirements/functional-requirements.md).

## Atualização deste registro

Revise esta página quando um comportamento descrito passar a existir no código e tiver validação adequada. Não marque uma capacidade como implementada apenas porque existe uma pasta, dependência, requisito ou diagrama.