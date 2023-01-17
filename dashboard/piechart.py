import plotly.express as px
import pandas as pd

def get_pie(data, comuna, dosis):
    data = data.loc[(data['Comuna'] == comuna) & (data['Dosis'] == dosis)]
    datavacunas1 = data[["Region", "Codigo region", 'Comuna', 'Codigo comuna', 'Total']]
    datavacunas1 = datavacunas1.assign(Estado='Vacunados')
    datavacunas2 = data[["Region", "Codigo region", 'Comuna', 'Codigo comuna', 'NoVacunados']]
    datavacunas2 = datavacunas2.assign(Estado='No Vacunados')
    datavacunas2=datavacunas2.rename(columns = {'NoVacunados': 'Total'}, inplace = False)
    data = pd.concat([datavacunas1, datavacunas2])
    fig = px.pie(data, values='Total', names='Estado',color='Estado',color_discrete_map={'Vacunados':'green','No Vacunados':'Red'}, height=300)
    #fig.update_traces(showlegend=False, selector=dict(type='pie'))
    fig.update_traces(showlegend=False,textposition = 'inside' , textinfo = 'percent+label',marker = dict(line=dict(color='#000000', width=2)))
    fig.update_layout(
    paper_bgcolor='rgb(248, 248, 255)',
    plot_bgcolor='rgb(248, 248, 255)',
    margin=dict(l=10, r=10, t=50, b=20),
    #showlegend=False,
    #font_color="blue",
    #title_font_color="blue",
    title={
        'text': f"Avance {dosis} Dosis",
        'y':0.95,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'}
    )
    
    return fig