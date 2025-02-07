import seaborn as sns
import pandas as pd

# Dados de exemplo
data = pd.DataFrame({
    'x': [1, 2, 3, 4, 5],
    'y': [10, 20, 25, 30, 40]
})

# Criar um gráfico
sns.lineplot(data=data, x='x', y='y', marker='o')
plt.title("Gráfico de Linha com Seaborn")
plt.show()  # Exibe o gráfico
