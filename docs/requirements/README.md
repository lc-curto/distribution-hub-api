# Requisitos e regras

Os documentos desta pasta descrevem comportamento desejado e restrições. Eles **não comprovam implementação**.

- [Requisitos funcionais](functional-requirements.md): capacidades que o sistema deve oferecer.
- [Regras de negócio](business-rules.md): condições que governam a operação comercial.
- [Requisitos não funcionais](non-functional-requirements.md): segurança, integridade, qualidade e operação.
- [Autenticação](authentication.md): escolha de OAuth 2.0 e limites ainda não definidos.
- [Questões em aberto](open-questions.md): lacunas que impedem decisões seguras de implementação.

## Estados usados

- `Especificado`: consta da documentação, mas não está implementado.
- `Implementado`: confirmado no código e teste; por enquanto, apenas alguns itens de infraestrutura e `GET /health`.
- `Por definir`: exige decisão ou critério adicional.

Os requisitos devem ganhar critérios de aceitação específicos quando forem refinados para uma entrega. Evite transformar uma pasta, dependência ou item de backlog em evidência de comportamento.