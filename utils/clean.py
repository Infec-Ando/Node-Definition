import pandas as pd

def handle(df):
  
  # eliminamos la columna country para ser remplazada por otra
  df =df.drop(columns=['country'])

  # renombramos el atributo "iso3" que trae la variable df, por "acronym_country" y "admin_name" por region 
  df= df.rename(columns={'iso2':'country','admin_name':'region'})
  #borramos los valores nulos de la poblacion y de la capital
  df=df.dropna(subset=['population'])
  df=df.dropna(subset=['capital'])

  #pasamos la poblacion a entero
  df.population=df.population.astype(int)
  df.isnull().sum()
  # vuelve asignar un index a cada país
  df=df.groupby(['city','region','country','lng','lat','population'])['capital'].count().reset_index()
  df =df.drop(columns=['capital'])

  return df
