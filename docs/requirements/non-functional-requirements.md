# Requisitos não funcionais — MVP

**Produto:** Cosmetics Hub  
**Escopo:** MVP

Requisitos não funcionais descrevem **como o sistema deve funcionar**, incluindo segurança, qualidade, manutenção e operação.

## Segurança

### RNF-001 — Senhas
Palavras-passe nunca devem ser armazenadas em texto puro. Devem ser protegidas com hash seguro.

### RNF-002 — Autenticação
Rotas privadas devem exigir autenticação válida.

### RNF-003 — Autorização
O backend deve validar o papel e a permissão do utilizador em cada operação protegida.

### RNF-004 — Isolamento
Um utilizador não pode consultar ou alterar dados de uma empresa à qual não está associado. O `tenant_id` enviado pelo frontend não é confiável por si só.

### RNF-005 — Dados sensíveis
Respostas e mensagens de erro não devem expor palavras-passe, segredos ou detalhes internos desnecessários.

## Integridade dos dados

### RNF-010 — Banco relacional
O sistema deve utilizar PostgreSQL como fonte principal de verdade.

### RNF-011 — Integridade referencial
Relacionamentos importantes devem ser protegidos por foreign keys, constraints e validações.

### RNF-012 — Valores monetários
Valores monetários não devem utilizar `float`. Devem utilizar tipo decimal apropriado no banco e na aplicação.

### RNF-013 — Transações
Confirmação de pedido e atualização de estoque devem ser atómicas: se uma parte falhar, nenhuma alteração parcial deve permanecer.

### RNF-014 — Histórico
Movimentações de estoque, estados de pedidos e pagamentos devem preservar histórico suficiente para rastreabilidade.

## API

### RNF-020 — Contratos
A API deve validar entradas e saídas através de schemas tipados.

### RNF-021 — Erros
A API deve utilizar respostas de erro consistentes, sem depender de mensagens específicas do banco de dados.

### RNF-022 — Documentação
A API deve disponibilizar documentação OpenAPI através do FastAPI.

### RNF-023 — Versionamento futuro
A API deve ser organizada de modo que uma futura versão possa ser adicionada sem quebrar imediatamente os clientes existentes. A necessidade de versionamento formal fica para quando houver mais de uma versão publicada.

## Frontend

### RNF-030 — Responsividade
A aplicação web deve funcionar em computador, tablet e telemóvel.

### RNF-031 — Estados da interface
As telas devem tratar loading, sucesso, erro e ausência de dados.

### RNF-032 — Acessibilidade básica
Formulários, botões, tabelas e mensagens devem possuir labels e estados compreensíveis.

### RNF-033 — Segurança no frontend
A interface pode validar e orientar o utilizador, mas nunca deve ser a única camada de autorização.

## Qualidade e testes

### RNF-040 — Testes de regras críticas
Devem existir testes para isolamento por tenant, permissões, estoque negativo, confirmação de pedido e pagamentos.

### RNF-041 — Testes de integração
Os principais fluxos devem ser testados com API e PostgreSQL.

### RNF-042 — Teste E2E
Deve existir pelo menos um teste E2E do fluxo principal do MVP.

### RNF-043 — Build e CI
O projeto deve executar testes e build através do GitHub Actions.

## Manutenção

### RNF-050 — Organização
O backend deve ser organizado por módulos de negócio e o frontend por features/domínios.

### RNF-051 — Documentação
Decisões relevantes, regras de negócio, modelo de dados e instruções de execução devem estar documentados no repositório.

### RNF-052 — Configuração
Segredos e configurações específicas de ambiente devem ser fornecidos por variáveis de ambiente, nunca gravados no código.

### RNF-053 — Migrations
Alterações do schema devem ser feitas através de migrations versionadas.

## Operação

### RNF-060 — Health check
A API deve disponibilizar um endpoint de verificação de saúde.

### RNF-061 — Ambiente reproduzível
Um novo ambiente local deve poder ser iniciado através das instruções do README e do Docker Compose.

### RNF-062 — Observabilidade mínima
Erros relevantes devem ser registados com contexto suficiente para investigação, sem expor dados sensíveis.

## Fora do escopo não funcional do MVP

Alta disponibilidade, escalabilidade horizontal, observabilidade avançada, disaster recovery automatizado, SLA formal e otimizações de grande escala ficam para versões futuras.
