<div align="center">
  ˚₊‧꒰ა 🌙 ໒꒱ ─── Ɛ 📖 ɜ ─── ꒰ა 🌙 ໒꒱‧₊
</div>

<div align="center">

  # °₊·εʋ 📓 Python Data Cleaning Pipeline 📓 ϭ3·₊°

  <p><i>✦·˚*·.* Command-line and automated Python data cleaning pipeline built with Pandas to audit, validate, and structure sales records *·.-°*·.✦</i></p>

  <p>
    <img src="https://img.shields.io/badge/Python-FFB7C5?style=for-the-badge&logo=python&logoColor=white" alt="Python" />
    <img src="https://img.shields.io/badge/Pandas-E6E6FA?style=for-the-badge&logo=pandas&logoColor=555555" alt="Pandas" />
    <img src="https://img.shields.io/badge/Data%20Engineering-FFD1DC?style=for-the-badge&logo=databricks&logoColor=white" alt="Data Engineering" />
    <img src="https://img.shields.io/badge/ETL-Pipeline-E6E6FA?style=for-the-badge&logoColor=555555" alt="ETL" />
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
   ˚₊‧꒰ა 🌙 ໒꒱ ─── Ɛ 📖 ɜ ─── ꒰ა 🌙 ໒꒱‧₊
  <p><i>made with 🩷 by **Maria Eduarda Gonçalves**</i></p>
</div>
