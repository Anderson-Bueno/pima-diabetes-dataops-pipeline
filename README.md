# Diabetes Risk Prediction Pipeline

**DataOps, Model Validation & MLOps Foundation**

---

## 🔎 Visão Geral

Este projeto apresenta a construção de um pipeline estruturado para análise e preparação de dados clínicos da base **Pima Indians Diabetes**, com evolução planejada para modelagem preditiva, validação de modelos e entrega futura em arquitetura MLOps.

A proposta não é apenas criar uma análise pontual, mas organizar um fluxo reprodutível que conecte:

- ingestão de dados;
- transformação com Python e SQL;
- validação de qualidade;
- preparação para modelagem;
- avaliação preditiva;
- geração de artefatos;
- fundação para deploy e MLOps.

Este projeto foi reposicionado como um case de **Machine Learning Engineering aplicado**, partindo de um pipeline de DataOps/Data Engineering e evoluindo para um sistema preditivo de risco de diabetes.

---

## 📌 Problema de Negócio

Em contextos de saúde preventiva, identificar pacientes com maior risco de diabetes pode apoiar decisões clínicas, triagens e estratégias de acompanhamento.

Bases clínicas, no entanto, frequentemente apresentam desafios como:

- dados ausentes ou inconsistentes;
- variáveis clínicas em escalas diferentes;
- necessidade de regras explícitas de transformação;
- risco de interpretações equivocadas;
- necessidade de rastreabilidade;
- impacto crítico de falsos negativos.

A base utilizada neste projeto permite explorar um problema supervisionado de classificação, no qual o objetivo final é estimar o risco de diabetes a partir de variáveis clínicas e biométricas.

### Pergunta central

> Como construir um pipeline reprodutível para preparar dados clínicos, aplicar regras de negócio, treinar modelos preditivos e gerar artefatos reutilizáveis para uma futura arquitetura MLOps?

---

## 🎯 Objetivos

Os objetivos principais deste projeto são:

- estruturar um pipeline de dados com Python, SQLite e SQL;
- aplicar regras de negócio de forma auditável;
- preparar dados para consumo analítico e modelagem;
- validar problemas de qualidade dos dados;
- evoluir para treinamento de modelo preditivo;
- avaliar métricas de classificação;
- gerar artefatos de modelo e avaliação;
- preparar o projeto para evolução com MLflow, FastAPI, Docker e CI/CD.

---

## ✅ Escopo Atual do Projeto

A versão atual implementa uma camada de **DataOps/Data Engineering**, responsável por:

- ler a base Pima Indians Diabetes;
- filtrar pacientes com idade superior a 50 anos;
- criar uma classificação de perfil baseada no IMC;
- persistir os dados intermediários em SQLite;
- aplicar transformações utilizando SQL;
- exportar o resultado final em CSV;
- documentar regras de negócio e limitações de qualidade dos dados.

Essa etapa representa a fundação do pipeline, garantindo organização, rastreabilidade e reprodutibilidade antes da adição da camada preditiva.

---

## 🚀 Evolução para Machine Learning / MLOps

A próxima camada do projeto expande o pipeline para um fluxo preditivo completo.

A evolução proposta inclui:

- validação dos dados de entrada;
- pré-processamento para modelagem;
- separação treino/teste;
- treinamento de modelo supervisionado;
- avaliação com métricas adequadas;
- geração de artefatos;
- salvamento do modelo treinado;
- preparação para tracking com MLflow;
- possibilidade de consumo via API com FastAPI;
- containerização com Docker.

Com isso, o projeto passa de um pipeline analítico para uma fundação de **Machine Learning em produção**.

---

## 🏗️ Arquitetura da Solução

### Camada atual — DataOps / Data Engineering

```text
data/raw/diabetes.csv
        ↓
Python / Pandas ingestion
        ↓
SQLite staging table
        ↓
SQL business rules
        ↓
data/processed/resultado.csv
