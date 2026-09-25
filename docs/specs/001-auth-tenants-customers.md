# Spec 001 — Auth, Tenants e Customers

<!-- ============================================================
     CONTEXTO: OBJETIVO
     ============================================================ -->

## Objetivo

Permitir que uma pessoa crie uma conta e uma empresa, se torne
automaticamente `ADMIN`, inicie sessão, selecione uma empresa ativa e
faça a gestão de clientes dessa empresa.

<!-- ============================================================
     CONTEXTO: ESCOPO
     ============================================================ -->

## Escopo

Esta spec cobre:

- cadastro inicial;
- criação da primeira empresa;
- atribuição do primeiro `ADMIN`;
- login e logout;
- seleção da empresa ativa;
- isolamento entre empresas;
- gestão inicial de clientes.

<!-- ============================================================
     CONTEXTO: ATORES
     ============================================================ -->

## Atores envolvidos

- Administrador da empresa;
- Operador da empresa;
- Utilizador não autenticado.

<!-- ============================================================
     CONTEXTO: PRIMEIRO ACESSO
     ============================================================ -->

## Primeiro acesso

No primeiro acesso, a pessoa informa:

<!-- CONTEXTO: DADOS DO UTILIZADOR -->

### Dados do utilizador

- nome obrigatório;
- email obrigatório;
- palavra-passe obrigatória.

<!-- CONTEXTO: DADOS DA EMPRESA -->

### Dados da empresa

- nome da empresa obrigatório.

<!-- CONTEXTO: FLUXO DE ONBOARDING -->

O fluxo deve ser:

1. A pessoa informa os dados do utilizador e da empresa.
2. O sistema valida os dados.
3. O sistema cria o utilizador.
4. O sistema cria a empresa.
5. O sistema cria o vínculo entre utilizador e empresa.
6. O sistema atribui `role = ADMIN` ao vínculo.
7. O sistema inicia a sessão.
8. O sistema define a empresa criada como ativa.
9. O sistema redireciona o utilizador para o dashboard.

<!-- CONTEXTO: TRANSAÇÃO DO ONBOARDING -->

A criação do utilizador, da empresa e do vínculo `ADMIN` deve ocorrer
numa única transação.

Se qualquer etapa falhar, nenhum dos registros deve permanecer no banco.

<!-- ============================================================
     CONTEXTO: ACESSO POSTERIOR
     ============================================================ -->

## Acesso posterior

Nos acessos seguintes:

1. O utilizador informa email e palavra-passe.
2. O sistema valida as credenciais.
3. O sistema inicia uma sessão segura.
4. O sistema lista as empresas associadas ao utilizador.
5. O utilizador seleciona uma empresa ativa.
6. O sistema permite o acesso aos recursos autorizados.

<!-- CONTEXTO: UTILIZADOR COM UMA ÚNICA EMPRESA -->

Se o utilizador estiver associado a apenas uma empresa, ela pode ser
selecionada automaticamente.

<!-- CONTEXTO: UTILIZADOR SEM EMPRESA -->

Se o utilizador não estiver associado a nenhuma empresa, deve ser
encaminhado para o fluxo de criação da primeira empresa.

<!-- ============================================================
     CONTEXTO: AUTENTICAÇÃO
     ============================================================ -->

## Autenticação

A autenticação do MVP utiliza sessão através de cookie `HttpOnly`.

<!-- CONTEXTO: REGRAS DE AUTENTICAÇÃO -->

Regras:

- a palavra-passe deve ser armazenada apenas como hash;
- o cookie não pode ser acessível por JavaScript;
- rotas privadas exigem uma sessão válida;
- o logout deve invalidar ou encerrar a sessão;
- mensagens de erro não devem revelar se o email está cadastrado.

<!-- ============================================================
     CONTEXTO: EMPRESA ATIVA
     ============================================================ -->

## Empresa ativa

O frontend envia a empresa ativa no header:

```text
X-Tenant-ID: <id-da-empresa>