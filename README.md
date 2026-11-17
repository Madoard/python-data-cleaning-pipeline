˚₊‧꒰ა 🌙 ໒꒱ ─── Ɛ 📖 ɜ ─── ꒰ა 🌙 ໒꒱‧₊

<div align="center">

  # °₊·εʋ 📓 Python Data Cleaning Pipeline 📓 ϭ3·₊°

  <p><i>✦·˚*·.* Command-line and automated Python data cleaning pipeline built with Pandas to audit, validate, and structure sales records *·.-°*·.✦</i></p>

  <p>
    <img src="https://img.shields.io/badge/PYTHON-3.X-FFB7C5?style=flat-square&logo=python&logoColor=white" alt="Python" />
    <img src="https://img.shields.io/badge/PANDAS-ETL-E6E6FA?style=flat-square&logo=pandas&logoColor=555555" alt="Pandas" />
    <img src="https://img.shields.io/badge/DATA-QUALITY-FFD1DC?style=flat-square&logo=databricks&logoColor=white" alt="Data Quality" />
    <img src="https://img.shields.io/badge/IN_MEMORY-PIPELINE-E6E6FA?style=flat-square&logoColor=555555" alt="Pipeline" />
  </p>

</div>

˚₊·☁︎ ·˖ ☾ ─── ⋆.ೃ࿔* ─── ☾ ·˖ ☁︎·₊

### ╰─► ε 📞 3 Pipeline Capabilities

The automated data cleaning script supports complete auditing and structural processing:

*   ₊˚🖊️ **Ingestion & Inspection ( Read ):** Loads raw CSV records via `pandas.read_csv()` and checks dataset dimensions (`.shape`), metadata (`.info()`), and head previews (`.head()`).
*   ₊˚🏷️ **Data Quality Audit:** 
    *   *Null Mapping:* Scans missing fields across columns using `.isnull().sum()`.
    *   *Duplication Check:* Identifies and filters fully repeated rows using `.duplicated()`.
    *   *Business Logic:* Audits negative or zero quantities and unit prices.
*   ₊˚📋 **Cleaning & Classification ( Update ):** 
    *   Removes duplicates via `.drop_duplicates()`.
    *   Assigns analytical statuses (`VALIDO`, `PENDENTE`, `SUSPEITO`) using conditional mapping.
*   ₊˚💾 **Secure Export ( Write ):** Filters clean rows and exports a structured dataset (`vendas_validas.csv`) omitting default indices (`index=False`).

˚₊·☁︎ ·˖ ☾ ─── ⋆.ೃ࿔* ─── ☾ ·˖ ☁︎·₊

### <p align="center">˚₊‧꒰ა 💻 Core Script ໒꒱‧₊˚</p>

```python
# Import Pandas library
import pandas as pd

# Load CSV dataset
dados = pd.read_csv("vendas.csv")

# Create a working copy to preserve raw data
dados_tratados = dados.copy()

# Remove fully duplicated rows
dados_tratados = dados_tratados.drop_duplicates()

# Create a status classification column
dados_tratados["status"] = "VALIDO"

# Classify records with missing info or logic anomalies
dados_tratados.loc[dados_tratados["produto"].isnull(), "status"] = "PENDENTE"
dados_tratados.loc[dados_tratados["quantidade"] <= 0, "status"] = "SUSPEITO"

# Filter valid records and export to a new clean CSV
dados_validos = dados_tratados[dados_tratados["status"] == "VALIDO"]
dados_validos.to_csv("vendas_validas.csv", index=False)

print("✨ Pipeline executed successfully! Clean dataset generated. 🌸")
