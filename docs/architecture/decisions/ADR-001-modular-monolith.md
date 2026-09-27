# ADR-001 — API como monólito modular

**Estado:** Aceito
**Data da decisão original:** não registrada na fonte preservada. Revisado em 2026-09-27.

## Contexto

O produto precisa de uma API com módulos de negócio distintos, mas operar microserviços exige deploy, monitoramento e comunicação entre serviços que não são necessários para o escopo atual.

## Decisão

Manter uma única aplicação FastAPI, organizada internamente por módulos de domínio. A API não será dividida em microserviços sem uma necessidade concreta que justifique essa mudança.

## Consequências

- A implantação e a comunicação entre módulos permanecem simples.
- Os limites dos módulos devem evitar dependências cruzadas desnecessárias.
- A separação do frontend em outro repositório não altera a API para microserviços.
- O código atual ainda não implementa os módulos comerciais; a decisão descreve a arquitetura adotada, não funcionalidades já disponíveis.

## Reavaliação

Reavaliar se surgirem requisitos de escala, autonomia de implantação, isolamento operacional ou equipes que justifiquem serviços independentes.
