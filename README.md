<div align="center">
  ˚₊‧꒰ა 🌙 ໒꒱ ─── Ɛ 📖 ɜ ─── ꒰ა 🌙 ໒꒱‧₊
</div>

<div align="center">

  # °₊·εʋ 📓 Pipeline de Limpeza de Dados em Python 📓 ϭ3·₊°

  <p><i>✦·˚*·.* Pipeline de limpeza de dados em Python via linha de comando e automatizado construído com Pandas para auditar, validar e estruturar registros de vendas *·.-°*·.✦</i></p>

  <p>
    <img src="https://img.shields.io/badge/Python-FFB7C5?style=for-the-badge&logo=python&logoColor=white" alt="Python" />
    <img src="https://img.shields.io/badge/Pandas-E6E6FA?style=for-the-badge&logo=pandas&logoColor=555555" alt="Pandas" />
    <img src="https://img.shields.io/badge/Engenharia%20de%20Dados-FFD1DC?style=for-the-badge&logo=databricks&logoColor=white" alt="Engenharia de Dados" />
    <img src="https://img.shields.io/badge/ETL-Pipeline-E6E6FA?style=for-the-badge&logo=pandas&logoColor=555555" alt="ETL" />
  </p>

</div>

˚₊·☁︎ ·˖ ☾ ─── ⋆.ೃ࿔* ─── ☾ ·˖ ☁︎·₊

### ╰─► ε 📞 3 Capacidades do Pipeline

O script automatizado de limpeza de dados oferece auditoria completa e processamento estrutural:

-   ₊˚🖊️ **Ingestão e Inspeção ( Leitura ):** Carrega registros brutos em CSV via `pandas.read_csv()` e verifica dimensões do dataset (`.shape`), metadados (`.info()`) e prévia das primeiras linhas (`.head()`).
-   ₊˚🏷️ **Auditoria de Qualidade de Dados:** 
  -   *Mapeamento de Nulos:* Identifica campos ausentes nas colunas usando `.isnull().sum()`.
  -   *Verificação de Duplicatas:* Localiza e filtra linhas totalmente repetidas usando `.duplicated()`.
  -   *Regras de Negócio:* Audita quantidades e preços unitários negativos ou zerados.
-   ₊˚📋 **Limpeza e Classificação ( Atualização ):** 
  -   Remove duplicatas via `.drop_duplicates()`.
  -   Atribui status analíticos (`VALIDO`, `PENDENTE`, `SUSPEITO`) usando mapeamento condicional.
-   ₊˚💾 **Exportação Segura ( Escrita ):** Filtra as linhas válidas e exporta um dataset estruturado (`vendas_validas.csv`) omitindo os índices padrão (`index=False`).

˚₊·☁︎ ·˖ ☾ ─── ⋆.ೃ࿔* ─── ☾ ·˖ ☁︎·₊

<div align="center">
 ˚₊‧꒰ა 🌙 ໒꒱ ─── Ɛ 📖 ɜ ─── ꒰ა 🌙 ໒꒱‧₊
  <p><i>feito com 🩷 por <b>Maria Eduarda Gonçalves</b></i></p>
</div>
