import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.io as pio
import os
from dotenv import load_dotenv
from geopy.geocoders import Nominatim
import pycountry_convert as pc
from utils.clean import handle as cleanData


#haciendo 'públicas' las variables del archivo .env para el proyecto
load_dotenv()

def start():
  df = pd.read_csv('./content/worldcities.csv')

  df = cleanData(df)
  df.to_csv('./content/rebuild-worldcities.csv')

  fig = go.Figure(go.Scattermapbox(
    lon = df.lng,
    lat = df.lat,

    #para lso circulos en los mapas
    mode = 'markers+text',

    #para los ciculos, tamaño, color y demás
    marker=go.scattermapbox.Marker(
        #tamaño de las burbujas
        size=4,

        # cantidad de paises selecionados

        #para los colores https://plotly.com/python/builtin-colorscales/
        colorscale= 'Edge',

        showscale=True,

        #cambia los pixeles de las areas
        sizemode = 'diameter',
        opacity = 0.8
    ),

    hoverinfo='text',
    hovertext= '<b>Ciudad:</b>' + df['country'].astype(str) + '<br>'
    #+'<b>cantidad de paises:</b>' + df['capital'].astype(str) + '<br>'
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

for i in range(0, len(df)):
    if df['capital'][i] == 1:
        print(df['country'][i])

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