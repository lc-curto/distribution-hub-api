# Cosmetics Hub — Cronologia de Implementação

> Roteiro cronológico do projeto. Não está organizado por dias ou semanas. Você avança de um ponto para o seguinte quando os critérios de conclusão forem cumpridos.

## Legenda das etiquetas

- `[DOC]` documentação, requisitos e especificação
- `[BD]` base de dados, modelo, SQL e migrations
- `[BE]` backend FastAPI, regras, serviços, repositories e endpoints
- `[FE]` frontend React, telas, componentes e integração visual
- `[QA]` testes, validação e qualidade
- `[INFRA]` ambiente, Docker, CI/CD e deploy
- `[MOBILE]` aplicação React Native/Expo
- `[PORTFÓLIO]` README, apresentação e demonstração

> Quando uma tarefa envolver mais de uma área, ela recebe a etiqueta da área principal. A implementação de cada funcionalidade continua seguindo: `[DOC] → [BD] → [BE] → [FE] → [QA]`.

## Decisões já definidas

Estas decisões não precisam ser reavaliadas a cada etapa, salvo se surgir uma razão técnica forte e documentada.

### Produto

- **Nome:** Cosmetics Hub.
- **Tipo:** MVP de um SaaS de gestão comercial para distribuidores/empresas de cosméticos.
- **Objetivo:** gerir empresas, utilizadores, clientes, catálogo, pedidos, estoque e contas a receber num fluxo integrado.
- **Prioridade:** concluir primeiro um MVP web completo, sem tentar reconstruir todos os módulos do sistema original.

### Stack

- **Frontend web:** React + TypeScript + Vite.
- **Backend:** FastAPI + Python.
- **Banco de dados:** PostgreSQL.
- **Persistência:** SQLAlchemy 2 + Alembic.
- **Validação da API:** Pydantic/FastAPI.
- **Mobile:** React Native + Expo, numa etapa posterior.
- **Testes:** Pytest, Vitest/Testing Library e Playwright.
- **Ambiente:** Docker Compose.
- **CI/CD:** GitHub Actions.

### Arquitetura

- **Estilo:** monólito modular, não microserviços.
- **Frontend:** organização por features/domínios.
- **Backend:** módulos de negócio com router, schemas, service/use cases e repository.
- **Banco:** PostgreSQL como fonte principal de verdade.
- **Mobile:** aplicação separada da web, consumindo a mesma API FastAPI.
- **Desenvolvimento:** Spec-Driven Development incremental.

### Monorepo

```text
cosmetics-hub/
├── apps/api/          # FastAPI + Python
├── apps/web/          # React + TypeScript + Vite
├── apps/mobile/       # React Native + Expo, etapa posterior
├── packages/contracts/
├── database/
├── docs/
└── .github/workflows/
```

### Ordem de desenvolvimento

```text
Documentação
→ Banco de dados
→ Backend
→ Frontend
→ Testes
→ Revisão
→ Próxima funcionalidade
```

A ordem é aplicada **por fatia vertical**, e não como três grandes fases isoladas. Não será desenvolvido todo o banco, depois todo o backend e só depois todo o frontend.

### Papel da revisão

- A implementação será feita pelo estudante.
- A revisão técnica será feita após cada spec, modelo de dados ou incremento relevante.
- Não avançar para a migration sem revisar o modelo correspondente.
- Não considerar uma funcionalidade concluída sem testes e validação do fluxo.

## Estado inicial já concluído

- [x] `[INFRA]` Repositório privado `lc-curto/cosmetics-hub` criado no GitHub
- [x] `[INFRA]` Monorepo inicial criado
- [x] `[INFRA]` Scaffold de `apps/api`, `apps/web`, `apps/mobile` e `packages/contracts` criado
- [x] `[INFRA]` PostgreSQL configurado no Docker Compose
- [x] `[BE]` API FastAPI inicial criada
- [x] `[BE]` Endpoint `/health` criado
- [x] `[QA]` Teste inicial da API aprovado
- [x] `[FE]` Frontend React + TypeScript + Vite inicial criado
- [x] `[QA]` Build inicial do frontend aprovado
- [x] `[DOC]` Visão, escopo, arquitetura e ADRs iniciais documentados
- [x] `[DOC]` Primeira spec Auth + Tenants + Customers criada
- [x] `[INFRA]` CI inicial com GitHub Actions criada

> O que está concluído é apenas a fundação. Auth, tenants, clientes, banco real, migrations e os restantes módulos ainda precisam ser implementados.

## Regra geral de cada funcionalidade

Para cada módulo, siga esta sequência:

```text
1. Especificar o comportamento
2. Definir regras de negócio
3. Modelar ou ajustar o banco
4. Criar a migration
5. Implementar schemas e validações
6. Implementar repository
7. Implementar service/use case
8. Implementar router/endpoints
9. Criar testes da API
10. Criar a interface React
11. Integrar frontend e backend
12. Testar o fluxo completo
13. Atualizar a documentação
14. Fazer commit
15. Solicitar revisão
```

---

# Ponto 0 — Definir o produto

## Fazer

- [x] `[DOC]` Definir o nome do projeto: Cosmetics Hub
- [x] `[DOC]` Definir o problema que o sistema resolve
- [x] `[DOC]` Definir o público-alvo
- [x] `[DOC]` Definir o objetivo do MVP
- [x] `[DOC]` Definir o fluxo principal do negócio
- [x] `[DOC]` Definir os módulos incluídos
- [x] `[DOC]` Definir o que ficará fora do MVP
- [x] `[DOC]` Documentar a visão em `docs/product/vision.md`
- [x] `[DOC]` Documentar o escopo em `docs/product/scope.md`

