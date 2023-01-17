import plotly.express as px

def get_scatter(data, year):
    data_year = data[data.year== year]
    fig = px.scatter(data_year, x= "gdpPercap", y="lifeExp")
    return fig

def get_bubble(data, region):
    data = data[data.Region == region]
    fig = px.scatter(data, x='Casos', y= 'Fallecidos', 
           hover_data=['Comuna', 'Fecha'],
           color='Fallecidos', size= 'Fallecidos', size_max=50, 
           log_x=True, log_y=True, height=300, color_continuous_scale=px.colors.sequential.Rainbow,)
    
    fig.update_layout(
    paper_bgcolor='rgb(248, 248, 255)',
    plot_bgcolor='rgb(248, 248, 255)',
    margin=dict(l=10, r=10, t=50, b=20),
    #showlegend=False,
    #font_color="blue",
    #title_font_color="blue",
    title={
        'text': "Confirmados vs Fallecidos",
        'y':0.95,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'}
    )
    
    return fig