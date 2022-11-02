def handle(df):
  # vuelve asignar un index a cada país
  df = df.groupby(['city','region','country','lng','lat','population'])['capital'].count().reset_index()
  return df 