## Fluxo principal que deve orientar o projeto

- [ ] `[DOC]` Utilizador faz login
- [ ] `[DOC]` Utilizador seleciona uma empresa
- [ ] `[DOC]` Utilizador cria um cliente
- [ ] `[DOC]` Utilizador cria um produto
- [ ] `[DOC]` Utilizador registra estoque
- [ ] `[DOC]` Utilizador cria um pedido
- [ ] `[DOC]` Sistema valida o estoque
- [ ] `[DOC]` Sistema confirma o pedido
- [ ] `[DOC]` Sistema movimenta o estoque
- [ ] `[DOC]` Sistema gera um recebível
- [ ] `[DOC]` Utilizador registra um pagamento
- [ ] `[DOC]` Dashboard apresenta os resultados

## Só avançar quando

- [ ] `[DOC]` O MVP estiver claramente delimitado
- [ ] `[DOC]` O fluxo principal estiver compreendido
- [ ] `[DOC]` As funcionalidades fora do escopo estiverem registradas
- [ ] `[DOC]` A documentação inicial estiver publicada no Git

---

# Ponto 1 — Definir requisitos e regras de negócio

## Fazer

- [ ] `[DOC]` Identificar os atores do sistema
- [ ] `[DOC]` Definir os papéis iniciais: `ADMIN` e `OPERATOR`
- [ ] `[DOC]` Definir o que um utilizador autenticado pode fazer
- [ ] `[DOC]` Definir o que é uma empresa/tenant
- [ ] `[DOC]` Definir o isolamento entre empresas
- [ ] `[DOC]` Definir regras de clientes
- [ ] `[DOC]` Definir regras de produtos e preços
- [ ] `[DOC]` Definir regras de estoque
- [ ] `[DOC]` Definir regras de pedidos
- [ ] `[DOC]` Definir regras de recebíveis
- [x] `[DOC]` Definir requisitos funcionais
- [x] `[DOC]` Definir requisitos não funcionais
- [ ] `[DOC]` Definir critérios de aceitação da primeira fatia
- [x] `[DOC]` Atualizar `docs/specs/001-auth-tenants-customers.md`

## Primeira spec

A primeira spec deve cobrir:

```text
Auth + Tenants + Customers
```

Ela deve responder:

- [ ] `[DOC]` Quem pode fazer login?
- [ ] `[DOC]` Como o login funciona?
- [ ] `[DOC]` Como o utilizador escolhe a empresa?
- [ ] `[DOC]` Como se valida a associação à empresa?
- [ ] `[DOC]` Como um cliente é criado?
- [ ] `[DOC]` Como impedir que uma empresa veja clientes de outra?
- [ ] `[DOC]` Quais erros podem ocorrer?
- [ ] `[DOC]` Como saberemos que a funcionalidade está concluída?

## Só avançar quando

- [ ] `[DOC]` A primeira spec estiver completa
- [ ] `[DOC]` As regras não dependerem de suposições não documentadas
- [ ] `[DOC]` Os critérios de aceitação estiverem definidos
- [ ] `[DOC]` A spec tiver sido revisada

---

# Ponto 2 — Modelar o domínio e o banco inicial

## Entidades da primeira versão

- [ ] `[BD]` `users`
- [ ] `[BD]` `tenants`
- [ ] `[BD]` `tenant_users`
- [ ] `[BD]` `roles`
- [ ] `[BD]` `customers`

## Fazer

- [ ] `[BD]` Definir os campos de cada entidade
- [ ] `[BD]` Definir chaves primárias
- [ ] `[BD]` Definir foreign keys
- [ ] `[BD]` Definir cardinalidades
- [ ] `[BD]` Definir campos obrigatórios
- [ ] `[BD]` Definir campos opcionais
- [ ] `[BD]` Definir timestamps
- [ ] `[BD]` Definir estados
- [ ] `[BD]` Definir regras de unicidade
- [ ] `[BD]` Definir índices iniciais
- [ ] `[BD]` Adicionar `tenant_id` onde necessário
- [ ] `[BD]` Criar diagrama entidade-relacionamento
- [ ] `[BD]` Criar dicionário de dados
- [ ] `[BD]` Documentar o modelo em `docs/database/data-model.md`
- [ ] `[BD]` Validar o modelo contra a primeira spec
- [ ] `[BD]` Pedir revisão do modelo

## Regras iniciais do banco

- [ ] `[BD]` Valores monetários não usam `float`
- [ ] `[BD]` Relacionamentos importantes têm foreign keys
- [ ] `[BD]` Dados de negócio pertencem a um tenant
- [ ] `[BD]` Unicidades são definidas no banco quando aplicável
- [ ] `[BD]` Campos obrigatórios são protegidos por `NOT NULL`
- [ ] `[BD]` Estados inválidos são impedidos
- [ ] `[BD]` O banco consegue representar um utilizador associado a várias empresas

## Só avançar quando

- [ ] `[BD]` O diagrama estiver coerente com os requisitos
- [ ] `[BD]` O dicionário de dados estiver preenchido
- [ ] `[BD]` O isolamento por tenant estiver representado
- [ ] `[BD]` O modelo tiver sido revisado

---

# Ponto 3 — Preparar a infraestrutura técnica

## Fazer

