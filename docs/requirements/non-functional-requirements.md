# Requisitos não funcionais

Estes requisitos descrevem qualidade, segurança e operação. Foram preservados como necessidades do produto; vários ainda precisam de métrica, critério de aceitação ou validação do responsável pelo produto.

## Segurança e acesso

| ID | Requisito | Situação |
|---|---|---|
| RNF-001 | Nenhuma credencial deve ser armazenada em texto puro. Se o produto vier a armazenar senhas, deve usar hash resistente apropriado. | Especificado; arquitetura de identidade por definir |
| RNF-002 | Recursos privados exigem identidade autenticada válida. | Especificado; não implementado |
| RNF-003 | O backend verifica permissões em toda operação protegida. | Especificado; não implementado |
| RNF-004 | Uma pessoa não lê nem altera dados de outra empresa. Identificadores enviados pela interface não concedem acesso. | Especificado; não implementado |
| RNF-005 | Respostas e erros não expõem credenciais, segredos ou detalhes internos desnecessários. | Especificado; critérios detalhados pendentes |

## Integridade dos dados

| ID | Requisito | Situação |
|---|---|---|
| RNF-010 | PostgreSQL é o banco relacional previsto; o serviço local está configurado no Compose. | Configuração local implementada; schema comercial ausente |
| RNF-011 | Relações importantes são protegidas por integridade referencial e validação. | Especificado; não implementado |
| RNF-012 | Valores monetários não usam ponto flutuante binário; devem ter representação decimal adequada. | Especificado; precisão/moeda por definir |
| RNF-013 | Confirmação de pedido e mudanças de estoque são atômicas. | Especificado; não implementado |
| RNF-014 | Movimentos de estoque, estados de pedido e pagamentos preservam histórico suficiente. | Especificado; política de retenção pendente |
| RNF-015 | Onboarding que cria registros relacionados não deixa dados parciais em caso de falha. | Especificado; fluxo de identidade pendente |
| RNF-016 | A atribuição do primeiro `ADMIN` ocorre no backend, nunca por escolha não confiável da interface. | Especificado; não implementado |

## API e interface

| ID | Requisito | Situação |
|---|---|---|
| RNF-020 | Entradas e respostas usam schemas validados e tipados. | Parcial: FastAPI está presente; contratos comerciais não existem |
| RNF-021 | Erros da API têm formato consistente e não dependem de mensagens internas do banco. | Especificado; não implementado |
| RNF-022 | A API disponibiliza contrato OpenAPI gerado a partir de endpoints. | OpenAPI automático do FastAPI disponível; hoje há somente `/health` |
| RNF-023 | Uma mudança futura da API não quebra clientes sem uma política de versão compatível. | Princípio registrado; política de versionamento por definir |
| RNF-030 | A aplicação web funciona em computador, tablet e celular. | Especificado; ainda não avaliado |
| RNF-031 | As telas tratam carregamento, sucesso, erro e ausência de dados. | Especificado; telas de produto não existem |
| RNF-032 | Formulários, botões, tabelas e mensagens são compreensíveis e acessíveis por meios adequados. | Especificado; critérios e testes pendentes |
| RNF-033 | Validações da interface não substituem autorização no backend. | Princípio documentado; autorização não implementada |

## Testes e manutenção

| ID | Requisito | Situação |
|---|---|---|
| RNF-040 | Regras críticas têm testes, incluindo isolamento, permissões, estoque, confirmação e pagamentos. | Não implementado; existe teste de saúde da API |
| RNF-041 | Fluxos principais têm testes de integração com API e PostgreSQL. | Não implementado |
| RNF-042 | Existe teste ponta a ponta para um fluxo principal do produto. | Não implementado |
| RNF-043 | GitHub Actions valida os repositórios. | Parcialmente implementado: CI executa teste da API e build web separadamente |
| RNF-050 | API organizada por módulos de domínio; frontend organizado por páginas/rotas e pastas partilhadas. | Estrutura de pastas preparada; módulos e páginas comerciais ainda vazios |
| RNF-051 | Regras, requisitos, decisões e instruções ficam documentados e navegáveis. | Documentação organizada neste repositório |
| RNF-052 | Segredos e configurações específicas de ambiente vêm de configuração externa, não do código. | Exemplos/configuração local presentes; política de produção por definir |
| RNF-053 | Alterações de schema são versionadas por migrations. | Alembic/diretório reservado; migrations de domínio ausentes |

## Operação

| ID | Requisito | Situação |
|---|---|---|
| RNF-060 | A API oferece verificação de saúde. | Implementado e coberto por teste: `GET /health` |
| RNF-061 | Um ambiente local pode ser iniciado seguindo README e Docker Compose. | Parcial: PostgreSQL local e scaffold documentados; fluxos de negócio inexistentes |
| RNF-062 | Eventos relevantes são registrados com contexto suficiente sem expor dados sensíveis. | Especificado; observabilidade ainda não implementada |

Alta disponibilidade, recuperação de desastre automatizada, SLA formal, escalabilidade horizontal e observabilidade avançada não têm requisitos definidos para o escopo atual. Não há metas numéricas de desempenho ou disponibilidade; elas devem ser acordadas antes de serem tratadas como requisitos verificáveis.