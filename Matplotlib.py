# Exibir gráficos gerados por bibliotecas (Matplotlib, Seaborn, Plotly, etc.)
# Exemplo com Matplotlib:

import matplotlib.pyplot as plt

# Dados de exemplo
x = [1, 2, 3, 4, 5]
y = [10, 20, 25, 30, 40]

# Criar um gráfico
plt.plot(x, y, marker='o')
plt.title("Gráfico de Linha")
plt.xlabel("Eixo X")
plt.ylabel("Eixo Y")
plt.show()  # Exibe o gráfico
