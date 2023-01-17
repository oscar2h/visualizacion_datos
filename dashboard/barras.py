import plotly.express as px
import pandas as pd

def get_barraRegion(data):
    fig = px.bar(data, x='Casos totales acumulados', y='Region', title="Casos Confirmados",color='Region')
    fig.update_layout(yaxis={'categoryorder':'total ascending'})
    return fig

def get_barraComunas(data, region, fecha):
    comunas= data.loc[data["Region"] == region, ["Comuna", "Codigo comuna", fecha]]
    comunas = comunas.rename({fecha: 'Confirmados'}, axis=1)
    fig = px.bar(comunas, x='Confirmados', y='Comuna', color='Comuna')
    fig.update_layout(yaxis={'categoryorder':'total ascending'})
    
    fig.update_layout(
    paper_bgcolor='rgb(248, 248, 255)',
    plot_bgcolor='rgb(248, 248, 255)',
    margin=dict(l=10, r=10, t=50, b=20),
    #showlegend=False,
    #font_color="blue",
    #title_font_color="blue",
    title={
        'text': "Casos Confirmados",
        'y':0.95,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'}
    )
    return fig