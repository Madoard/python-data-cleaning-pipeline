# python-data-cleaning-pipeline
<div align="center">

  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:FFD1DC,50:FFB7C5,100:E6E6FA&height=180&section=header&text=Data%20Cleaning%20Pipeline&fontSize=34&fontColor=ffffff&fontAlignY=38&desc=%E2%9C%A7%EF%BD%A5%EF%BE%9F:%20*Python%20•%20Pandas%20•%20ETL*%20:%EF%BD%A5%EF%BE%9F%E2%9C%A7&descSize=14&descAlignY=58&animation=twinkling" width="100%" alt="Header Banner" />

  <p>｡ﾟ☁︎｡⋆｡ ﾟ☾ ﾟ｡⋆ ──────────── ꒰ 🦢 ꒱ ──────────── ⋆｡ﾟ☾ ﾟ｡⋆｡☁︎｡ﾟ</p>

  <p>
    <img src="https://img.shields.io/badge/Python-FFB7C5?style=for-the-badge&logo=python&logoColor=white" alt="Python" />
    <img src="https://img.shields.io/badge/Pandas-E6E6FA?style=for-the-badge&logo=pandas&logoColor=555555" alt="Pandas" />
    <img src="https://img.shields.io/badge/Data%20Engineering-FFD1DC?style=for-the-badge&logo=databricks&logoColor=white" alt="Data Engineering" />
    <img src="https://img.shields.io/badge/Status-Completed-E6E6FA?style=for-the-badge&logoColor=555555" alt="Status" />
  </p>

</div>

<br/>

<p align="center">୨୧ ─────── ‧₊˚ ☁️⋅♡𓂃 ࣪ ִֶָ☾. ─────── ୨୧</p>

### <p align="center">˚₊‧꒰ა 🍓 About the Project 🍓 ໒꒱‧₊˚</p>

> ✧･ﾟ: *✧･ﾟ:* *Automated Python pipeline for data auditing, cleaning, and validation of sales datasets using Pandas.* *:･ﾟ✧*:･ﾟ✧

<div align="center">
  <p>🌷 <b>Welcome to my data cleansing & ETL repository!</b> 🌷</p>
  <p>This project features a robust script crafted to process raw sales records, handle structural anomalies, audit duplicate or suspicious entries, and export a clean, reliable dataset ready for analytical insights. ☁️✨</p>
</div>

<br/>

<p align="center">₊˚ʚ ᗢ₊˚✧ ﾟ. ─────── ꒰ 🪄 ꒱ ─────── .ﾟ ✧˚₊ᗢ ɞ˚₊</p>

### <p align="center">˚₊‧꒰ა 🛠️ ETL Pipeline Workflow ໒꒱‧₊˚</p>

- **📥 1. Ingestion & Initial Inspection:**
  - Loading the raw CSV dataset (`vendas.csv`) using `pandas.read_csv()`.
  - Checking structural dimensions (`.shape`), schema metadata (`.info()`), and previewing records (`.head()`).
- **🔍 2. Data Quality Audit:**
  - Mapping missing and null values (`.isnull().sum()`).
  - Identifying and counting completely duplicated rows (`.duplicated()`).
  - Auditing core business rules (e.g., negative or zero quantities and unit prices).
- **🧹 3. Cleaning & Classification:**
  - Removing full duplicate rows using `.drop_duplicates()`.
  - Creating an analytical **`status`** column to classify each record with precision:
    - 🟢 **`VALIDO`**: Clean and reliable data ready for consumption.
    - 🟡 **`PENDENTE`**: Records lacking critical product information.
    - 🔴 **`SUSPEITO`**: Rows containing logical anomalies (e.g., quantity $\le 0$).
- **📤 4. Secure Export:**
  - Isolating valid records (`dados_validos`).
  - Exporting to a new structured file (`vendas_validas.csv`) while omitting unnecessary indexes (`index=False`).

<br/>

<p align="center">୨୧ ─────── ‧₊˚ ☁️⋅♡𓂃 ࣪ ִֶָ☾. ─────── ୨୧</p>

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
