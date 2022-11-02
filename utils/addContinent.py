import pandas as pd
import pycountry_convert as pc
from utils.resetIndex import handle as resetIndex 

def handle(df):
  continent = pd.Series(dtype=str,data=[])

  # este for loop eliminará todos las filas cuyo código de país no contenga la librería pycountry 
  for i in range(len(df)):
    try:
      continent[i] = pc.country_alpha2_to_continent_code(df['country'][i])

    except Exception:
      df = df.drop([i])
      
  df = resetIndex(df)
  return [df,continent]
