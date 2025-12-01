import pandas as pd

def cargar_datos(ruta):
    return pd.read_csv(ruta, parse_dates=["fecha"])

def limpiar_datos(df):
    df = df.drop_duplicates()
    df = df.dropna()
    return df
