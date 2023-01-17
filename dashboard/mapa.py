import plotly.express as px
import requests

def get_mapa(data, region, fecha):
    dataTotalComunas= data.loc[data["Region"] == region, ["Codigo region","Comuna", "Codigo comuna", fecha]]
    dataTotalComunas = dataTotalComunas.rename({fecha: 'Confirmados', 'Codigo region':'Region'}, axis=1)
    region_jason = dataTotalComunas.Region.unique()
    repo_url = 'https://raw.githubusercontent.com/caracena/chile-geojson/master/'+str(region_jason[0])+'.geojson' #Archivo GeoJSON
    #print(repo_url)
    chile_regions_geo = requests.get(repo_url).json()
    
    fig = px.choropleth(data_frame=dataTotalComunas, 
                    geojson=chile_regions_geo, 
                    locations='Codigo comuna', # nombre de la columna del Dataframe
                    featureidkey='properties.cod_comuna',  # ruta al campo del archivo GeoJSON con el que se hará la relación (nombre de los estados)
                    color='Confirmados', #El color depende de las cantidades
                    #color_continuous_scale="burg", #greens
                    #color_continuous_scale=px.colors.sequential.Rainbow,
                    color_continuous_scale=px.colors.sequential.Rainbow,
                    hover_name='Comuna',
                    labels={'CasosTotales':'Casos Totales', 'Codigo comuna':'Cód. Comuna'},
                    #projection="mercator",
                    #scope="south america"
                   )
    fig.update_geos(showcountries=True, showcoastlines=True, showland=True, fitbounds="locations")
    
    fig.update_layout(
        title_text = 'Casos Totales por Regiones',
        paper_bgcolor='rgb(248, 248, 255)',
        plot_bgcolor='rgb(248, 248, 255)',
        margin=dict(l=10, r=10, t=50, b=20),
        #showlegend=False,
        #font_color="blue",
        #title_font_color="blue",
        title={
            'text': "Mapa Calor Casos Confirmados",
            'y':0.95,
            'x':0.5,
            'xanchor': 'center',
            'yanchor': 'top'}
    )
    
    return fig