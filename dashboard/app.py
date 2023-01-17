from dash import Dash, html, dcc, Input, Output
import dash_bootstrap_components as dbc
import os
from wordcloud import WordCloud
from data import dataTotalRegion, dataTotal, dataTotalComunas, dataTotalComunas2, dataTotalFallecidos,datasintomas, df_casos_fallecidos_actual, datavacunas
from scatter import get_scatter, get_bubble
from piechart import get_pie
from heatmap import get_heatmap
from barras import get_barraRegion, get_barraComunas
from line import get_linetotal, get_linetotalComunas, get_linetotalFallecidos
from wordcloudd import get_wordcloud
from openpyxl import Workbook
from mapa import get_mapa
from utils import get_kpi
import requests
from datetime import datetime

is_gunicorn = "gunicorn" in os.environ.get("SERVER_SOFTWARE", "")
if is_gunicorn:
    grupo = os.environ.get("GRUPO", "")
    requests_pathname_prefix = f"/{ grupo }"
else:
    requests_pathname_prefix = "/"

app = Dash(__name__, 
           requests_pathname_prefix=requests_pathname_prefix,
           #external_stylesheets=[dbc.themes.BOOTSTRAP],
           external_stylesheets=[dbc.themes.CERULEAN],
          )
colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}

server = app.server

#date = datetime.today().strftime('%Y-%m-%d')
date = '2022-08-26'
app.layout = dbc.Container(
    children=[
        dbc.Row([
                dbc.Col(html.Div(
                    [html.H1('COVID-19: Situación Actual por Región', style={'color': 'White','textAlign': 'center','backgroundColor':'rgb(15, 105, 180)'}),
                     html.H2(f'{date}', style={'color': 'White','textAlign': 'center','backgroundColor':'rgb(235, 60, 70)'}),
                     html.Div(
                         [html.P('El objetivo de las siguientes visualizaciones es mantener informado a las distintas instituciones de gobierno, privados y población en general sobre la situación actual en la que se encuentra la pandemia por Covid-19 en Chile.',style={'fontSize': 20}),
                          html.P("La información es desplegada a nivel regional, con datos de casos confirmados y fallecidos. A nivel comunal con datos de la evolución histórica de casos confirmados y fallecidos, además de informar el avance de las distintas dosis de vacunas a la fecha.",style={'fontSize': 20}),
                          html.P("Los datos visualizados son oficiales, los cuales reportados por el Ministerio de Salud en sus reportes diarios de Covid-19. Fuente: https://github.com/MinCiencia/Datos-COVID19",style={'fontSize': 20})
                         ])
                    ]))
        ]
        ),
        #dbc.Row(dbc.Col(html.Div(
        #    html.H3('Casos Confirmados Región: ', style={'color': 'White','textAlign': 'center','backgroundColor':'blue'})
        #)
        #               )
        #),
        dbc.Row([html.Div(id = 'titRegion')]), 
        dbc.Row(
            [
                dcc.Dropdown(
                id='selectRegion', options = [{"label": region, "value": region} 
                                         for region in dataTotalComunas.Region.unique()],
                value = 'Biobío',style={
                'width': '50%'
            }),
            ],
        ),
        dbc.Row(
            [
                dbc.Col(dcc.Graph(id="BarraComunas")
                ),
                dbc.Col(dcc.Graph(id="Mapa")
                ),                
            ],
            align="center",
        ),
        dbc.Row(html.H3("   ")),
        dbc.Row(
            [
                #dbc.Col(dcc.Graph(id="wordcloud_sintomas", figure =get_wordcloud(datasintomas)),
                dbc.Col(dcc.Graph(id="burbujas"),
                #dbc.Col(
                ),
            ],
            align="center",
        ),
        dbc.Row(html.H3("   ")),
        #dbc.Row(dbc.Col(html.H3('Evolución Casos Confirmados y Fallecidos Comuna: ', style={'color': 'White','textAlign': 'center','backgroundColor':'blue'}),),
        #),
        dbc.Row([html.Div(id = 'titComuna')]), 
        dbc.Row(
            [
                dcc.Dropdown(
                id='selectComuna', options = [], style={'width': '50%'}
                ),
            ],
        ),
        dbc.Row(
            [
                dbc.Col(dcc.Graph(id="lineaComunas"),
                ),
                dbc.Col(dcc.Graph(id="lineaFallecidos"),
                ),
            ],
            align="center",
        ),
        dbc.Row(html.H3("   ")),
        dbc.Row(dbc.Col(html.H3('Avance Vacunación vs Población Objetivo', style={'color': 'White','textAlign': 'center','backgroundColor':'rgb(77, 77, 77)'}),),
        ),
        dbc.Row(
            [
                dbc.Col(dcc.Graph(id="PieVacunados"),
                ),
                dbc.Col(dcc.Graph(id="PieVacunadosd2"),
                ),
                dbc.Col(dcc.Graph(id="PieVacunadosd4"),
                ),
                dbc.Col(dcc.Graph(id="PieVacunadosdRefuerzo"),
                ),
            ],
            align="center",
        ),
    ]
)

@app.callback(
    Output('selectComuna', 'options'),
    Input('selectRegion', 'value')
)
def set_comunas_lista(SeleccionarComuna):
    dff = dataTotalComunas2[dataTotalComunas2.Region == SeleccionarComuna]
    return [{'label': c, 'value': c} for c in sorted(dff.Comuna.unique())]

@app.callback(
    Output('selectComuna', 'value'),
    Input('selectComuna', 'options')
)
def set_comunas_lista1(selectComuna):
    return [k['value'] for k in selectComuna][0]

@app.callback(Output("BarraComunas", "figure"),Output("Mapa", "figure"),Output("burbujas", "figure"),Input("selectRegion", "value"))
def update_ejer4(input1):
    #print(input1)
    return get_barraComunas(dataTotalComunas, input1, "2022-08-26"), get_mapa(dataTotalComunas, input1, "2022-08-26"), get_bubble(df_casos_fallecidos_actual, input1)

@app.callback(Output("lineaComunas", "figure"), Output("lineaFallecidos", "figure"),Output("PieVacunados", "figure"),Output("PieVacunadosd2", "figure"),Output("PieVacunadosd4", "figure"),Output("PieVacunadosdRefuerzo", "figure"), Input("selectComuna", "value"))
def update_ejer5(input1):
    #print(input1)
    return get_linetotalComunas(dataTotalComunas2, input1), get_linetotalFallecidos(dataTotalFallecidos, input1), get_pie(datavacunas, input1, 'Primera'), get_pie(datavacunas, input1, 'Segunda'),get_pie(datavacunas, input1, 'Cuarta'), get_pie(datavacunas, input1, 'Refuerzo')

@app.callback(
    Output('titRegion', 'children'),
    Input("selectRegion", "value")
)
def update_titulo(value):
    return  html.H3(f'Casos Confirmados Región: {value}', style={'color': 'White','textAlign': 'center','backgroundColor':'rgb(15, 105, 180)'})

@app.callback(
    Output('titComuna', 'children'),
    Input("selectComuna", "value")
)
def update_tituloComuna(value):
    return  html.H3(f'Evolución Casos Confirmados y Fallecidos Comuna: {value}', style={'color': 'White','textAlign': 'center','backgroundColor':'rgb(15, 105, 180)'})


#@app.callback(Output("Mapa", "figure"), Input("selectRegion", "value"))
#def update_mapa(input1):
#    return get_mapa(dataTotalComunas, "Biobío", "2022-08-01"), 

if __name__ == "__main__":
    app.run_server(debug=True, host="0.0.0.0", port="5000")
