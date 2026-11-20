<div align="center">

  <p>─────────────────────── ✦ ───────────────────────</p>

  <h1>˚₊‧꒰ა Pipeline de Limpeza de Dados em Python ໒꒱‧₊˚</h1>

  <p>
    <i>Pipeline automatizado em Python com Pandas via linha de comando para auditar, validar, classificar e exportar registros de vendas.</i>
  </p>

  <p>
    <img src="https://img.shields.io/badge/Python-FFB7C5?style=for-the-badge&logo=python&logoColor=white" alt="Python" />
    <img src="https://img.shields.io/badge/Pandas-E6E6FA?style=for-the-badge&logo=pandas&logoColor=555555" alt="Pandas" />
    <img src="https://img.shields.io/badge/Engenharia%20de%20Dados-FFD1DC?style=for-the-badge&logo=databricks&logoColor=white" alt="Engenharia de Dados" />
    <img src="https://img.shields.io/badge/ETL-Pipeline-E6E6FA?style=for-the-badge&logo=pandas&logoColor=555555" alt="ETL" />
  </p>

</div>

<br/>

### ✦ Resumo

Automatiza a leitura, inspeção, auditoria de qualidade, remoção de duplicatas, classificação de status e exportação de dados de vendas em CSV a partir de um script em Python com Pandas.

### ✦ Tecnologias

- **Python 3.x:** Linguagem principal para execução do pipeline via linha de comando e orquestração das etapas de processamento.
- **Pandas:** Biblioteca utilizada para leitura e escrita de CSV (`read_csv`, `to_csv`), inspeção (`shape`, `info`, `head`), auditoria (`isnull`, `duplicated`) e limpeza (`drop_duplicates`).

### ✦ Regras

O pipeline aplica verificações e transformações em quatro etapas sobre os registros de vendas:

- **Ingestão e inspeção:** Carrega os dados brutos de um arquivo CSV e exibe dimensões (`.shape`), estrutura/tipos (`.info()`) e primeiras linhas (`.head()`).
- **Auditoria de qualidade:** Conta valores nulos por coluna (`.isnull().sum()`), identifica linhas duplicadas (`.duplicated()`) e verifica quantidades ou preços unitários negativos ou iguais a zero.
- **Limpeza e classificação:** Remove linhas duplicadas (`.drop_duplicates()`) e classifica cada registro com os status `VALIDO`, `PENDENTE` ou `SUSPEITO` conforme as regras aplicadas.
- **Exportação:** Filtra apenas os registros válidos e gera o arquivo `vendas_validas.csv` sem a coluna de índice (`index=False`).
<p align="center">─────────────────────── · ───────────────────────</p>

### ✦ Como Executar

1. **Pré-requisitos:** Tenha o **Python 3.x** e a biblioteca **Pandas** instalados na máquina:
   ```bash
   pip install pandas
   ```
2. **Clone o repositório:**
   ```bash
   git clone [https://github.com/Madoard/python-data-cleaning-pipeline.git](https://github.com/Madoard/python-data-cleaning-pipeline.git)
   cd python-data-cleaning-pipeline
   ```
3. **Execute os scripts:**
   ```bash
   python analisevendas.py
   ```
   ```bash
   python analise.py
   ```

### ✦ Exemplo de Uso

```text
Total de registros: 14

Registros pendentes de confirmação:
...
Vendas com quantidade suspeita:
...
VALIDO      ...
PENDENTE    ...
SUSPEITO    ...

Arquivo vendas_validas.csv gerado com sucesso!
```

<p align="center">─────────────────────── · ───────────────────────</p>

### ✦ Como Foi Construído

Os scripts principais estão em [analisevendas.py](analisevendas.py) e [analise.py](analise.py), operando sobre arquivos CSV como `vendas.csv` e `demanda_vendas_datatech.csv`[cite: 1, 2]. Abaixo está a estrutura principal e como cada parte funciona:

```python
dados = pd.read_csv("vendas.csv")
dados_tratados = dados.copy()

dados_tratados = dados_tratados.drop_duplicates()

dados_tratados["status"] = "VALIDO"
dados_tratados.loc[dados_tratados["produto"].isnull(), "status"] = "PENDENTE"
dados_tratados.loc[dados_tratados["quantidade"] <= 0, "status"] = "SUSPEITO"

dados_validos = dados_tratados[dados_tratados["status"] == "VALIDO"]
dados_validos.to_csv("vendas_validas.csv", index=False)
```

- **Inspeção e auditoria com Pandas:** Lê os arquivos CSV com `pd.read_csv()` e avalia formato, tipos, duplicatas, valores ausentes e condições de negócio como `quantidade <= 0` e `preco_unitario <= 0`[cite: 1, 2].
- **Tratamento e classificação (`analisevendas.py`):** Trabalha sobre `dados.copy()`, remove linhas duplicadas com `.drop_duplicates()`, rotula os registros com `status` (`VALIDO`, `PENDENTE` e `SUSPEITO`) e filtra apenas os válidos para salvar em `vendas_validas.csv` com `index=False`[cite: 1].
- **Análise exploratória e duplicidade de chaves (`analise.py`):** Carrega `demanda_vendas_datatech.csv`, verifica duplicidades gerais e especificamente em `id_venda` (ordenando com `.sort_values("id_venda")`), remove duplicatas em uma cópia e exibe o novo formato do dataset[cite: 2].

<br/>

<div align="center">
  <p>°•. ✦ .•° ────── ꒰ ✦ ꒱ ────── °•. ✦ .•°</p>
  <p><i>Feito por <b>Eduarda Gonçalves</b></i></p>
</div>
