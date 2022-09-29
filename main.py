import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.io as pio
import os
from geopy.geocoders import Nominatim
import pycountry_convert as pc


def start():
  df = pd.read_csv('./content/worldcities.csv')
  # renombramos el atributo "iso3" que trae la variable df, por "acronym_country"
  df= df.rename(columns={'iso3':'acronym_country'})
  #borramos los valores nulos de la poblacion y de la capital
  df=df.dropna(subset=['population'])
  df=df.dropna(subset=['capital'])

  #pasamos la poblacion a entero
  df.population=df.population.astype(int)
  df.isnull().sum()
  # vuelve asignar un index a cada país
  df=df.groupby(['acronym_country','lng','lat'])['capital'].count().reset_index()
  

  fig = go.Figure(go.Scattermapbox(
    lon = df.lng,
    lat = df.lat,

    #para lso circulos en los mapas
    mode = 'markers+text',

    #para los ciculos, tamaño, color y demás
    marker=go.scattermapbox.Marker(
        #tamaño de las burbujas
        size=df.capital, 

        # cantidad de paises selecionados 
        color=df.capital, 

        #para los colores https://plotly.com/python/builtin-colorscales/
        colorscale= 'Edge', 

        showscale=True,

        #cambia los pixeles de las areas 
        sizemode = 'diameter', 
        opacity = 0.8 
    ),

    hoverinfo='text',
    hovertext= '<b>Ciudad:</b>' + df['acronym_country'].astype(str) + '<br>'+
    '<b>cantidad de paises:</b>' + df['capital'].astype(str) + '<br>'
    ))

  fig.update_layout(
      hovermode='x',
      margin= dict(r=0, l=0, t=0),
      mapbox=dict(
          accesstoken=os.getenv('TOKEN'),
          style='stamen-terrain',
      ),
      showlegend = True,
      autosize = True
  )
  fig.show()
start()

continent_name = pc.country_alpha2_to_continent_code('PE')
print(continent_name)


# initialize Nominatim API
#geolocator = Nominatim(user_agent="geoapiExercises")
#
#
#Latitude = "35.6839"
#Longitude = "139.7744"
# 
#location = geolocator.reverse(Latitude+","+Longitude)
#
#
#
#
#address = location.raw['address'] 
## Display
#print(address)