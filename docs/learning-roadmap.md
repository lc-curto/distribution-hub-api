# Roadmap de aprendizagem e desenvolvimento

Este documento é o **to-do principal** do projeto. A regra é simples: antes de implementar uma etapa, estudar o mínimo necessário para entender o que está sendo feito e por quê.

Não avance por quantidade de código. Avance quando conseguir explicar a etapa com suas próprias palavras.

## Como usar este documento

1. Trabalhe em apenas uma tarefa marcada como **Agora**.

1. Faça o estudo indicado antes de escrever código.

1. Anote dúvidas e termos novos.

1. Implemente uma versão pequena.

1. Teste manualmente e com teste automatizado quando aplicável.

1. Marque a tarefa somente quando o critério de conclusão estiver satisfeito.

1. Se uma tarefa parecer grande, divida-a antes de começar.

## Como estudar uma tarefa

Para cada item, use este ciclo curto:

1. **Entender:** escreva o que a tecnologia faz e qual problema resolve.
2. **Observar:** leia a documentação oficial e veja um exemplo mínimo.
3. **Praticar:** faça um exercício isolado, sem misturar ainda com o projeto.
4. **Explicar:** descreva o exercício com suas próprias palavras.
5. **Aplicar:** só então faça a alteração no Cosmetics Hub.

Não tente aprender toda a tecnologia antes de começar. Estude apenas o conceito necessário para a tarefa atual e registre o que ficou para depois.

## Fila de trabalho

Mantenha três grupos para não tentar fazer tudo ao mesmo tempo:

- **Agora:** uma única tarefa pequena. Atualmente: Fase 0 — preparar o ambiente.
- **Depois:** as próximas duas ou três tarefas da fase atual.
- **Mais tarde:** ideias, melhorias e módulos que ainda não são necessários para o primeiro fluxo.

Quando terminar uma tarefa, mova apenas a próxima para **Agora**. Não reorganize o projeto inteiro toda semana.

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

**Objetivo:** deixar a API executando no seu computador antes de criar qualquer funcionalidade.

### Passo a passo executável

Faça um passo por vez, confirmando o resultado antes de continuar:

```bash
# 1. Entre na pasta do repositório
cd caminho/para/cosmetics-hub-api

# 2. Confira as ferramentas
python3 --version
git --version
docker --version
docker compose version

# 3. Crie e ative um ambiente Python isolado
python3 -m venv .venv
source .venv/bin/activate

# 4. Instale as dependências do projeto
python -m pip install --upgrade pip
pip install -e ".[dev]"

# 5. Crie sua configuração local
cp .env.example .env

# 6. Inicie somente o PostgreSQL local
docker compose up -d postgres

# 7. Inicie a API; mantenha este terminal aberto
uvicorn app.main:app --reload
```

Abra outro terminal, ative o ambiente novamente e verifique:

```bash
cd caminho/para/cosmetics-hub-api
source .venv/bin/activate
curl http://127.0.0.1:8000/health
pytest
```

**Resultado esperado:** o `curl` retorna `{"status":"ok"}` e o teste passa. Depois abra `http://127.0.0.1:8000/docs` para ver a documentação automática da API.

**Se algo falhar:** copie a mensagem de erro para suas notas; não tente corrigir várias coisas ao mesmo tempo. Primeiro identifique se o problema é Python, dependência, Docker, banco ou API.

### Exemplo de estudo

Antes de começar, explique em uma frase: “o ambiente virtual separa as dependências deste projeto das dependências do meu computador”. Depois faça o mesmo para Docker Compose, FastAPI, endpoint, teste e migration.


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

**Antes de avançar:** devo saber onde ficam o código da API, os testes, as configurações e o comando para executar o projeto.

---

## Fase 1 — Banco de dados e persistência

> Não criar todo o banco futuro. Criar somente o necessário para o primeiro fluxo.

### 1.1 PostgreSQL e migrations

**Exemplo:** criar uma tabela mínima `users` com `id`, `email` e `created_at`. Primeiro você cria o modelo, depois gera uma migration, aplica a migration e confirma que a tabela existe no PostgreSQL. Se apagar o banco e aplicar as migrations novamente, o resultado deve ser igual.