- [ ] `[INFRA]` Configurar PostgreSQL no Docker Compose
- [ ] `[INFRA]` Configurar variáveis de ambiente
- [ ] `[INFRA]` Configurar SQLAlchemy
- [ ] `[INFRA]` Configurar Alembic
- [ ] `[INFRA]` Configurar FastAPI
- [ ] `[INFRA]` Configurar React + TypeScript + Vite
- [ ] `[INFRA]` Configurar React Router
- [ ] `[INFRA]` Configurar TanStack Query
- [ ] `[INFRA]` Configurar React Hook Form
- [ ] `[INFRA]` Configurar validação no frontend
- [ ] `[INFRA]` Configurar Pytest
- [ ] `[INFRA]` Configurar Vitest
- [ ] `[INFRA]` Configurar Playwright para a fase E2E
- [ ] `[INFRA]` Configurar lint e formatter
- [ ] `[INFRA]` Configurar GitHub Actions
- [ ] `[INFRA]` Criar endpoint `/health`
- [ ] `[INFRA]` Criar teste do endpoint `/health`
- [ ] `[INFRA]` Confirmar que o frontend faz build
- [ ] `[INFRA]` Confirmar que a API inicia
- [ ] `[INFRA]` Confirmar que o banco inicia

## Só avançar quando

- [ ] `[INFRA]` Banco, API e frontend iniciam localmente
- [ ] `[INFRA]` O health check responde
- [ ] `[INFRA]` O teste inicial passa
- [ ] `[INFRA]` O build inicial passa
- [ ] `[INFRA]` O CI está configurado

---

# Ponto 4 — Criar migrations e dados de desenvolvimento

## Fazer

- [ ] `[BD]` Criar migration de `users`
- [ ] `[BD]` Criar migration de `tenants`
- [ ] `[BD]` Criar migration de `tenant_users`
- [ ] `[BD]` Criar migration de `roles`
- [ ] `[BD]` Criar migration de `customers`
- [ ] `[BD]` Executar as migrations num banco vazio
- [ ] `[BD]` Reverter as migrations
- [ ] `[BD]` Executar novamente as migrations
- [ ] `[BD]` Criar seed de desenvolvimento
- [ ] `[BD]` Criar utilizador demo
- [ ] `[BD]` Criar empresa demo
- [ ] `[BD]` Associar o utilizador à empresa demo
- [ ] `[BD]` Criar dados iniciais apenas se forem necessários
- [ ] `[BD]` Testar constraints diretamente no PostgreSQL
- [ ] `[BD]` Atualizar o diagrama com o schema real

## Só avançar quando

- [ ] `[BD]` O banco é criado do zero através das migrations
- [ ] `[BD]` As migrations podem ser revertidas
- [ ] `[BD]` O seed funciona
- [ ] `[BD]` As foreign keys funcionam
- [ ] `[BD]` Os dados demo podem ser recriados

---

# Ponto 5 — Implementar Auth

## Backend

- [ ] `[BE]` Criar módulo `auth`
- [ ] `[BE]` Criar módulo `users`
- [ ] `[BE]` Implementar hash seguro de senha
- [ ] `[BE]` Implementar criação de utilizador
- [ ] `[BE]` Implementar login
- [ ] `[BE]` Implementar identificação do utilizador atual
- [ ] `[BE]` Implementar logout ou invalidação de sessão
- [ ] `[BE]` Configurar autenticação por cookie HttpOnly ou mecanismo equivalente
- [ ] `[BE]` Configurar segredo por variável de ambiente
- [ ] `[BE]` Padronizar erros de autenticação
- [ ] `[BE]` Impedir retorno de senha nas respostas

## Endpoints

- [ ] `[BE]` `POST /auth/register`
- [ ] `[BE]` `POST /auth/login`
- [ ] `[BE]` `GET /auth/me`
- [ ] `[BE]` `POST /auth/logout`

## Testes

- [ ] `[QA]` Login válido
- [ ] `[QA]` Senha incorreta
- [ ] `[QA]` Utilizador inexistente
- [ ] `[QA]` Utilizador inativo
- [ ] `[QA]` Rota privada sem autenticação
- [ ] `[QA]` Token/sessão inválida
- [ ] `[QA]` Senha não aparece na resposta
- [ ] `[QA]` Senha não é armazenada em texto puro

## Frontend

- [ ] `[FE]` Criar feature `auth`
- [ ] `[FE]` Criar tela de login
- [ ] `[FE]` Criar schema de formulário
- [ ] `[FE]` Criar cliente HTTP
- [ ] `[FE]` Criar gestão da sessão
- [ ] `[FE]` Criar rota protegida
- [ ] `[FE]` Criar logout
- [ ] `[FE]` Criar estados de loading
- [ ] `[FE]` Criar estados de erro
- [ ] `[FE]` Preservar sessão ao atualizar a página

## Só avançar quando

- [ ] `[FE]` O utilizador consegue criar conta ou usar a conta demo
- [ ] `[FE]` O utilizador consegue fazer login
- [ ] `[FE]` Rotas privadas estão protegidas
- [ ] `[FE]` O logout funciona
- [ ] `[FE]` Os testes de autenticação passam

---

# Ponto 6 — Implementar Tenants e autorização básica

## Backend

