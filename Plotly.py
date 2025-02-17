#Exemplo com Plotly:

import plotly.express as px

# Dados de exemplo
data = px.data.iris()

# Criar um gráfico interativo
fig = px.scatter(data, x="sepal_width", y="sepal_length", color="species")

# Exibir o gráfico no Kaggle
fig.show()


#Manipulando Dados no Plotly

#Add Métricas personalizadas

import plotly.express as px

# Dados de exemplo
data = px.data.iris()

# Criar um gráfico interativo
fig = px.scatter(
    data, 
    x="sepal_width", 
    y="sepal_length", 
    color="species",  # Cores baseadas na coluna "species"
    labels={
        "sepal_width": "Largura da Sépala (cm)",  # Nome do eixo X
        "sepal_length": "Comprimento da Sépala (cm)",  # Nome do eixo Y
        "species": "Espécie"  # Nome da legenda
    },
    title="Gráfico de Dispersão: Comprimento vs Largura da Sépala"  # Título do gráfico
)

# Exibir o gráfico
fig.show()



# Personalização adicional
fig.update_layout(
    title_font_size=20,  # Tamanho da fonte do título
    title_font_color="blue",  # Cor do título
    legend_title_font_color="green",  # Cor do título da legenda
    xaxis_title_font_size=14,  # Tamanho da fonte do eixo X
    yaxis_title_font_size=14,  # Tamanho da fonte do eixo Y
    legend=dict(x=0.8, y=0.9)  # Posição da legenda
)

# Exibir o gráfico
fig.show()