**Estudar:** tabelas, colunas, chaves primárias, chaves estrangeiras, índices, constraints, transações, SQLAlchemy e Alembic.

- [ ] Entender como o PostgreSQL inicia no Docker Compose.

- [ ] Entender a diferença entre modelo Python, tabela e migration.

- [ ] Criar uma migration simples e saber revertê-la.

- [ ] Verificar a tabela criada diretamente no banco.

### 1.2 Primeiro modelo

**Exemplo:** a mesma pessoa pode estar na empresa A como `ADMIN` e na empresa B como `OPERATOR`. Isso mostra por que o papel fica em `tenant_users`, e não diretamente em `users`. Teste também que o mesmo usuário não pode ter duas associações iguais com a mesma empresa.


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

**Exemplo:** criar o cliente “Loja Rosa” na empresa A. Ele pode ser consultado por usuários autorizados da empresa A, mas não aparece para usuários da empresa B. Ao inativá-lo, ele continua no histórico e deixa de poder ser usado em pedidos novos.


**Estudar:** soft delete/inativação, timestamps, unicidade por empresa e modelagem de dados de cadastro.

- [ ] Definir campos mínimos de `customers`.

- [ ] Relacionar cliente com empresa.

- [ ] Garantir que `customer_code` seja único dentro da empresa quando usado.

- [ ] Criar migration.

- [ ] Testar que clientes pertencem a uma única empresa.

**Entrega da Fase 1:** banco reproduzível por migrations, com usuários, empresas, vínculos e clientes.

**Antes de avançar:** devo conseguir apagar e recriar o banco a partir das migrations e explicar por que cada tabela existe.

---

## Fase 2 — Backend básico

### 2.1 Estrutura da API

**Exemplo:** criar primeiro um endpoint `GET /customers` que retorna uma lista vazia. Depois separar o schema da resposta, a rota e a consulta ao banco. O objetivo inicial não é ter um CRUD completo, mas entender o caminho “requisição → validação → regra → banco → resposta”.


**Estudar:** FastAPI, dependências, Pydantic, routers, schemas e separação entre rota, serviço e persistência.

- [ ] Entender o caminho de uma requisição até o banco.

- [ ] Definir uma organização simples de módulos.

- [ ] Criar schemas de entrada e saída.

- [ ] Aprender a validar dados e retornar erros HTTP claros.

### 2.2 Identidade de desenvolvimento

**Exemplo:** em desenvolvimento, usar uma identidade fixa e explícita, como `dev-user-a`, somente para os testes. Uma requisição sem essa identidade deve receber erro. Essa solução serve para aprender autorização; não deve ser apresentada como autenticação de produção.


> OAuth/OIDC ainda precisa de decisão. Não bloquear o aprendizado com uma integração definitiva.

**Estudar:** autenticação versus autorização, usuário atual, sessão/token e princípio do menor privilégio.

- [ ] Definir um mecanismo temporário apenas para desenvolvimento/testes.

- [ ] Deixar explícito no código que não é solução de produção.

- [ ] Obter o usuário atual em uma dependência da API.

- [ ] Recusar requisições sem identidade.

### 2.3 Empresa ativa e autorização

**Exemplo:** o usuário A pertence às empresas 1 e 2. Ao consultar clientes da empresa 1, vê apenas clientes da empresa 1. Se tentar trocar o identificador para empresa 2 sem ter autorização, a API recusa. Escreva esse caso como teste negativo antes do código.


**Estudar:** autorização por recurso, isolamento multiempresa e testes negativos.

- [ ] Validar que o usuário pertence à empresa.

- [ ] Validar papel dentro da empresa correta.

- [ ] Definir como a empresa ativa chega à API.

- [ ] Impedir acesso usando apenas um ID de empresa enviado pelo cliente.

- [ ] Testar usuário com duas empresas e papéis diferentes.

### 2.4 CRUD de clientes

**Exemplo de sequência:** `POST` cria “Loja Rosa”; `GET` lista a loja; `GET /customers/{id}` consulta; `PATCH` corrige o telefone; a ação de inativação altera o estado. Teste também um ID inexistente, dados inválidos e um cliente de outra empresa.


