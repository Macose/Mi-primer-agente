import streamlit as st
from src.db_utils import cargar_datos, limpiar_datos
from src.dashboard import mostrar_dashboard

st.set_page_config(page_title="Dashboard de Ventas", layout="wide")
st.title("Dashboard de Ventas")

df = cargar_datos("data/ventas.csv")
df_limpio = limpiar_datos(df)
mostrar_dashboard(df_limpio)
