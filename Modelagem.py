import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Certifique-se de que o dataframe 'df' já foi carregado anteriormente
# df = pd.read_csv('hour.csv')

# Configuração de estilo para os gráficos ficarem mais profissionais
sns.set_style("whitegrid")

# --- 1. Matriz de Correlação e Heatmap ---
# Calculando a correlação apenas para colunas numéricas
corr_matrix = df.corr(numeric_only=True)

plt.figure(figsize=(12, 10))
# Plotando o Heatmap
sns.heatmap(corr_matrix,
            annot=True,
            cmap='coolwarm',
            fmt=".2f",
            linewidths=0.5)
plt.title("Matriz de Correlação - Destaque para Multicolinearidade", fontsize=16)
plt.show()

# --- 2. Scatterplot: Temperatura vs Total de Aluguéis ---
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df,
                x='temp',
                y='cnt',
                hue='season',
                palette='viridis',
                alpha=0.6) # alpha ajuda a ver a densidade dos pontos

# Ajustando as legendas dos eixos e título
plt.title("Relação entre Temperatura e Aluguéis (cnt)", fontsize=16)
plt.xlabel("Temperatura Normalizada", fontsize=12)
plt.ylabel("Total de Aluguéis (cnt)", fontsize=12)

# Melhorando a legenda da estação (Season)
# O dataset original usa 1:Inverno, 2:Primavera, 3:Verão, 4:Outono (ajuste conforme a documentação exata do UCI)
handles, labels = plt.gca().get_legend_handles_labels()
plt.legend(handles=handles, title='Estação', labels=['1', '2', '3', '4'])

plt.show()