# Roadmap de aprendizagem e desenvolvimento

Este documento é o **to-do principal** do projeto. A regra é simples: antes de implementar uma etapa, estudar o mínimo necessário para entender o que está sendo feito e por quê.

Não avance por quantidade de código. Avance quando conseguir explicar a etapa com suas próprias palavras.

## Como usar este documento

1. Trabalhe em apenas uma tarefa marcada como **Agora**.
2. Faça o estudo indicado antes de escrever código.
3. Anote dúvidas e termos novos.
4. Implemente uma versão pequena.
5. Teste manualmente e com teste automatizado quando aplicável.
6. Marque a tarefa somente quando o critério de conclusão estiver satisfeito.
7. Se uma tarefa parecer grande, divida-a antes de começar.

## Ritmo recomendado

Faça três sessões semanais de 60 a 90 minutos:

- **Sessão A — estudar:** conceito, documentação oficial e exemplo pequeno.
- **Sessão B — implementar:** uma alteração pequena e funcional.
- **Sessão C — testar e revisar:** corrigir, explicar o que aprendeu e atualizar este arquivo.

Se tiver menos tempo, reduza o tamanho da tarefa, não pule o estudo.

## Regra de conclusão

Uma etapa só está concluída quando:

- [ ] consigo explicar o que implementei sem copiar a explicação;
- [ ] sei em quais arquivos a mudança foi feita;
- [ ] consigo executar a funcionalidade localmente;
- [ ] existe teste ou verificação manual registrada;
- [ ] não deixei dúvidas importantes escondidas;
- [ ] atualizei a documentação quando o comportamento mudou.

---

## Fase 0 — Preparar o estudo e o ambiente

### Estudar antes

- [ ] Revisar Git: branch, commit, diff, restore e log.
- [ ] Revisar Python: ambiente virtual, imports, funções, classes e exceções.
- [ ] Revisar HTTP: request, response, métodos, status codes e JSON.
- [ ] Entender o que são API, backend, frontend, banco de dados e migration.
- [ ] Ler o README e [arquitetura](architecture.md).

### Fazer

- [ ] Clonar e executar a API localmente.
- [ ] Executar `GET /health`.
- [ ] Executar os testes existentes.
- [ ] Criar uma branch de trabalho para a primeira funcionalidade.
- [ ] Registrar dúvidas em uma seção pessoal de notas.

**Entrega:** consigo iniciar a API, chamar `/health` e explicar o fluxo básico.

---

## Fase 1 — Banco de dados e persistência

> Não criar todo o banco futuro. Criar somente o necessário para o primeiro fluxo.

### 1.1 PostgreSQL e migrations

**Estudar:** tabelas, colunas, chaves primárias, chaves estrangeiras, índices, constraints, transações, SQLAlchemy e Alembic.

- [ ] Entender como o PostgreSQL inicia no Docker Compose.
- [ ] Entender a diferença entre modelo Python, tabela e migration.
- [ ] Criar uma migration simples e saber revertê-la.
- [ ] Verificar a tabela criada diretamente no banco.

### 1.2 Primeiro modelo

Criar somente estas entidades iniciais:

- [ ] `users` — pessoa que acessa o sistema.
- [ ] `tenants` — empresa.
- [ ] `tenant_users` — vínculo entre pessoa, empresa, papel e estado.

**Estudar:** relacionamento muitos-para-muitos, chave composta ou constraint de unicidade e integridade referencial.

- [ ] Definir campos mínimos.
- [ ] Criar modelos SQLAlchemy.
- [ ] Criar migration.
- [ ] Criar dados de desenvolvimento, se necessário.
- [ ] Testar criação e relacionamento dos registros.

### 1.3 Clientes

**Estudar:** soft delete/inativação, timestamps, unicidade por empresa e modelagem de dados de cadastro.

- [ ] Definir campos mínimos de `customers`.
- [ ] Relacionar cliente com empresa.
- [ ] Garantir que `customer_code` seja único dentro da empresa quando usado.
- [ ] Criar migration.
- [ ] Testar que clientes pertencem a uma única empresa.

**Entrega da Fase 1:** banco reproduzível por migrations, com usuários, empresas, vínculos e clientes.

---

## Fase 2 — Backend básico

### 2.1 Estrutura da API

**Estudar:** FastAPI, dependências, Pydantic, routers, schemas e separação entre rota, serviço e persistência.

