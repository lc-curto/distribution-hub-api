# Fluxo de trabalho para mudanças do produto

Este fluxo organiza uma mudança funcional em fatias verticais e mantém documentação e implementação alinhadas.

## Etapas

1. **Definir a necessidade:** registrar quem precisa do comportamento, por que e a fonte dessa necessidade.
2. **Atualizar regras e requisitos:** separar regra de negócio, requisito funcional, qualidade e decisão técnica; esclarecer questões abertas antes de fixar comportamento.
3. **Atualizar o modelo de domínio/dados:** mudar entidades, relações e restrições quando necessário; registrar migration como parte da implementação, não como substituto da especificação.
4. **Definir o contrato da API:** atualizar endpoints e schemas; validar o contrato OpenAPI que FastAPI gera.
5. **Implementar e testar a API:** aplicar autorização no backend e cobrir regras críticas com testes.
6. **Implementar o frontend:** integrar-se pela API e apresentar estados de carregamento, sucesso, erro e ausência de dados.
7. **Validar integração e atualizar documentação:** revisar critérios de aceitação, estado da funcionalidade e links.

## Critério de conclusão

Uma funcionalidade só pode ser descrita como implementada quando o código correspondente existe, os testes relevantes passam e os critérios de aceitação são satisfeitos. Se alguma etapa estiver pendente, a documentação deve dizer isso diretamente.

O fluxo é orientativo: ele não aprova sozinho regras de negócio, escolhas de autenticação nem mudanças de escopo.