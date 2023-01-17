import plotly.express as px

def get_linetotal(data):
    fig = px.line(data, x="Fecha", y="Casos totales", title='Casos Totales Acumulados',color_discrete_sequence = ['red'])
    return fig

def get_linetotalComunas(data, comuna):
    data= data.loc[data["Comuna"] == comuna, ["Codigo region","Comuna", "Codigo comuna", "Fecha", "Casos"]]
    fig = px.line(data, x="Fecha", y="Casos", title='Casos Confirmados Acumulados',color_discrete_sequence = ['red'], height=250)
    fig.update_layout(
    paper_bgcolor='rgb(248, 248, 255)',
    plot_bgcolor='rgb(248, 248, 255)',
    margin=dict(l=10, r=10, t=50, b=20),
    #showlegend=False,
    #font_color="blue",
    #title_font_color="blue",
    title={
        'text': "Casos Confirmados Acumulados",
        'y':0.95,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'}
    )
    return fig

def get_linetotalFallecidos(data, comuna):
    data= data.loc[data["Comuna"] == comuna, ["Codigo region","Comuna", "Codigo comuna", "Fecha", "Fallecidos"]]
    fig = px.line(data, x="Fecha", y="Fallecidos", title='Fallecidos Acumulados',color_discrete_sequence = ['red'], height=250)
    
    fig.update_layout(
    paper_bgcolor='rgb(248, 248, 255)',
    plot_bgcolor='rgb(248, 248, 255)',
    margin=dict(l=10, r=10, t=50, b=20),
    #showlegend=False,
    #font_color="blue",
    #title_font_color="blue",
    title={
        'text': "Casos Fallecidos Acumulados",
        'y':0.95,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'}
    )
    return fig