import pandas as pd

dados = pd.read_csv("demanda_vendas_datatech.csv")

print(dados.shape)
print(dados.info())
print(dados.duplicated().sum())
print(dados[dados.duplicated(keep=False)])
print(dados.isnull().sum())
print(dados[dados["id_venda"].duplicated(keep=False)].sort_values("id_venda"))

dados_tratados = dados.copy()
dados_tratados = dados_tratados.drop_duplicates()
print("Novo formato:", dados_tratados.shape)