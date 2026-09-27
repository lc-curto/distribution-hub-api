# Questões em aberto

Estas questões são lacunas ou conflitos encontrados nas especificações preservadas. Elas são mantidas visíveis para evitar que a implementação assuma decisões silenciosamente.

## OAuth 2.0 e identidade

1. O uso pretendido de OAuth 2.0 é autorização de acesso a uma API, login federado de pessoas, ou ambos?
2. Se pessoas precisarem de login federado, OIDC será adotado? Qual provedor de identidade será usado?
3. Como a identidade externa será associada ao usuário local? Email será apenas contato ou também terá política de unicidade/verificação?
4. Quais clientes, scopes, política de tokens, logout, renovação, revogação e armazenamento no navegador são necessários?

## Empresas e permissões

5. Como uma nova pessoa entra na empresa: cadastro aberto, convite administrativo ou outro processo?
6. Como o frontend comunica a empresa ativa à API: token, sessão, cabeçalho ou outro contrato? O antigo exemplo `X-Tenant-ID` não foi confirmado.

### Permissões do papel OPERATOR

Os documentos preservados divergem sobre a gestão de produtos e categorias, movimentos de estoque e registro de pagamentos pelo operador. Essas permissões precisam de validação antes de serem implementadas.

7. Quais ações de criação/edição de produtos e categorias são permitidas ao `OPERATOR`? Os documentos preservados divergem.
8. Quais papéis podem registrar cada tipo de entrada, saída e ajuste de estoque, bem como pagamentos?
9. Como a empresa recupera acesso se perder seu último administrador? A regra atual protege o último `ADMIN`, mas não descreve recuperação administrativa.

## Regras comerciais e dados

10. Ao cancelar um pedido confirmado, quando e como o estoque é devolvido? O texto atual não fecha a regra.
11. Qual a moeda, precisão, arredondamento, impostos e representação de preço? Como preço e desconto são preservados no histórico do pedido?
12. Qual a data de vencimento de um recebível e como calendário, fuso horário e estados vencidos são calculados?
13. Quais métodos de pagamento são aceitos e como estornos/reembolsos são tratados?
14. Quais campos de produto, estoque, pedido, itens do pedido, pagamento e recebível serão persistidos? O modelo detalhado atual cobre apenas usuários, empresas, associações e clientes.
15. Quais identificadores fiscais e regras de endereço se aplicam aos países atendidos?

## Qualidade, privacidade e operação

16. Quais metas quantitativas de desempenho, disponibilidade e acessibilidade devem ser testadas?
17. Quais políticas de retenção, exportação, correção e exclusão de dados se aplicam?
18. Quais requisitos de auditoria, monitoramento, backup e recuperação são necessários para produção?
19. Qual o formato versionado do contrato OpenAPI e como o frontend será validado contra ele?

Quando uma questão for resolvida, atualize o documento pertinente e registre uma ADR se a resposta for uma decisão técnica significativa.
