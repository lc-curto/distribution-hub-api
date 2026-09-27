# Princípios de documentação

Esta página registra os critérios usados para organizar e revisar a documentação do Cosmetics Hub.

## Tipos de informação

- **Objetivo de negócio:** por que o produto existe e que necessidade atende.
- **Regra de negócio:** condição ou política que deve permanecer verdadeira para a operação, independentemente da tecnologia.
- **Requisito:** comportamento, qualidade ou restrição que o sistema precisa satisfazer; deve ter origem e uma forma observável de validação.
- **Decisão técnica:** escolha de como construir ou organizar a solução, com contexto e consequências. Decisões significativas são registradas em [ADRs](architecture/decisions/).

Uma regra responde “o que precisa ser verdade para o negócio?”. Um requisito responde “o que o sistema deve permitir ou garantir?”. Uma decisão técnica responde “como a solução será construída?”.

## Clareza e estado

1. Escreva para o leitor, explique siglas na primeira ocorrência e use os mesmos termos em todos os documentos.
2. Dê identificadores aos requisitos e às regras para permitir referência e teste.
3. Diferencie o que está implementado, especificado, aceito como decisão e ainda por definir.
4. Prefira critérios verificáveis a expressões vagas como “rápido”, “simples” ou “seguro” sem medida.
5. Mostre a arquitetura em níveis; comece pelo contexto e acrescente detalhes quando responderem a uma pergunta concreta.
6. Em React não há uma estrutura universal obrigatória. Este projeto organiza páginas por rota e componentes compartilhados por tipo, sem diretório `features/`, conforme preferência expressa para este repositório.

## Referências consultadas

- [NASA — How to Write a Good Requirement](https://www.nasa.gov/reference/appendix-c-how-to-write-a-good-requirement/): clareza, necessidade, rastreabilidade e verificabilidade.
- [IREB — Glossário de engenharia de requisitos](https://cpre.ireb.org/en/downloads-and-resources/glossary): vocabulário de requisitos.
- [ISO/IEC/IEEE 29148](https://standards.ieee.org/standard/29148-2018.html): processos e artefatos de engenharia de requisitos.
- [OMG SBVR](https://www.omg.org/spec/SBVR/1.5/About-SBVR): vocabulário e regras de negócio.
- [ISO/IEC/IEEE 42010](https://standards.ieee.org/ieee/42010/6846/): descrição arquitetural e preocupações dos interessados.
- [C4 Model](https://c4model.com/diagrams): diagramas em diferentes níveis de abstração.
- [Diátaxis](https://diataxis.fr/): separar tutoriais, guias, referência e explicações.
- [React — File Structure](https://legacy.reactjs.org/docs/faq-structure.html): opções de organização, sem estrutura única prescrita.
- [Google Developer Documentation Style Guide](https://developers.google.com/style): clareza e consistência para documentação técnica.
- [RFC 6749](https://www.rfc-editor.org/rfc/rfc6749.html), [RFC 9700](https://www.rfc-editor.org/rfc/rfc9700.html) e [OpenID Connect Core](https://openid.net/specs/openid-connect-core-1_0.html): referências para a decisão de autenticação, não substitutos de requisitos de produto.

Essas referências orientam a forma de documentar; não aprovam automaticamente requisitos ou decisões do Cosmetics Hub.