- [ ] `[BE]` Listar empresas do utilizador autenticado
- [ ] `[BE]` Validar associação utilizador-empresa
- [ ] `[BE]` Selecionar empresa ativa
- [ ] `[BE]` Criar contexto de tenant
- [ ] `[BE]` Criar dependency/guard de tenant
- [ ] `[BE]` Criar papel `ADMIN`
- [ ] `[BE]` Criar papel `OPERATOR`
- [ ] `[BE]` Implementar permissões básicas
- [ ] `[BE]` Impedir acesso a tenant externo
- [ ] `[BE]` Impedir que o cliente envie um `tenant_id` arbitrário para escapar do contexto

## Frontend

- [ ] `[FE]` Criar tela de seleção de empresa
- [ ] `[FE]` Guardar a empresa ativa
- [ ] `[FE]` Mostrar a empresa ativa no layout
- [ ] `[FE]` Criar navegação protegida por papel
- [ ] `[FE]` Esconder ações não autorizadas
- [ ] `[FE]` Tratar utilizador sem empresa associada

## Testes

- [ ] `[QA]` Utilizador vê apenas empresas associadas
- [ ] `[QA]` Utilizador não acessa dados de outro tenant
- [ ] `[QA]` Admin pode realizar ações administrativas
- [ ] `[QA]` Operador não realiza ações proibidas
- [ ] `[QA]` Requisição sem tenant ativo é rejeitada
- [ ] `[QA]` Manipulação manual de parâmetros não quebra o isolamento

## Só avançar quando

- [ ] `[QA]` O login leva à seleção de empresa
- [ ] `[QA]` Uma empresa ativa está disponível nas requisições
- [ ] `[QA]` A API aplica o tenant em todos os recursos
- [ ] `[QA]` Os papéis básicos funcionam
- [ ] `[QA]` O isolamento foi testado de forma explícita

---

# Ponto 7 — Implementar Customers

## Banco

- [ ] `[BD]` Criar migration de `customers`
- [ ] `[BD]` Confirmar `tenant_id`
- [ ] `[BD]` Confirmar nome obrigatório
- [ ] `[BD]` Adicionar email opcional
- [ ] `[BD]` Adicionar telefone opcional
- [ ] `[BD]` Adicionar identificação fiscal opcional
- [ ] `[BD]` Adicionar `is_active`
- [ ] `[BD]` Adicionar timestamps
- [ ] `[BD]` Criar índices de pesquisa

## Backend

- [ ] `[BE]` Criar schemas Pydantic
- [ ] `[BE]` Criar repository
- [ ] `[BE]` Criar service/use cases
- [ ] `[BE]` Criar router
- [ ] `[BE]` Criar paginação
- [ ] `[BE]` Criar busca
- [ ] `[BE]` Criar filtros
- [ ] `[BE]` Criar ordenação
- [ ] `[BE]` Aplicar tenant ativo
- [ ] `[BE]` Aplicar permissões

## Endpoints

- [ ] `[BE]` `POST /customers`
- [ ] `[BE]` `GET /customers`
- [ ] `[BE]` `GET /customers/{id}`
- [ ] `[BE]` `PATCH /customers/{id}`
- [ ] `[BE]` `DELETE /customers/{id}` ou desativação

## Frontend

- [ ] `[FE]` Criar feature `customers`
- [ ] `[FE]` Criar tabela
- [ ] `[FE]` Criar formulário
- [ ] `[FE]` Criar busca
- [ ] `[FE]` Criar paginação
- [ ] `[FE]` Criar edição
- [ ] `[FE]` Criar ativação/desativação
- [ ] `[FE]` Criar loading state
- [ ] `[FE]` Criar error state
- [ ] `[FE]` Criar estado vazio

## Testes

- [ ] `[QA]` Criar cliente válido
- [ ] `[QA]` Rejeitar nome vazio
- [ ] `[QA]` Rejeitar email inválido
- [ ] `[QA]` Consultar cliente existente
- [ ] `[QA]` Tratar cliente inexistente
- [ ] `[QA]` Pesquisar clientes
- [ ] `[QA]` Paginar clientes
- [ ] `[QA]` Validar isolamento entre tenants
- [ ] `[QA]` Executar fluxo no navegador

## Só avançar quando

- [ ] `[QA]` É possível criar cliente
- [ ] `[QA]` É possível listar cliente
- [ ] `[QA]` É possível pesquisar cliente
- [ ] `[QA]` É possível editar cliente
- [ ] `[QA]` É possível desativar cliente
- [ ] `[QA]` Clientes de outros tenants nunca aparecem
- [ ] `[QA]` A primeira fatia completa está documentada e revisada

---

# Ponto 8 — Implementar Catalog

## Banco

- [ ] `[BD]` Criar `categories`
- [ ] `[BD]` Criar `products`
- [ ] `[BD]` Criar `price_groups`
- [ ] `[BD]` Criar `product_prices`
- [ ] `[BD]` Definir preço como decimal
- [ ] `[BD]` Definir estoque mínimo
- [ ] `[BD]` Definir estado ativo/inativo
- [ ] `[BD]` Criar foreign keys
- [ ] `[BD]` Criar índices
- [ ] `[BD]` Criar migrations

## Backend

- [ ] `[BE]` Criar CRUD de categorias
- [ ] `[BE]` Criar CRUD de produtos
- [ ] `[BE]` Criar grupo de preço padrão
- [ ] `[BE]` Criar preço por grupo
- [ ] `[BE]` Filtrar produtos por categoria
- [ ] `[BE]` Filtrar produtos ativos
- [ ] `[BE]` Validar preço não negativo
- [ ] `[BE]` Aplicar tenant ativo
- [ ] `[BE]` Aplicar permissões

## Frontend

