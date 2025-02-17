#Exemplo com Plotly:

import plotly.express as px

# Dados de exemplo
data = px.data.iris()

# Criar um gráfico interativo
fig = px.scatter(data, x="sepal_width", y="sepal_length", color="species")

# Exibir o gráfico no Kaggle
fig.show()
