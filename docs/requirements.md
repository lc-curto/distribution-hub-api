# Requisitos e pendências

Os itens abaixo descrevem comportamento desejado; não comprovam implementação. No estado atual, a API fornece somente `GET /health`.

## Capacidades previstas

- **Acesso e empresas:** identificar usuários, listar empresas associadas, selecionar empresa ativa e aplicar `ADMIN`/`OPERATOR`.
- **Clientes:** criar, consultar, pesquisar, editar e inativar no escopo da empresa.
- **Catálogo e preços:** gerir categorias, produtos e preços conforme permissões.
- **Estoque:** consultar saldo, registrar entradas, saídas e ajustes com histórico.
- **Pedidos:** criar rascunhos, calcular totais, confirmar atomicamente, cancelar com justificativa e manter histórico.
- **Recebíveis:** criar após pedido, registrar pagamentos parciais/totais e calcular saldo/vencimento.
- **Painel:** exibir vendas, pedidos, recebíveis e estoque baixo por empresa e período.

## Qualidade e segurança

Identidade válida é exigida para recursos privados. O backend verifica permissões e impede acesso cruzado entre empresas. Segredos não aparecem em respostas. Valores monetários usam representação decimal. Erros têm formato consistente. Regras críticas terão testes unitários/integrados e os fluxos principais terão teste ponta a ponta.

PostgreSQL é o banco previsto; relações devem ter integridade referencial. A API deve manter contrato HTTP/JSON compatível e oferecer health check. Critérios de desempenho, disponibilidade, retenção e observabilidade ainda não foram definidos.

## Autenticação

OAuth 2.0 foi escolhido apenas como framework/protocolo de autorização. Ainda falta decidir se haverá login federado, OIDC, provedor, tipo de cliente, fluxo, scopes, tokens, cookies/sessões, logout, renovação, onboarding e recuperação de acesso. Não implementar autenticação antes dessas decisões.

## Pendências que bloqueiam implementação segura

- fluxo de entrada: cadastro, criação de empresa ou convite;
- provedor e desenho concreto de identidade;
- matriz final de permissões do `OPERATOR`;
- transporte técnico da empresa ativa;
- campos finais de clientes e regras fiscais;
- filtros, paginação, moeda, calendário e fuso;
- reversão de estoque ao cancelar pedido;
- meios de pagamento e retenção histórica;
- versionamento e validação do contrato com o frontend.

## Estados

- **Especificado:** documentado, mas não implementado.
- **Implementado:** confirmado em código e teste.
- **Por definir:** exige decisão ou critério adicional.