- [ ] `[FE]` Criar feature `catalog`
- [ ] `[FE]` Listar produtos
- [ ] `[FE]` Criar produto
- [ ] `[FE]` Editar produto
- [ ] `[FE]` Criar categoria
- [ ] `[FE]` Definir preço
- [ ] `[FE]` Definir estoque mínimo
- [ ] `[FE]` Ativar/desativar produto
- [ ] `[FE]` Filtrar por categoria

## Testes

- [ ] `[QA]` Criar categoria
- [ ] `[QA]` Criar produto
- [ ] `[QA]` Rejeitar preço inválido
- [ ] `[QA]` Filtrar por categoria
- [ ] `[QA]` Rejeitar acesso entre tenants
- [ ] `[QA]` Validar produto inativo

## Só avançar quando

- [ ] `[QA]` Produtos vendáveis podem ser cadastrados
- [ ] `[QA]` Produtos têm preço válido
- [ ] `[QA]` Categorias funcionam
- [ ] `[QA]` O frontend administra produtos
- [ ] `[QA]` Os testes do catálogo passam

---

# Ponto 9 — Implementar Inventory

## Banco

- [ ] `[BD]` Criar `stock_balances`
- [ ] `[BD]` Criar `stock_movements`
- [ ] `[BD]` Definir tipos de movimento
- [ ] `[BD]` Definir quantidade
- [ ] `[BD]` Associar movimento ao produto
- [ ] `[BD]` Associar movimento ao utilizador
- [ ] `[BD]` Associar movimento ao tenant
- [ ] `[BD]` Criar índices por produto e data
- [ ] `[BD]` Criar migrations

## Backend

- [ ] `[BE]` Implementar saldo inicial
- [ ] `[BE]` Implementar entrada
- [ ] `[BE]` Implementar saída
- [ ] `[BE]` Implementar ajuste
- [ ] `[BE]` Implementar consulta de saldo
- [ ] `[BE]` Implementar histórico
- [ ] `[BE]` Exigir justificativa no ajuste
- [ ] `[BE]` Impedir estoque negativo
- [ ] `[BE]` Garantir transação
- [ ] `[BE]` Implementar alerta de estoque baixo

## Frontend

- [ ] `[FE]` Criar feature `inventory`
- [ ] `[FE]` Listar saldos
- [ ] `[FE]` Criar entrada
- [ ] `[FE]` Criar saída
- [ ] `[FE]` Criar ajuste
- [ ] `[FE]` Mostrar histórico
- [ ] `[FE]` Mostrar alerta de estoque baixo
- [ ] `[FE]` Mostrar justificativa

## Testes

- [ ] `[QA]` Registrar entrada
- [ ] `[QA]` Registrar saída
- [ ] `[QA]` Registrar ajuste
- [ ] `[QA]` Rejeitar estoque negativo
- [ ] `[QA]` Exigir motivo no ajuste
- [ ] `[QA]` Confirmar que toda alteração gera movimento
- [ ] `[QA]` Confirmar isolamento por tenant
- [ ] `[QA]` Testar transação

## Só avançar quando

- [ ] `[QA]` É possível cadastrar estoque inicial
- [ ] `[QA]` Entradas funcionam
- [ ] `[QA]` Saídas funcionam
- [ ] `[QA]` Ajustes funcionam
- [ ] `[QA]` O histórico é auditável
- [ ] `[QA]` O sistema impede saldo negativo

---

# Ponto 10 — Implementar Orders

## Banco

- [ ] `[BD]` Criar `orders`
- [ ] `[BD]` Criar `order_items`
- [ ] `[BD]` Criar `order_status_history`
- [ ] `[BD]` Definir estados `DRAFT`, `CONFIRMED` e `CANCELLED`
- [ ] `[BD]` Definir subtotal
- [ ] `[BD]` Definir desconto
- [ ] `[BD]` Definir total
- [ ] `[BD]` Criar foreign keys
- [ ] `[BD]` Criar índices
- [ ] `[BD]` Criar migrations

## Rascunho

- [ ] `[BD]` Criar pedido em rascunho
- [ ] `[BD]` Selecionar cliente
- [ ] `[BD]` Adicionar item
- [ ] `[BD]` Remover item
- [ ] `[BD]` Alterar quantidade
- [ ] `[BD]` Calcular subtotal
- [ ] `[BD]` Aplicar desconto
- [ ] `[BD]` Calcular total
- [ ] `[BD]` Garantir que rascunho não movimenta estoque

## Confirmação

- [ ] `[BD]` Validar que pedido está em `DRAFT`
- [ ] `[BD]` Validar produtos ativos
- [ ] `[BD]` Validar preços
- [ ] `[BD]` Validar estoque disponível
- [ ] `[BD]` Iniciar transação
- [ ] `[BD]` Registrar movimentações
- [ ] `[BD]` Atualizar saldos
- [ ] `[BD]` Alterar status
- [ ] `[BD]` Registrar histórico
- [ ] `[BD]` Fazer rollback se uma etapa falhar

## Cancelamento

- [ ] `[BD]` Definir quando um pedido pode ser cancelado
- [ ] `[BD]` Reverter estoque quando aplicável
- [ ] `[BD]` Registrar histórico
- [ ] `[BD]` Definir efeito sobre o recebível

## Frontend

