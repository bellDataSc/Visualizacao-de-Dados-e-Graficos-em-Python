#Essa opção que será removida em versões futuras do Pandas
#Para silenciar o aviso add 'warnings'

import warnings
warnings.filterwarnings("ignore", category=FutureWarning)


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt  # Importando matplotlib

# Criar um DataFrame de exemplo
data = pd.DataFrame({'x': [1, 2, 3, 4, 5], 'y': [10, 20, 25, 30, 50]})

# Criar um gráfico
sns.lineplot(data=data, x='x', y='y', marker='o')

# Adicionar título e exibir o gráfico
plt.title("Gráfico de Linha com Seaborn")
plt.show()
