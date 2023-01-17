import pandas as pd
from datetime import datetime

gapminder = pd.read_csv("https://raw.githubusercontent.com/holtzy/The-Python-Graph-Gallery/master/static/data/gapminderData.csv")
migrantes = pd.read_excel("https://github.com/curso-visualizacion/practicas_diploma/blob/master/Practica3/MigrantesChile%20(2005-2016)-Copy1.xlsx?raw=true")

#date = datetime.today().strftime('%Y-%m-%d')
date = '2022-08-26'
dataTotalRegion = pd.read_csv("https://raw.githubusercontent.com/MinCiencia/Datos-COVID19/master/output/producto4/"+date+"-CasosConfirmados-totalRegional.csv")
dataTotalRegion = dataTotalRegion.iloc[:-2]

dataTotal = pd.read_csv("https://raw.githubusercontent.com/MinCiencia/Datos-COVID19/master/output/producto5/TotalesNacionales_T.csv")

## data comunas
dataTotalComunas = pd.read_csv("https://raw.githubusercontent.com/MinCiencia/Datos-COVID19/master/output/producto1/Covid-19.csv")

## data comunas2
dataTotalComunas2 = pd.read_csv("https://raw.githubusercontent.com/MinCiencia/Datos-COVID19/master/output/producto1/Covid-19.csv")
dataTotalComunas2 = dataTotalComunas2.drop("Tasa", axis=1)
dataTotalComunas2 = dataTotalComunas2.melt(['Region','Codigo region','Comuna','Codigo comuna', 'Poblacion'], var_name='Fecha')
dataTotalComunas2=dataTotalComunas2.rename(columns = {'value': 'Casos'}, inplace = False)
dataTotalComunas2= dataTotalComunas2.loc[(dataTotalComunas2["Codigo comuna"].notnull())]

## Data Fallecidos Comunas
dataTotalFallecidos = pd.read_csv("https://raw.githubusercontent.com/MinCiencia/Datos-COVID19/master/output/producto38/CasosFallecidosPorComuna.csv")
dataTotalFallecidos = dataTotalFallecidos.melt(['Region','Codigo region','Comuna','Codigo comuna', 'Poblacion'], var_name='Fecha')
dataTotalFallecidos=dataTotalFallecidos.rename(columns = {'value': 'Fallecidos'}, inplace = False)
dataTotalFallecidos= dataTotalFallecidos.loc[(dataTotalFallecidos["Codigo comuna"].notnull())]

##DataSintomas
datasintomas = pd.read_csv("https://raw.githubusercontent.com/MinCiencia/Datos-COVID19/master/output/producto21/SintomasCasosConfirmados.csv")
datasintomas = datasintomas[["Sintomas", "2020-07-13"]]

##DataCAsos vd FAllecidos
df_casos_actual = dataTotalComunas2.loc[(dataTotalComunas2['Fecha'] == date)]
df_fallecidos_actual = dataTotalFallecidos.loc[(dataTotalFallecidos['Fecha'] == date)]
df_casos_fallecidos_actual = pd.merge(df_casos_actual, df_fallecidos_actual, how="inner", on=["Codigo comuna", "Fecha"])
df_casos_fallecidos_actual = df_casos_fallecidos_actual[["Codigo region_x","Region_x", "Codigo comuna", "Comuna_x","Fecha", "Casos", "Fallecidos"]]
df_casos_fallecidos_actual.rename(columns = {'Codigo region_x':'Codigo Region', 'Region_x':'Region', 'Comuna_x': 'Comuna'}, inplace = True)
#print(df_casos_fallecidos_actual)

## Vacunas
datavacunas1 = pd.read_csv("https://raw.githubusercontent.com/MinCiencia/Datos-COVID19/master/output/producto80/vacunacion_comuna_1eraDosis.csv")
datavacunas1= datavacunas1.loc[(datavacunas1["Codigo comuna"].notnull())]
datavacunas1['Total'] = datavacunas1.iloc[:, 5:-1].sum(numeric_only=True,axis=1)
datavacunas1 = datavacunas1.assign(Dosis='Primera')
datavacunas1 = datavacunas1[['Dosis',"Region", "Codigo region", 'Comuna', 'Codigo comuna', 'Poblacion', 'Total']]
datavacunas1['NoVacunados'] = (datavacunas1['Poblacion']-datavacunas1['Total'])

datavacunasd2 = pd.read_csv("https://raw.githubusercontent.com/MinCiencia/Datos-COVID19/master/output/producto80/vacunacion_comuna_2daDosis.csv")
datavacunasd2= datavacunasd2.loc[(datavacunasd2["Codigo comuna"].notnull())]
datavacunasd2['Total'] = datavacunasd2.iloc[:, 5:-1].sum(numeric_only=True,axis=1)
datavacunasd2 = datavacunasd2.assign(Dosis='Segunda')
datavacunasd2 = datavacunasd2[['Dosis',"Region", "Codigo region", 'Comuna', 'Codigo comuna', 'Poblacion', 'Total']]
datavacunasd2['NoVacunados'] = (datavacunasd2['Poblacion']-datavacunasd2['Total'])

datavacunasd4 = pd.read_csv("https://raw.githubusercontent.com/MinCiencia/Datos-COVID19/master/output/producto80/vacunacion_comuna_4taDosis.csv")
datavacunasd4= datavacunasd4.loc[(datavacunasd4["Codigo comuna"].notnull())]
datavacunasd4['Total'] = datavacunasd4.iloc[:, 5:-1].sum(numeric_only=True,axis=1)
datavacunasd4 = datavacunasd4.assign(Dosis='Cuarta')
datavacunasd4 = datavacunasd4[['Dosis',"Region", "Codigo region", 'Comuna', 'Codigo comuna', 'Poblacion', 'Total']]
datavacunasd4['NoVacunados'] = (datavacunasd4['Poblacion']-datavacunasd4['Total'])

datavacunasdref = pd.read_csv("https://raw.githubusercontent.com/MinCiencia/Datos-COVID19/master/output/producto80/vacunacion_comuna_4taDosis.csv")
datavacunasdref= datavacunasdref.loc[(datavacunasdref["Codigo comuna"].notnull())]
datavacunasdref['Total'] = datavacunasdref.iloc[:, 5:-1].sum(numeric_only=True,axis=1)
datavacunasdref = datavacunasdref.assign(Dosis='Refuerzo')
datavacunasdref = datavacunasdref[['Dosis',"Region", "Codigo region", 'Comuna', 'Codigo comuna', 'Poblacion', 'Total']]
datavacunasdref['NoVacunados'] = (datavacunasdref['Poblacion']-datavacunasdref['Total'])

datavacunasdu = pd.read_csv("https://raw.githubusercontent.com/MinCiencia/Datos-COVID19/master/output/producto80/vacunacion_comuna_UnicaDosis.csv")
datavacunasdu= datavacunasdu.loc[(datavacunasdu["Codigo comuna"].notnull())]
datavacunasdu['Total'] = datavacunasdu.iloc[:, 5:-1].sum(numeric_only=True,axis=1)
datavacunasdu = datavacunasdu.assign(Dosis='Unica')
datavacunasdu = datavacunasdu[['Dosis',"Region", "Codigo region", 'Comuna', 'Codigo comuna', 'Poblacion', 'Total']]
datavacunasdu['NoVacunados'] = (datavacunasdu['Poblacion']-datavacunasdu['Total'])
datavacunas = pd.concat([datavacunas1, datavacunasd2, datavacunasd4,datavacunasdref,datavacunasdu])
datavacunas['NoVacunados'] = datavacunas.loc[:, 'NoVacunados'].clip(lower=0)