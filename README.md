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

<div align="center">
  <p><i>developed with 💗 and ☕ by <b>Maria Eduarda Gonçalves</b></i></p>
</div>