- [ ] `[FE]` Criar feature `orders`
- [ ] `[FE]` Criar formulário de pedido
- [ ] `[FE]` Selecionar cliente
- [ ] `[FE]` Selecionar produto
- [ ] `[FE]` Alterar quantidade
- [ ] `[FE]` Aplicar desconto
- [ ] `[FE]` Mostrar resumo
- [ ] `[FE]` Confirmar pedido
- [ ] `[FE]` Cancelar pedido
- [ ] `[FE]` Mostrar status
- [ ] `[FE]` Mostrar histórico

## Testes

- [ ] `[QA]` Calcular subtotal
- [ ] `[QA]` Calcular desconto
- [ ] `[QA]` Calcular total
- [ ] `[QA]` Rejeitar item inválido
- [ ] `[QA]` Rejeitar produto inativo
- [ ] `[QA]` Rejeitar estoque insuficiente
- [ ] `[QA]` Impedir confirmação duplicada
- [ ] `[QA]` Testar rollback
- [ ] `[QA]` Testar cancelamento
- [ ] `[QA]` Testar isolamento por tenant
- [ ] `[QA]` Testar fluxo E2E do pedido

## Só avançar quando

- [ ] `[QA]` É possível criar um pedido em rascunho
- [ ] `[QA]` É possível confirmar um pedido
- [ ] `[QA]` O estoque é atualizado corretamente
- [ ] `[QA]` O histórico é registrado
- [ ] `[QA]` O rollback funciona
- [ ] `[QA]` O pedido não pode ser confirmado duas vezes

---

# Ponto 11 — Implementar Receivables

## Banco

- [ ] `[BD]` Criar `receivables`
- [ ] `[BD]` Criar `receivable_installments`
- [ ] `[BD]` Criar `payments`
- [ ] `[BD]` Definir valor original
- [ ] `[BD]` Definir saldo
- [ ] `[BD]` Definir vencimento
- [ ] `[BD]` Definir estados
- [ ] `[BD]` Criar foreign keys
- [ ] `[BD]` Criar índices
- [ ] `[BD]` Criar migrations

## Estados

- [ ] `[BD]` `OPEN`
- [ ] `[BD]` `PARTIALLY_PAID`
- [ ] `[BD]` `PAID`
- [ ] `[BD]` `OVERDUE`
- [ ] `[BD]` `CANCELLED`

## Backend

- [ ] `[BE]` Gerar recebível ao confirmar pedido
- [ ] `[BE]` Criar parcelas
- [ ] `[BE]` Listar contas abertas
- [ ] `[BE]` Listar contas vencidas
- [ ] `[BE]` Registrar pagamento
- [ ] `[BE]` Suportar pagamento parcial
- [ ] `[BE]` Atualizar saldo
- [ ] `[BE]` Atualizar status
- [ ] `[BE]` Impedir pagamento acima do saldo
- [ ] `[BE]` Impedir pagamento duplicado
- [ ] `[BE]` Tratar cancelamento de pedido

## Frontend

- [ ] `[FE]` Criar feature `receivables`
- [ ] `[FE]` Listar contas abertas
- [ ] `[FE]` Filtrar por status
- [ ] `[FE]` Filtrar por vencimento
- [ ] `[FE]` Mostrar saldo
- [ ] `[FE]` Registrar pagamento
- [ ] `[FE]` Mostrar pagamentos
- [ ] `[FE]` Mostrar parcelas

## Testes

- [ ] `[QA]` Gerar recebível ao confirmar pedido
- [ ] `[QA]` Registrar pagamento total
- [ ] `[QA]` Registrar pagamento parcial
- [ ] `[QA]` Atualizar saldo corretamente
- [ ] `[QA]` Alterar estado para pago
- [ ] `[QA]` Identificar conta vencida
- [ ] `[QA]` Rejeitar valor acima do saldo
- [ ] `[QA]` Rejeitar pagamento duplicado
- [ ] `[QA]` Validar tenant

## Só avançar quando

- [ ] `[QA]` Pedido confirmado gera recebível
- [ ] `[QA]` Recebível pode ser consultado
- [ ] `[QA]` Pagamento total funciona
- [ ] `[QA]` Pagamento parcial funciona
- [ ] `[QA]` Saldo e status são atualizados
- [ ] `[QA]` Regras financeiras estão testadas

---

# Ponto 12 — Histórico e consultas cruzadas

- [ ] `[DOC]` Mostrar histórico de pedidos do cliente
- [ ] `[DOC]` Mostrar detalhe completo do pedido
- [ ] `[DOC]` Mostrar movimentações de um produto
- [ ] `[DOC]` Mostrar recebíveis de um cliente
- [ ] `[DOC]` Mostrar pagamentos de um pedido
- [ ] `[DOC]` Filtrar pedidos por período
- [ ] `[DOC]` Rever joins
- [ ] `[DOC]` Rever índices
- [ ] `[DOC]` Executar `EXPLAIN ANALYZE` em consultas importantes
- [ ] `[DOC]` Documentar consultas relevantes

## Só avançar quando

- [ ] `[DOC]` Os módulos conseguem ser consultados de forma integrada
- [ ] `[DOC]` As consultas devolvem apenas dados do tenant ativo
- [ ] `[DOC]` A performance básica é aceitável

---

# Ponto 13 — Implementar Dashboard

## Backend

- [ ] `[BE]` Criar módulo `dashboard`
- [ ] `[BE]` Criar resumo geral
- [ ] `[BE]` Criar vendas por período
- [ ] `[BE]` Criar pedidos recentes
- [ ] `[BE]` Criar contas a receber
- [ ] `[BE]` Criar produtos com estoque baixo
- [ ] `[BE]` Aplicar filtros por tenant
- [ ] `[BE]` Aplicar filtros de período
- [ ] `[BE]` Fazer agregações no banco/backend

