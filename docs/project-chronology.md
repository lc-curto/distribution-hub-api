**# Cosmetics Hub — Cronologia de Implementação**

\> Roteiro cronológico do projeto. Não está organizado por dias. Você só avança quando o marco atual estiver concluído.

<!-- ============================================================
     CONTEXTO: COMO USAR O DOCUMENTO
     ============================================================ -->

**## Como usar**

Cada marco informa:

\- **\*\*Objetivo:\*\*** o resultado esperado;

\- **\*\*Pré-requisito:\*\*** o que precisa existir antes;

\- **\*\*Tarefas:\*\*** o que fazer, separado por área;

\- **\*\*Entrega:\*\*** arquivos ou funcionalidades que devem existir;

\- **\*\*Avançar quando:\*\*** critério de conclusão;

\- **\*\*Próximo passo:\*\*** o que fazer depois.

<!-- ============================================================
     CONTEXTO: ETIQUETAS DO PROJETO
     ============================================================ -->

**## Etiquetas**

\- \`[DOC]\` documentação e requisitos

\- \`[BD]\` banco de dados, SQL e migrations

\- \`[BE]\` backend FastAPI

\- \`[FE]\` frontend React

\- \`[QA]\` testes e validação

\- \`[INFRA]\` ambiente e deploy

\- \`[MOBILE]\` React Native/Expo

\- \`[PORTFÓLIO]\` apresentação do projeto

<!-- ============================================================
     CONTEXTO: ORDEM DE IMPLEMENTAÇÃO
     ============================================================ -->

**## Ordem de uma funcionalidade**

\`\`\`

spec → modelo BD → migration → backend → testes API → frontend → integração → revisão

\`\`\`

\---

<!-- ============================================================
     MARCO 0 — FUNDAÇÃO E DOCUMENTAÇÃO
     ============================================================ -->

**# Marco 0 — Fundação e documentação**

**## Objetivo**

Ter o projeto criado, executável e documentado antes de iniciar a implementação de negócio.

**## Já concluído**

\- [x] \`[INFRA]\` Repositório privado criado — **\*\*Prova:\*\*** \`https\://github.com/lc-curto/cosmetics-hub\` + \`git remote -v\`

\- [x] \`[INFRA]\` Monorepo criado — **\*\*Prova:\*\*** \`package.json\` + \`pnpm-workspace.yaml\`

\- [x] \`[INFRA]\` \`apps/api\` criado — **\*\*Prova:\*\*** \`apps/api/app/main.py\`

\- [x] \`[INFRA]\` \`apps/web\` criado — **\*\*Prova:\*\*** \`apps/web/src/main.tsx\` + \`apps/web/package.json\`

\- [x] \`[INFRA]\` \`apps/mobile\` reservado para depois — **\*\*Prova:\*\*** \`apps/mobile/README.md\`

\- [x] \`[INFRA]\` PostgreSQL e Docker Compose configurados — **\*\*Prova:\*\*** \`docker-compose.yml\` + \`docker compose config\`

\- [x] \`[BE]\` FastAPI inicial criada — **\*\*Prova:\*\*** \`apps/api/app/main.py\`

\- [x] \`[BE]\` Endpoint \`/health\` criado — **\*\*Prova:\*\*** \`apps/api/app/main.py\` — rota \`/health\`

\- [x] \`[FE]\` React + TypeScript + Vite inicial criado — **\*\*Prova:\*\*** \`apps/web/package.json\` + \`apps/web/vite.config.ts\` + \`apps/web/tsconfig.json\`

\- [x] \`[QA]\` Teste inicial da API aprovado — **\*\*Prova:\*\*** \`apps/api/tests/test_health.py\` + comando \`python -m pytest -q\`

\- [x] \`[QA]\` Build inicial do frontend aprovado — **\*\*Prova:\*\*** \`apps/web/package.json\` + comando \`pnpm --dir apps/web build\`

\- [x] \`[INFRA]\` CI inicial configurado — **\*\*Prova:\*\*** \`.github/workflows/ci.yml\` + GitHub Actions

**## Documentação concluída**

\- [x] \`[DOC]\` Visão e escopo do produto — **\*\*Prova:\*\*** \`docs/product/vision.md\` + \`docs/product/scope.md\`

\- [x] \`[DOC]\` Atores do sistema — **\*\*Prova:\*\*** \`docs/requirements/actors.md\`

\- [x] \`[DOC]\` Papéis \`ADMIN\` e \`OPERATOR\` — **\*\*Prova:\*\*** \`docs/requirements/roles.md\`

\- [x] \`[DOC]\` Ações do utilizador autenticado — **\*\*Prova:\*\*** \`docs/requirements/authenticated-user-actions.md\`

\- [x] \`[DOC]\` Regras de negócio do MVP — **\*\*Prova:\*\*** \`docs/requirements/business-rules-mvp.md\`

\- [x] \`[DOC]\` Regras futuras separadas — **\*\*Prova:\*\*** \`docs/requirements/business-rules-future.md\`

\- [x] \`[DOC]\` Requisitos funcionais — **\*\*Prova:\*\*** \`docs/requirements/functional-requirements.md\`

\- [x] \`[DOC]\` Requisitos não funcionais — **\*\*Prova:\*\*** \`docs/requirements/non-functional-requirements.md\`

\- [x] \`[DOC]\` Spec inicial de Auth, Tenants e Customers — **\*\*Prova:\*\*** \`docs/specs/001-auth-tenants-customers.md\`

**## Estado**

**\*\*Concluído.\*\***

**## Próximo marco**

Modelar o banco da primeira funcionalidade: **\*\*Auth + Tenants + Customers\*\***.

\---

<!-- ============================================================
     MARCO 1 — MODELAR AUTH, TENANTS E CUSTOMERS
     ============================================================ -->

**# Marco 1 — Modelar Auth, Tenants e Customers**

**## Objetivo**

Transformar a primeira spec num modelo de dados revisado.

**## Pré-requisito**

\- [x] \`[DOC]\` Spec \`001-auth-tenants-customers.md\` criada — **\*\*Prova:\*\*** \`docs/specs/001-auth-tenants-customers.md\`

\- [x] \`[DOC]\` Atores e papéis definidos — **\*\*Prova:\*\*** \`docs/requirements/actors.md\` + \`docs/requirements/roles.md\`

\- [x] \`[DOC]\` Regras de isolamento definidas — **\*\*Prova:\*\*** \`docs/requirements/business-rules-mvp.md\` — RN-001 a RN-005

**## Tarefas \`[DOC]\`**

\- [ ] Rever a spec e retirar dúvidas

\- [ ] Definir campos de \`users\`

\- [ ] Definir campos de \`tenants\`

\- [ ] Definir campos de \`tenant_users\`

\- [ ] Definir campos de \`customers\`

\- [ ] Definir campos obrigatórios e opcionais

\- [ ] Definir estados de utilizador, empresa e cliente

\- [ ] Criar \`docs/database/data-model.md\`

\- [ ] Criar o dicionário de dados

**## Tarefas \`[BD]\`**

\- [ ] Definir chaves primárias

\- [ ] Definir foreign keys

\- [ ] Definir cardinalidades

\- [ ] Definir \`tenant_id\` nas entidades de negócio

\- [ ] Definir regras de unicidade

\- [ ] Definir índices iniciais

\- [ ] Criar \`database/diagrams/er-model.mmd\`

\- [ ] Rever o modelo antes da migration

**## Entrega**

\`\`\`

docs/database/data-model.md

database/diagrams/er-model.mmd

\`\`\`

**## Avançar quando**

\- [ ] O mesmo utilizador pode pertencer a várias empresas

\- [ ] O papel fica no vínculo utilizador-empresa

\- [ ] O isolamento por tenant está representado

\- [ ] O modelo está coerente com a spec

\- [ ] O modelo foi revisado

**## Próximo passo**

Criar as migrations do banco no **\*\*Marco 2\*\***.

\---

<!-- ============================================================
     MARCO 2 — MIGRATIONS E DADOS DEMO
     ============================================================ -->

**# Marco 2 — Criar migrations e dados demo**

**## Objetivo**

Criar o banco inicial do zero de forma reproduzível.

**## Pré-requisito**

\- [ ] Modelo do Marco 1 revisado

**## Tarefas \`[BD]\`**

\- [ ] Configurar SQLAlchemy

\- [ ] Configurar Alembic

\- [ ] Criar migration de \`users\`

\- [ ] Criar migration de \`tenants\`

\- [ ] Criar migration de \`tenant_users\`

\- [ ] Criar migration de \`customers\`

\- [ ] Executar migrations num banco vazio

\- [ ] Reverter migrations

\- [ ] Executar migrations novamente

\- [ ] Criar seed de desenvolvimento

\- [ ] Criar utilizador demo

\- [ ] Criar empresa demo

\- [ ] Associar o utilizador à empresa demo

**## Tarefas \`[QA]\`**

\- [ ] Testar foreign keys

\- [ ] Testar constraints

\- [ ] Testar recriação dos dados demo

**## Avançar quando**

\- [ ] O banco é criado apenas com migrations

\- [ ] As migrations podem ser revertidas

\- [ ] O seed funciona

\- [ ] O utilizador e a empresa demo existem

**## Próximo passo**

Implementar autenticação no backend no **\*\*Marco 3\*\***.

\---

<!-- ============================================================
     MARCO 3 — AUTH NO BACKEND
     ============================================================ -->

**# Marco 3 — Auth no backend**

**## Objetivo**

Permitir login seguro através da API.

**## Pré-requisito**

\- [ ] Migrations do Marco 2 concluídas

**## Tarefas \`[BE]\`**

\- [ ] Criar módulo \`auth\`

\- [ ] Criar módulo \`users\`

\- [ ] Implementar hash seguro de palavra-passe

\- [ ] Implementar login

\- [ ] Implementar utilizador atual

\- [ ] Implementar logout/invalidação de sessão

\- [ ] Configurar sessão ou cookie HttpOnly

\- [ ] Configurar segredos por variável de ambiente

\- [ ] Padronizar erros de autenticação

\- [ ] Não retornar palavra-passe nas respostas

**## Endpoints**

\- [ ] \`POST /auth/login\`

\- [ ] \`GET /auth/me\`

\- [ ] \`POST /auth/logout\`

**## Tarefas \`[QA]\`**

\- [ ] Login válido

\- [ ] Palavra-passe incorreta

\- [ ] Utilizador inexistente

\- [ ] Rota privada sem autenticação

\- [ ] Sessão inválida

\- [ ] Palavra-passe armazenada apenas como hash

**## Avançar quando**

\- [ ] Login válido funciona

\- [ ] Login inválido é rejeitado

\- [ ] Rota privada exige autenticação

\- [ ] Testes do backend passam

**## Próximo passo**

Criar login e sessão no frontend no **\*\*Marco 4\*\***.

\---

<!-- ============================================================
     MARCO 4 — AUTH NO FRONTEND
     ============================================================ -->

**# Marco 4 — Auth no frontend**

**## Objetivo**

Permitir login pelo navegador e proteger as telas privadas.

**## Pré-requisito**

\- [ ] Auth do backend concluído

**## Tarefas \`[FE]\`**

\- [ ] Criar feature \`auth\`

\- [ ] Criar tela de login

\- [ ] Criar validação do formulário

\- [ ] Criar cliente HTTP

\- [ ] Criar gestão de sessão

\- [ ] Criar rota protegida

\- [ ] Criar logout

\- [ ] Tratar loading e erro

\- [ ] Preservar sessão ao atualizar a página

**## Tarefas \`[QA]\`**

\- [ ] Testar login no navegador

\- [ ] Testar bloqueio de rota privada

\- [ ] Testar logout

**## Avançar quando**

\- [ ] Utilizador consegue entrar pelo navegador

\- [ ] Utilizador não autenticado é redirecionado

\- [ ] Logout funciona

**## Próximo passo**

Implementar empresa ativa e autorização no **\*\*Marco 5\*\***.

\---

<!-- ============================================================
     MARCO 5 — TENANTS E AUTORIZAÇÃO
     ============================================================ -->

**# Marco 5 — Tenants e autorização**

**## Objetivo**

Aplicar empresa ativa, papéis e isolamento em todas as requisições.

**## Pré-requisito**

\- [ ] Auth web concluído

**## Tarefas \`[BE]\`**

\- [ ] Listar empresas do utilizador

\- [ ] Validar associação utilizador-empresa

\- [ ] Selecionar empresa ativa

\- [ ] Criar contexto/dependency de tenant

\- [ ] Implementar autorização de \`ADMIN\`

\- [ ] Implementar autorização de \`OPERATOR\`

\- [ ] Rejeitar tenant externo

\- [ ] Ignorar \`tenant_id\` não autorizado enviado pelo cliente

**## Tarefas \`[FE]\`**

\- [ ] Criar tela de seleção de empresa

\- [ ] Guardar empresa ativa

\- [ ] Mostrar empresa ativa no layout

\- [ ] Mostrar navegação conforme o papel

\- [ ] Tratar utilizador sem empresa

**## Tarefas \`[QA]\`**

\- [ ] Utilizador vê apenas empresas associadas

\- [ ] Utilizador não acede a outro tenant

\- [ ] \`ADMIN\` pode executar ação administrativa

\- [ ] \`OPERATOR\` não pode executar ação administrativa

\- [ ] Requisição sem tenant ativo é rejeitada

**## Avançar quando**

\- [ ] Login leva à seleção de empresa

\- [ ] Empresa ativa é usada nas requisições

\- [ ] Papéis funcionam

\- [ ] Isolamento foi testado

**## Próximo passo**

Implementar Customers no **\*\*Marco 6\*\***.

\---

<!-- ============================================================
     MARCO 6 — CUSTOMERS
     ============================================================ -->

**# Marco 6 — Customers: primeira fatia completa**

**## Objetivo**

Concluir o primeiro fluxo vertical completo: login → empresa → clientes.

**## Pré-requisito**

\- [ ] Auth concluído

\- [ ] Tenants e autorização concluídos

\- [ ] Tabela \`customers\` criada

**## Tarefas \`[BE]\`**

\- [ ] Criar schemas Pydantic

\- [ ] Criar repository

\- [ ] Criar service/use cases

\- [ ] Criar router

\- [ ] Implementar paginação, busca e filtros

\- [ ] Aplicar tenant e permissões

**## Endpoints**

\- [ ] \`POST /customers\`

\- [ ] \`GET /customers\`

\- [ ] \`GET /customers/{id}\`

\- [ ] \`PATCH /customers/{id}\`

\- [ ] Desativar cliente

**## Tarefas \`[FE]\`**

\- [ ] Criar feature \`customers\`

\- [ ] Criar tabela

\- [ ] Criar formulário

\- [ ] Criar busca e paginação

\- [ ] Criar edição e desativação

\- [ ] Tratar loading, erro e estado vazio

**## Tarefas \`[QA]\`**

\- [ ] Criar cliente válido

\- [ ] Rejeitar nome vazio

\- [ ] Rejeitar email inválido

\- [ ] Pesquisar e paginar

\- [ ] Validar isolamento

\- [ ] Executar fluxo E2E no navegador

**## Avançar quando**

\- [ ] É possível criar, listar, pesquisar, editar e inativar cliente

\- [ ] Clientes de outro tenant nunca aparecem

\- [ ] O fluxo completo funciona no navegador

\- [ ] O teste E2E passa

**## Próximo passo**

Criar a spec do Catálogo no **\*\*Marco 7\*\***.

\---

<!-- ============================================================
     MARCO 7 — CATÁLOGO
     ============================================================ -->

**# Marco 7 — Catalog**

**## Objetivo**

Criar produtos, categorias, preços e estoque mínimo.

**## Antes de programar \`[DOC]\`**

\- [ ] Criar spec de Catalog

\- [ ] Definir campos de categorias, produtos e preços

\- [ ] Definir regras de produto ativo/inativo

\- [ ] Rever o modelo de dados

**## Implementar \`[BD]\`**

\- [ ] Criar \`categories\`

\- [ ] Criar \`products\`

\- [ ] Criar \`price_groups\`

\- [ ] Criar \`product_prices\`

\- [ ] Criar migration

\- [ ] Usar decimal para preços

\- [ ] Definir estoque mínimo

**## Implementar \`[BE]\`**

\- [ ] CRUD de categorias

\- [ ] CRUD de produtos

\- [ ] Gestão de preços

\- [ ] Busca e filtros

\- [ ] Aplicar tenant e permissões

\- [ ] Impedir produto inativo em novos pedidos

**## Implementar \`[FE]\`**

\- [ ] Lista e formulário de produtos

\- [ ] Gestão de categorias

\- [ ] Gestão de preços

\- [ ] Filtros

**## Validar \`[QA]\`**

\- [ ] Criar produto

\- [ ] Rejeitar preço inválido

\- [ ] Testar produto inativo

\- [ ] Testar isolamento

\- [ ] Validar fluxo completo do catálogo

**## Próximo passo**

Implementar Inventory no **\*\*Marco 8\*\***.

\---

<!-- ============================================================
     MARCO 8 — ESTOQUE
     ============================================================ -->

**# Marco 8 — Inventory**

**## Objetivo**

Controlar saldo, entradas, saídas, ajustes e histórico.

**## Implementar**

\- [ ] \`[DOC]\` Criar spec de Inventory

\- [ ] \`[BD]\` Criar \`stock_balances\`

\- [ ] \`[BD]\` Criar \`stock_movements\`

\- [ ] \`[BD]\` Criar migration

\- [ ] \`[BE]\` Consultar saldo

\- [ ] \`[BE]\` Registrar entrada

\- [ ] \`[BE]\` Registrar saída

\- [ ] \`[BE]\` Registrar ajuste com motivo

\- [ ] \`[BE]\` Impedir estoque negativo

\- [ ] \`[BE]\` Implementar alerta de estoque baixo

\- [ ] \`[FE]\` Criar feature \`inventory\`

\- [ ] \`[FE]\` Mostrar saldo, histórico e alertas

\- [ ] \`[QA]\` Testar entradas, saídas, ajustes e isolamento

**## Avançar quando**

\- [ ] O saldo é atualizado corretamente

\- [ ] O estoque nunca fica negativo

\- [ ] Todo movimento tem histórico

\- [ ] O fluxo funciona no navegador

**## Próximo passo**

Implementar Orders no **\*\*Marco 9\*\***.

\---

<!-- ============================================================
     MARCO 9 — PEDIDOS
     ============================================================ -->

**# Marco 9 — Orders**

**## Objetivo**

Criar, confirmar e cancelar pedidos, movimentando o estoque.

**## Antes de programar \`[DOC]\`**

\- [ ] Criar spec de Orders

\- [ ] Definir estados \`DRAFT\`, \`CONFIRMED\` e \`CANCELLED\`

\- [ ] Definir regra de cancelamento

**## Implementar \`[BD]\`**

\- [ ] Criar \`orders\`

\- [ ] Criar \`order_items\`

\- [ ] Criar \`order_status_history\`

\- [ ] Criar migration

**## Implementar \`[BE]\`**

\- [ ] Criar pedido em \`DRAFT\`

\- [ ] Adicionar e remover itens

\- [ ] Calcular subtotal, desconto e total

\- [ ] Validar produtos ativos e estoque

\- [ ] Confirmar pedido numa transação

\- [ ] Baixar estoque ao confirmar

\- [ ] Cancelar com motivo

\- [ ] Impedir edição de pedido confirmado

\- [ ] Registrar histórico de estados

**## Implementar \`[FE]\`**

\- [ ] Criar feature \`orders\`

\- [ ] Criar formulário

\- [ ] Selecionar cliente e produtos

\- [ ] Mostrar cálculo e estado

\- [ ] Confirmar e cancelar pedido

**## Validar \`[QA]\`**

\- [ ] Estoque insuficiente é rejeitado

\- [ ] Confirmação duplicada é rejeitada

\- [ ] Falha faz rollback

\- [ ] Cancelamento funciona

\- [ ] Fluxo E2E do pedido passa

**## Próximo passo**

Implementar Receivables no **\*\*Marco 10\*\***.

\---

<!-- ============================================================
     MARCO 10 — CONTAS A RECEBER
     ============================================================ -->

**# Marco 10 — Receivables**

**## Objetivo**

Gerar contas a receber e registrar pagamentos.

**## Implementar**

\- [ ] \`[DOC]\` Criar spec de Receivables

\- [ ] \`[BD]\` Criar \`receivables\`

\- [ ] \`[BD]\` Criar \`receivable_installments\`

\- [ ] \`[BD]\` Criar \`payments\`

\- [ ] \`[BD]\` Criar migration

\- [ ] \`[BE]\` Gerar recebível ao confirmar pedido

\- [ ] \`[BE]\` Criar parcelas

\- [ ] \`[BE]\` Listar contas

\- [ ] \`[BE]\` Registrar pagamento parcial ou total

\- [ ] \`[BE]\` Atualizar saldo e estado

\- [ ] \`[BE]\` Identificar vencidos

\- [ ] \`[BE]\` Impedir pagamento acima do saldo

\- [ ] \`[FE]\` Criar lista e filtros

\- [ ] \`[FE]\` Criar registro de pagamento

\- [ ] \`[QA]\` Testar geração, pagamento, vencimento e cancelamento

**## Próximo passo**

Implementar Dashboard no **\*\*Marco 11\*\***.

\---

<!-- ============================================================
     MARCO 11 — DASHBOARD
     ============================================================ -->

**# Marco 11 — Dashboard**

**## Objetivo**

Mostrar indicadores da empresa ativa.

**## Implementar**

\- [ ] \`[BE]\` Vendas do período

\- [ ] \`[BE]\` Pedidos recentes

\- [ ] \`[BE]\` Total a receber

\- [ ] \`[BE]\` Produtos com estoque baixo

\- [ ] \`[BE]\` Filtro por período e tenant

\- [ ] \`[FE]\` Cards de indicadores

\- [ ] \`[FE]\` Gráfico simples de vendas

\- [ ] \`[FE]\` Listas de pedidos e estoque baixo

\- [ ] \`[QA]\` Validar totais, filtros e isolamento

**## Próximo passo**

Consolidar o MVP web no **\*\*Marco 12\*\***.

\---

<!-- ============================================================
     MARCO 12 — VALIDAÇÃO E PUBLICAÇÃO DO MVP WEB
     ============================================================ -->

**# Marco 12 — Validar e publicar o MVP web**

**## Fluxo de aceitação**

\- [ ] \`[QA]\` Fazer login

\- [ ] \`[QA]\` Selecionar empresa

\- [ ] \`[QA]\` Criar cliente

\- [ ] \`[QA]\` Criar produto

\- [ ] \`[QA]\` Registrar estoque

\- [ ] \`[QA]\` Criar pedido

\- [ ] \`[QA]\` Confirmar pedido

\- [ ] \`[QA]\` Verificar baixa de estoque

\- [ ] \`[QA]\` Verificar recebível

\- [ ] \`[QA]\` Registrar pagamento

\- [ ] \`[QA]\` Verificar dashboard

**## Qualidade**

\- [ ] \`[QA]\` Executar testes unitários e de integração

\- [ ] \`[QA]\` Executar teste E2E principal

\- [ ] \`[QA]\` Executar lint e build

\- [ ] \`[QA]\` Rever segurança e isolamento

\- [ ] \`[DOC]\` Atualizar README e documentação da API

\- [ ] \`[DOC]\` Atualizar modelo de dados

**## Próximo passo**

Depois de o MVP web estar estável, iniciar o mobile no **\*\*Marco 13\*\***.

\---

<!-- ============================================================
     MARCO 13 — MOBILE
     ============================================================ -->

**# Marco 13 — Mobile**

\> Mobile é uma aplicação separada que consome a mesma API. É uma etapa posterior ao MVP web.

\- [ ] \`[MOBILE]\` Criar projeto React Native + Expo

\- [ ] \`[MOBILE]\` Implementar login e sessão

\- [ ] \`[MOBILE]\` Consultar clientes e produtos

\- [ ] \`[MOBILE]\` Consultar estoque

\- [ ] \`[MOBILE]\` Criar e consultar pedidos

\- [ ] \`[QA]\` Validar tenant e permissões

**## Próximo passo**

Fazer deploy e preparar o portfólio no **\*\*Marco 14\*\***.

\---

<!-- ============================================================
     MARCO 14 — DEPLOY E PORTFÓLIO
     ============================================================ -->

**# Marco 14 — Deploy e portfólio**

\- [ ] \`[INFRA]\` Configurar produção

\- [ ] \`[INFRA]\` Executar migrations de produção

\- [ ] \`[INFRA]\` Publicar API e frontend

\- [ ] \`[QA]\` Testar fluxo em produção

\- [ ] \`[PORTFÓLIO]\` Atualizar README

\- [ ] \`[PORTFÓLIO]\` Adicionar diagrama ER

\- [ ] \`[PORTFÓLIO]\` Adicionar screenshots

\- [ ] \`[PORTFÓLIO]\` Adicionar link da demo

\- [ ] \`[PORTFÓLIO]\` Criar vídeo de demonstração

\- [ ] \`[PORTFÓLIO]\` Documentar limitações e próximos passos

\---

<!-- ============================================================
     CONTEXTO: ESTADO ATUAL DO PROJETO
     ============================================================ -->

**# Onde você está agora**

\`\`\`

Marco concluído: 0 — Fundação e documentação

Próximo marco: 1 — Modelar Auth, Tenants e Customers

Primeira entrega: docs/database/data-model.md

\`\`\`

<!-- ============================================================
     CONTEXTO: PRÓXIMA AÇÃO
     ============================================================ -->

**## Próxima ação exata**

\- [ ] Abrir \`docs/specs/001-auth-tenants-customers.md\`

\- [ ] Listar \`users\`, \`tenants\`, \`tenant_users\` e \`customers\`

\- [ ] Definir os campos de cada entidade

\- [ ] Definir os relacionamentos

\- [ ] Criar \`docs/database/data-model.md\`

\- [ ] Criar \`database/diagrams/er-model.mmd\`

\- [ ] Solicitar revisão antes de criar a migration