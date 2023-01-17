import plotly.express as px

def get_scatter(data, year):
    data_year = data[data.year== year]
    fig = px.scatter(data, x= "gdpPercap", y="lifeExp")
    return fig