## Endpoints

- [ ] `[BE]` `GET /dashboard/summary`
- [ ] `[BE]` `GET /dashboard/sales-by-period`
- [ ] `[BE]` `GET /dashboard/recent-orders`
- [ ] `[BE]` `GET /dashboard/low-stock`
- [ ] `[BE]` `GET /dashboard/receivables`

## Frontend

- [ ] `[FE]` Criar feature `dashboard`
- [ ] `[FE]` Criar cards de indicadores
- [ ] `[FE]` Criar gráfico de vendas
- [ ] `[FE]` Criar tabela de pedidos recentes
- [ ] `[FE]` Criar lista de estoque baixo
- [ ] `[FE]` Criar lista de contas vencidas
- [ ] `[FE]` Criar filtro de período
- [ ] `[FE]` Criar loading state
- [ ] `[FE]` Criar error state
- [ ] `[FE]` Criar estado sem dados

## Só avançar quando

- [ ] `[FE]` O dashboard mostra dados reais
- [ ] `[FE]` Os totais correspondem às operações realizadas
- [ ] `[FE]` Os filtros funcionam
- [ ] `[FE]` O dashboard respeita o tenant ativo

---

# Ponto 14 — Consolidar o MVP web

## Segurança

- [ ] `[QA]` Rever autenticação
- [ ] `[QA]` Rever autorização
- [ ] `[QA]` Rever isolamento entre tenants
- [ ] `[QA]` Rever CORS
- [ ] `[QA]` Rever cookies/tokens
- [ ] `[QA]` Rever exposição de dados sensíveis
- [ ] `[QA]` Rever validação de entrada
- [ ] `[QA]` Rever tratamento de exceções
- [ ] `[QA]` Rever permissões dos endpoints

## Qualidade

- [ ] `[QA]` Executar testes unitários
- [ ] `[QA]` Executar testes de integração
- [ ] `[QA]` Executar testes E2E
- [ ] `[QA]` Executar lint
- [ ] `[QA]` Executar formatter
- [ ] `[QA]` Executar build da API
- [ ] `[QA]` Executar build do frontend
- [ ] `[QA]` Corrigir warnings importantes
- [ ] `[QA]` Remover código morto
- [ ] `[QA]` Remover dependências não utilizadas

## Fluxo final do MVP web

- [ ] `[FE]` Fazer login
- [ ] `[FE]` Selecionar empresa
- [ ] `[FE]` Criar cliente
- [ ] `[FE]` Criar produto
- [ ] `[FE]` Registrar estoque
- [ ] `[FE]` Criar pedido
- [ ] `[FE]` Confirmar pedido
- [ ] `[FE]` Verificar baixa do estoque
- [ ] `[FE]` Verificar geração do recebível
- [ ] `[FE]` Registrar pagamento
- [ ] `[FE]` Verificar atualização do dashboard

## Só avançar quando

- [ ] `[FE]` O fluxo completo funciona localmente
- [ ] `[FE]` Os testes principais passam
- [ ] `[FE]` A API está documentada
- [ ] `[FE]` O frontend está responsivo
- [ ] `[FE]` O MVP web pode ser demonstrado sem intervenção manual no banco

---

# Ponto 15 — Implementar a aplicação mobile

> O mobile é outra aplicação, não apenas uma página web responsiva. Ele consome a mesma API do backend.

## Fundação

- [ ] `[MOBILE]` Criar projeto React Native com Expo
- [ ] `[MOBILE]` Configurar TypeScript
- [ ] `[MOBILE]` Configurar navegação
- [ ] `[MOBILE]` Configurar cliente HTTP
- [ ] `[MOBILE]` Configurar armazenamento seguro da sessão
- [ ] `[MOBILE]` Configurar ambiente da API
- [ ] `[MOBILE]` Implementar login
- [ ] `[MOBILE]` Implementar logout
- [ ] `[MOBILE]` Criar tela inicial

## Escopo operacional

- [ ] `[MOBILE]` Consultar clientes
- [ ] `[MOBILE]` Consultar produtos
- [ ] `[MOBILE]` Consultar estoque
- [ ] `[MOBILE]` Criar pedido
- [ ] `[MOBILE]` Consultar pedidos
- [ ] `[MOBILE]` Atualizar estado do pedido, se necessário

## Validação

- [ ] `[QA]` Mobile usa a mesma API FastAPI
- [ ] `[QA]` Mobile respeita autenticação
- [ ] `[QA]` Mobile respeita tenant ativo
- [ ] `[QA]` Mobile respeita permissões
- [ ] `[QA]` Mobile possui loading e error states
- [ ] `[QA]` Mobile funciona no Android
- [ ] `[QA]` Mobile possui instruções no README

## Só avançar quando

- [ ] `[QA]` O mobile consegue autenticar
- [ ] `[QA]` O mobile consulta dados reais da API
- [ ] `[QA]` O mobile cria um pedido válido
- [ ] `[QA]` O mobile não duplica regras de negócio do backend

---

# Ponto 16 — Deploy

## API

- [ ] `[BE]` Criar Dockerfile
- [ ] `[BE]` Configurar variáveis de produção
- [ ] `[BE]` Configurar PostgreSQL de produção
- [ ] `[BE]` Executar migrations de produção
- [ ] `[BE]` Configurar CORS
- [ ] `[BE]` Configurar URL pública
- [ ] `[BE]` Configurar health check
- [ ] `[BE]` Validar logs

