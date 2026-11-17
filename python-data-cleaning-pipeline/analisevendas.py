# Importa a biblioteca Pandas
import pandas as pd

# Lê o arquivo CSV e carrega os dados
dados = pd.read_csv("vendas.csv")

# Cria uma cópia para trabalhar sem alterar os dados originais
dados_tratados = dados.copy()

# Exibe as cinco primeiras linhas
print(dados_tratados.head())

print(dados)

print(dados.head())
print(dados.shape)
print(dados.info())
print(dados.duplicated().sum())
print(dados[dados.duplicated(keep=False)])
print(dados.isnull().sum())
print(dados[dados["quantidade"] <= 0])
print(dados[dados["preco_unitario"] <= 0])
print(dados[dados["quantidade"] > 1])
print(dados[dados["produto"] == "Mouse"])

# Remove registros completamente duplicados
dados_tratados = dados_tratados.drop_duplicates()

# Verifica quantas linhas temos após a remoção
print("Total de registros:", len(dados_tratados))

# Verifica os valores ausentes na cópia tratada
print(dados_tratados.isnull().sum())

print(dados_tratados[dados_tratados["produto"].isnull()])

# Separa os registros com produto não informado
pendencias = dados_tratados[dados_tratados["produto"].isnull()]

print("Registros pendentes de confirmação:")
print(pendencias)

# Separa vendas com quantidade igual ou menor que zero
vendas_suspeitas = dados_tratados[dados_tratados["quantidade"] <= 0]

print("Vendas com quantidade suspeita:")
print(vendas_suspeitas)

# Cria uma coluna para classificar os registros
dados_tratados["status"] = "VALIDO"

print(dados_tratados)

# Classifica registros com produto não informado
dados_tratados.loc[
    dados_tratados["produto"].isnull(), "status"
] = "PENDENTE"

# Classifica registros com quantidade igual a zero
dados_tratados.loc[
    dados_tratados["quantidade"] <= 0, "status"
] = "SUSPEITO"

print(dados_tratados)

print(dados_tratados["status"].value_counts())

# Separa somente os registros válidos
dados_validos = dados_tratados[dados_tratados["status"] == "VALIDO"]

# Exporta os registros válidos para um novo CSV
dados_validos.to_csv("vendas_validas.csv", index=False)

print("Arquivo vendas_validas.csv gerado com sucesso!")

print(dados_validos)

dados = pd.read_csv("vendas.csv")
# e na hora de salvar:
dados_validos.to_csv("vendas_validas.csv", index=False)