- [ ] Entender o caminho de uma requisição até o banco.
- [ ] Definir uma organização simples de módulos.
- [ ] Criar schemas de entrada e saída.
- [ ] Aprender a validar dados e retornar erros HTTP claros.

### 2.2 Identidade de desenvolvimento

> OAuth/OIDC ainda precisa de decisão. Não bloquear o aprendizado com uma integração definitiva.

**Estudar:** autenticação versus autorização, usuário atual, sessão/token e princípio do menor privilégio.

- [ ] Definir um mecanismo temporário apenas para desenvolvimento/testes.
- [ ] Deixar explícito no código que não é solução de produção.
- [ ] Obter o usuário atual em uma dependência da API.
- [ ] Recusar requisições sem identidade.

### 2.3 Empresa ativa e autorização

**Estudar:** autorização por recurso, isolamento multiempresa e testes negativos.

- [ ] Validar que o usuário pertence à empresa.
- [ ] Validar papel dentro da empresa correta.
- [ ] Definir como a empresa ativa chega à API.
- [ ] Impedir acesso usando apenas um ID de empresa enviado pelo cliente.
- [ ] Testar usuário com duas empresas e papéis diferentes.

### 2.4 CRUD de clientes

- [ ] Criar `POST /customers`.
- [ ] Criar `GET /customers`.
- [ ] Criar `GET /customers/{id}`.
- [ ] Criar `PATCH /customers/{id}`.
- [ ] Criar ação de inativação.
- [ ] Filtrar sempre pela empresa autorizada.
- [ ] Testar sucesso, validação, não encontrado e acesso cruzado.

**Entrega da Fase 2:** API de clientes funcionando com autorização e testes.

---

## Fase 3 — Frontend inicial

### Estudar antes

- [ ] Revisar React: componentes, props, estado e eventos.
- [ ] Revisar TypeScript: tipos, interfaces e unions.
- [ ] Revisar chamadas HTTP e tratamento de estados.
- [ ] Entender loading, sucesso, erro e estado vazio.
- [ ] Entender formulários e validação no frontend.

### Implementar

- [ ] Criar tela de listagem de clientes.
- [ ] Criar formulário de cliente.
- [ ] Integrar criação com a API.
- [ ] Integrar edição.
- [ ] Integrar inativação.
- [ ] Exibir loading, erro, sucesso e lista vazia.
- [ ] Testar manualmente o fluxo completo.

**Entrega da Fase 3:** usuário consegue entrar no fluxo, selecionar empresa e manter clientes pela interface.

---

## Fase 4 — Próximos módulos

Não iniciar esta fase antes de concluir o primeiro fluxo completo.

### Catálogo e preços

- [ ] Estudar modelagem de produtos, categorias e valores monetários.
- [ ] Definir escopo mínimo.
- [ ] Criar banco e migrations.
- [ ] Criar endpoints e testes.
- [ ] Criar telas básicas.

### Estoque

- [ ] Estudar transações e consistência.
- [ ] Definir movimentos, saldo e histórico.
- [ ] Criar banco, backend, testes e telas.

### Pedidos

- [ ] Estudar máquina de estados e transações.
- [ ] Criar rascunho e itens.
- [ ] Calcular subtotal, desconto e total.
- [ ] Confirmar pedido validando estoque.
- [ ] Integrar pedido e estoque.

### Recebíveis e painel

- [ ] Estudar pagamentos parciais, saldo e vencimento.
- [ ] Criar recebíveis após confirmação.
- [ ] Criar registros de pagamento.
- [ ] Criar indicadores simples por empresa e período.

---

## Quadro semanal

Copie esta seção para cada semana:

**Semana de:** ____ / ____ / ____

**Objetivo único:** __________________________________________

**Estudar antes:** ___________________________________________

- [ ] Estudo concluído
- [ ] Notas escritas com minhas próprias palavras
- [ ] Implementação pequena concluída
- [ ] Teste/verificação executado
- [ ] Dúvidas registradas
- [ ] Documentação atualizada

**O que aprendi:**

> 

**O que ficou difícil:**

> 

**Próximo passo concreto:**

> 

## Quando estiver perdido

Pare de codificar e responda, por escrito:

1. Qual comportamento estou tentando entregar?
2. Qual conceito ainda não entendo?
3. Que menor exemplo posso fazer isoladamente?
4. Como vou saber que funcionou?
5. Essa decisão está definida em [requisitos](requirements.md) ou ainda é uma pendência?

Se não conseguir responder, a próxima tarefa é **estudar e esclarecer**, não implementar mais código.