- [ ] Criar `POST /customers`.

- [ ] Criar `GET /customers`.

- [ ] Criar `GET /customers/{id}`.

- [ ] Criar `PATCH /customers/{id}`.

- [ ] Criar ação de inativação.

- [ ] Filtrar sempre pela empresa autorizada.

- [ ] Testar sucesso, validação, não encontrado e acesso cruzado.

**Entrega da Fase 2:** API de clientes funcionando com autorização e testes.

**Antes de avançar:** devo conseguir explicar o caminho de uma requisição, validar um dado inválido e provar com teste que uma empresa não acessa os clientes de outra.

---

## Fase 3 — Frontend inicial

### Estudar antes

**Exemplo:** antes de criar uma tela, faça uma tela de teste que apenas busca `/health` e mostra “API online”. Assim você aprende a chamada HTTP sem misturar formulário, autenticação e banco.


- [ ] Revisar React: componentes, props, estado e eventos.

- [ ] Revisar TypeScript: tipos, interfaces e unions.

- [ ] Revisar chamadas HTTP e tratamento de estados.

- [ ] Entender loading, sucesso, erro e estado vazio.

- [ ] Entender formulários e validação no frontend.

### Implementar

**Exemplo:** a primeira tela real pode apenas listar clientes. Depois adicione o formulário de criação; só depois edição e inativação. Em cada etapa, trate explicitamente carregando, sucesso, erro e lista vazia.


- [ ] Criar tela de listagem de clientes.

- [ ] Criar formulário de cliente.

- [ ] Integrar criação com a API.

- [ ] Integrar edição.

- [ ] Integrar inativação.

- [ ] Exibir loading, erro, sucesso e lista vazia.

- [ ] Testar manualmente o fluxo completo.

**Entrega da Fase 3:** usuário consegue entrar no fluxo, selecionar empresa e manter clientes pela interface.

**Antes de avançar:** devo conseguir explicar como o frontend chama a API e o que acontece nos estados de carregamento, sucesso, erro e lista vazia.

---

## Fase 4 — Próximos módulos

Não iniciar esta fase antes de concluir o primeiro fluxo completo.

### Catálogo e preços

**Exemplo:** comece com uma categoria “Batom” e um produto “Batom Rosa” com preço decimal. Não implemente promoções, múltiplas tabelas de preço ou importação em lote nesta primeira versão.


- [ ] Estudar modelagem de produtos, categorias e valores monetários.

- [ ] Definir escopo mínimo.

- [ ] Criar banco e migrations.

- [ ] Criar endpoints e testes.

- [ ] Criar telas básicas.

### Estoque

**Exemplo:** registrar entrada de 10 unidades, saída de 3 e confirmar saldo 7. Tentar retirar 8 deve falhar sem alterar o saldo. Esse caso ensina transação, validação e histórico.


- [ ] Estudar transações e consistência.

- [ ] Definir movimentos, saldo e histórico.

- [ ] Criar banco, backend, testes e telas.

### Pedidos

**Exemplo:** criar um pedido em `DRAFT` com um produto, calcular o total e confirmar. A confirmação só pode diminuir o estoque se houver saldo suficiente; se falhar, pedido e estoque não podem ficar parcialmente atualizados.


- [ ] Estudar máquina de estados e transações.

- [ ] Criar rascunho e itens.

- [ ] Calcular subtotal, desconto e total.

- [ ] Confirmar pedido validando estoque.

- [ ] Integrar pedido e estoque.

### Recebíveis e painel

**Exemplo:** um pedido confirmado de 100 cria um recebível de 100. Um pagamento de 40 deixa saldo 60 e estado parcial. O painel pode começar mostrando apenas vendas do mês e total em aberto.


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

1. Qual conceito ainda não entendo?

1. Que menor exemplo posso fazer isoladamente?

1. Como vou saber que funcionou?

1. Essa decisão está definida em [requisitos](requirements.md) ou ainda é uma pendência?

Se não conseguir responder, a próxima tarefa é **estudar e esclarecer**, não implementar mais código.