## Web

- [ ] `[FE]` Criar build de produção
- [ ] `[FE]` Configurar URL da API
- [ ] `[FE]` Publicar frontend
- [ ] `[FE]` Configurar variáveis de ambiente
- [ ] `[FE]` Validar autenticação em produção
- [ ] `[FE]` Validar rotas protegidas

## Dados demo

- [ ] `[FE]` Criar tenant demo
- [ ] `[FE]` Criar utilizador demo
- [ ] `[FE]` Criar clientes demo
- [ ] `[FE]` Criar produtos demo
- [ ] `[FE]` Criar estoque demo
- [ ] `[FE]` Criar pedidos demo
- [ ] `[FE]` Não usar dados reais
- [ ] `[FE]` Não publicar segredos

## Só avançar quando

- [ ] `[FE]` A aplicação web abre numa URL pública
- [ ] `[FE]` A API responde numa URL pública
- [ ] `[FE]` O banco não está publicamente exposto
- [ ] `[FE]` O fluxo demo completo funciona
- [ ] `[FE]` As migrations de produção foram executadas

---

# Ponto 17 — Preparar o portfólio

## README

- [ ] `[PORTFÓLIO]` Explicar o problema
- [ ] `[PORTFÓLIO]` Explicar o público-alvo
- [ ] `[PORTFÓLIO]` Explicar o MVP
- [ ] `[PORTFÓLIO]` Listar tecnologias
- [ ] `[PORTFÓLIO]` Mostrar arquitetura
- [ ] `[PORTFÓLIO]` Mostrar diagrama ER
- [ ] `[PORTFÓLIO]` Explicar execução local
- [ ] `[PORTFÓLIO]` Adicionar link da demo
- [ ] `[PORTFÓLIO]` Adicionar credenciais demo
- [ ] `[PORTFÓLIO]` Adicionar screenshots
- [ ] `[PORTFÓLIO]` Adicionar limitações
- [ ] `[PORTFÓLIO]` Adicionar próximos passos

## Apresentação

- [ ] `[PORTFÓLIO]` Gravar vídeo de 2–4 minutos
- [ ] `[PORTFÓLIO]` Mostrar login
- [ ] `[PORTFÓLIO]` Mostrar empresa ativa
- [ ] `[PORTFÓLIO]` Mostrar cliente
- [ ] `[PORTFÓLIO]` Mostrar produto
- [ ] `[PORTFÓLIO]` Mostrar estoque
- [ ] `[PORTFÓLIO]` Mostrar pedido
- [ ] `[PORTFÓLIO]` Mostrar recebível
- [ ] `[PORTFÓLIO]` Mostrar pagamento
- [ ] `[PORTFÓLIO]` Mostrar dashboard
- [ ] `[PORTFÓLIO]` Mostrar mobile, se concluído

## Documentação técnica

- [ ] `[PORTFÓLIO]` Diagrama de arquitetura
- [ ] `[PORTFÓLIO]` Diagrama entidade-relacionamento
- [ ] `[PORTFÓLIO]` Fluxo de criação de pedido
- [ ] `[PORTFÓLIO]` Fluxo de confirmação e estoque
- [ ] `[PORTFÓLIO]` Fluxo de pagamento
- [ ] `[PORTFÓLIO]` ADR sobre FastAPI e React
- [ ] `[PORTFÓLIO]` ADR sobre PostgreSQL
- [ ] `[PORTFÓLIO]` ADR sobre monólito modular
- [ ] `[PORTFÓLIO]` Documentação da API
- [ ] `[PORTFÓLIO]` Documentação de segurança

## Só considerar o projeto apresentado quando

- [ ] `[PORTFÓLIO]` A demo funciona
- [ ] `[PORTFÓLIO]` O README explica o projeto sem depender de explicação oral
- [ ] `[PORTFÓLIO]` O código está publicado
- [ ] `[PORTFÓLIO]` O fluxo principal está testado
- [ ] `[PORTFÓLIO]` A arquitetura pode ser explicada numa entrevista
- [ ] `[PORTFÓLIO]` As decisões técnicas estão documentadas

---

# Critério geral de avanço

Nunca avance apenas porque o código foi escrito. Avance quando o ponto atual tiver:

- [ ] `[PORTFÓLIO]` Especificação atualizada
- [ ] `[PORTFÓLIO]` Banco modelado
- [ ] `[PORTFÓLIO]` Migration executada
- [ ] `[PORTFÓLIO]` Backend implementado
- [ ] `[PORTFÓLIO]` Testes da API criados
- [ ] `[PORTFÓLIO]` Frontend integrado
- [ ] `[PORTFÓLIO]` Fluxo manual validado
- [ ] `[PORTFÓLIO]` Documentação atualizada
- [ ] `[PORTFÓLIO]` Commit criado
- [ ] `[PORTFÓLIO]` Revisão concluída

# Próxima ação

- [ ] `[PORTFÓLIO]` Abrir `docs/specs/001-auth-tenants-customers.md`
- [ ] `[PORTFÓLIO]` Revisar a primeira spec
- [ ] `[PORTFÓLIO]` Listar entidades e campos
- [ ] `[PORTFÓLIO]` Criar o diagrama ER inicial
- [ ] `[PORTFÓLIO]` Documentar o dicionário de dados
- [ ] `[PORTFÓLIO]` Enviar spec e modelo para revisão
- [ ] `[PORTFÓLIO]` Só depois criar a primeira migration
