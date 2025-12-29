```markdown
 Pipeline de Dados – Classificação de Pacientes por IMC (Python + SQL)

 📌 Contexto e Definição do Problema

Este projeto foi desenvolvido a partir da definição do Problema P1, 
cujo objetivo é construir um pipeline de dados utilizando Python, Banco de Dados e SQL, capaz de:

- Ler um dataset de pacientes (base Pima Indians Diabetes);
- Filtrar apenas pacientes com idade superior a 50 anos;
- Criar uma nova coluna de classificação de perfil baseada no IMC (BMI):
  - Normal → IMC < 30  
  - Obeso → IMC ≥ 30
- Persistir os dados intermediários em um banco de dados;
- Aplicar as transformações utilizando SQL;
- Exportar o resultado final em formato CSV para consumo analítico.

O foco do problema não é apenas a análise, mas a organização, reprodutibilidade e clareza do pipeline,
aproximando o exercício de um cenário real de Data Engineering / DataOps.



 🏗️ Arquitetura da Solução

A solução foi estruturada como um pipeline simples, modular e reprodutível:

```

┌──────────────┐
│  Dataset CSV │
│ (Raw Data)   │
└──────┬───────┘
│






▼
┌──────────────────┐
│ Python (Pandas)  │
│ Ingestão         │
└──────┬───────────┘
│





▼
┌──────────────────┐
│ Banco de Dados   │
│ SQLite           │
│ (Persistência)   │
└──────┬───────────┘
│






▼
┌──────────────────┐
│ SQL              │
│ Regras de Negócio│
│ Filtro + Perfil  │
└──────┬───────────┘
│







▼
┌──────────────────┐
│ CSV Final        │
│ (Processed Data) │
└──────────────────┘

````

Essa arquitetura reflete um fluxo comum em ambientes produtivos:
Python para orquestração, SQL para transformação e regras de negócio, e arquivos versionáveis como output.



 ⚙️ Tecnologias Utilizadas

- Python 3
- Pandas – ingestão e exportação de dados
- SQLite – banco relacional leve para persistência local
- SQL – aplicação das regras de negócio
- Git / GitHub – versionamento e portfólio



 ▶️ Como Executar o Pipeline

 1️⃣ Criar ambiente (opcional, mas recomendado)


python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
````

 2️⃣ Executar o pipeline ponta-a-ponta

```bash
python -m src.etl \
  --input_csv data/raw/diabetes.csv \
  --out_csv data/processed/resultado.csv
```

Ao final da execução, o arquivo abaixo será gerado:

```
data/processed/resultado.csv
```

contendo apenas pacientes com **idade > 50 anos** e a coluna adicional **Perfil**.



## 🧠 Decisões Técnicas e Justificativas

### Por que usar SQL para as transformações?

* Regras de negócio ficam **explícitas, auditáveis e versionáveis**;
* Facilita validação por times não Python (Analytics, BI, Data);
* Aproxima o exercício de cenários reais de produção.

### Por que SQLite?

* Zero dependência externa;
* Ideal para **demonstração local e portfólio**;
* A mesma lógica SQL é facilmente migrável para Postgres, MySQL ou BigQuery.

### Por que separar notebook de código?

* Notebooks são ótimos para **exploração**, mas frágeis para produção;
* O pipeline em `src/etl.py` é **determinístico, testável e automatizável**;
* Reflete boas práticas de DataOps.



## 🔍 Qualidade de Dados e Limitações

Durante o desenvolvimento, alguns pontos importantes de qualidade de dados foram identificados:

* No dataset original, valores **0 em colunas como BMI** representam, na prática, **dados ausentes**;
* Pela definição original do problema, esses registros foram mantidos;
* Em um cenário produtivo, recomenda-se:

  * Tratar BMI = 0 como `NULL`;
  * Aplicar regras de imputação ou descarte;
  * Versionar essas decisões como regras de negócio explícitas.

📌 **Impacto**: pacientes com BMI = 0 são classificados como `Normal`, o que pode subestimar o risco real.



## 📊 Outputs e Insights Acionáveis

A partir do arquivo final (`resultado.csv`), é possível observar:

* No recorte de pacientes com **idade acima de 50 anos**, há uma **alta concentração de indivíduos classificados como Obesos**;
* A taxa de diabetes tende a ser **significativamente maior em pacientes obesos**;
* Esse tipo de classificação simples já permite:

  * Priorização de acompanhamento clínico;
  * Estratificação de risco;
  * Integração com modelos preditivos futuros.



## 🚀 Roadmap de Evolução

Este projeto pode ser expandido para um cenário corporativo real:

### 🔹 Persistência e Escala

* Migrar de SQLite para **PostgreSQL**
* Armazenar outputs em **Amazon S3**

### 🔹 Transformações Analíticas

* Introduzir **dbt** para versionamento de modelos SQL
* Documentar métricas e regras de negócio

### 🔹 Orquestração

* Agendar o pipeline com **Apache Airflow**
* Execuções batch diárias ou semanais

### 🔹 Qualidade e Confiabilidade

* Criar **testes automatizados** (pytest)
* Validar schema e regras de negócio

### 🔹 CI/CD

* Pipeline de CI para lint, testes e validação
* Deploy automatizado via GitHub Actions

```
