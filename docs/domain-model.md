# Modelo conceptual do domínio

Este modelo apresenta as relações principais do Cosmetics Hub em termos de produto. Os nomes em código são mantidos para facilitar a correspondência com o projeto; a descrição não é um catálogo de campos nem uma especificação completa do banco de dados.

## Entidades

- **`users`** representa pessoas com uma conta no sistema. A conta identifica a pessoa; a pertença e o papel numa empresa são representados separadamente.
- **`tenants`** representa as empresas que utilizam a plataforma. Os dados e a atividade comercial são organizados no contexto da empresa.
- **`tenant_users`** representa a associação entre uma pessoa e uma empresa, incluindo o papel dessa pessoa naquela empresa. A associação permite que uma pessoa pertença a mais de uma empresa e tenha um papel associado a cada pertença.
- **`customers`** representa clientes comerciais registados por uma empresa. São distintos das pessoas que têm contas de utilizador no sistema.

## Relações

Uma pessoa pode estar associada a várias empresas, e uma empresa pode ter várias pessoas associadas; `tenant_users` representa essa relação entre `users` e `tenants`. Uma empresa pode, por sua vez, manter vários `customers`.

## Âmbito

A descrição e o [diagrama conceptual](diagrams/domain-baseline.mmd) são referências introdutórias. Não enumeram todos os dados, tabelas, regras ou relações que possam existir na implementação atual ou futura.
