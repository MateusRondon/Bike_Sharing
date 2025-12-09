from google.colab import files

uploaded = files.upload()

for fn in uploaded.keys():
  print('User uploaded file "{name}" with length {length} bytes'.format(
      name=fn, length=len(uploaded[fn])))


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 1. Carregar o dataset (Certifique-se de usar o arquivo 'hour.csv' do dataset Bike Sharing)
# Se estiver no Colab, faça o upload do arquivo primeiro
df = pd.read_csv('hour.csv')

# Configuração de estilo dos gráficos
sns.set_style("whitegrid")

# --- A. Visão Geral dos Dados ---
print("--- Informações do Dataset ---")
print(df.info())
print("\n--- Estatísticas Descritivas ---")
print(df.describe())

# --- B. Distribuição da Variável Alvo (cnt - contagem de bikes) ---
plt.figure(figsize=(10, 5))
sns.histplot(df['cnt'], kde=True, bins=30, color='blue')
plt.title('Distribuição da Quantidade de Aluguéis (cnt)')
plt.xlabel('Total de Aluguéis')
plt.show()

# --- C. Correlação (Quais variáveis explicam o aluguel?) ---
# Vamos focar nas variáveis numéricas principais
cols_corr = ['temp', 'atemp', 'hum', 'windspeed', 'cnt']
plt.figure(figsize=(8, 6))
sns.heatmap(df[cols_corr].corr(), annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Mapa de Calor de Correlação')
plt.show()

# --- D. Análise Sazonal e Temporal ---
# 1. Aluguéis por Hora do Dia (O padrão mais forte neste dataset)
plt.figure(figsize=(12, 6))
sns.boxplot(x='hr', y='cnt', data=df, palette='viridis')
plt.title('Distribuição de Aluguéis por Hora do Dia')
plt.xlabel('Hora')
plt.ylabel('Contagem de Bikes')
plt.show()

# 2. Impacto da Estação do Ano
plt.figure(figsize=(8, 5))
sns.barplot(x='season', y='cnt', data=df, errorbar=None, palette='magma')
plt.xticks(ticks=[0, 1, 2, 3], labels=['Inverno', 'Primavera', 'Verão', 'Outono']) # Ajuste conforme a doc do dataset
plt.title('Média de Aluguéis por Estação')
plt.show()