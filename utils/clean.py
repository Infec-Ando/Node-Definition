import pandas as pd
import pycountry_convert as pc
from utils.addContinent import handle as addContinent
from utils.resetIndex import handle as resetIndex 

def handle(df:pd):
  
  # eliminamos la columna country para ser remplazada por otra
  df = df.drop(columns=['country'])

  # renombramos el atributo "iso3" que trae la variable df, por "acronym_country" y "admin_name" por region 
  df = df.rename(columns={'iso2':'country','admin_name':'region'})
  #borramos los valores nulos de la poblacion y de la capital
  df = df.dropna(subset=['population'])
  df = df.dropna(subset=['capital'])

  #pasamos la poblacion a entero
  df.population=df.population.astype(int)
  df.isnull().sum()
  df = resetIndex(df)
  [df,continent] = addContinent(df)
  df = df.drop(columns=['capital'])
  df.insert(6 ,"continent",continent)


  return df


