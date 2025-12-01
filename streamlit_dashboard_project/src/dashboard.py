import streamlit as st
import plotly.express as px

def mostrar_dashboard(df):
    st.sidebar.header("Filtros")
    ciudades = st.sidebar.multiselect("Ciudad", df["ciudad"].unique(), default=df["ciudad"].unique())
    df_filtrado = df[df["ciudad"].isin(ciudades)]

    total_ventas = (df_filtrado["cantidad"] * df_filtrado["precio"]).sum()
    st.metric("Total Ventas (€)", f"{total_ventas:,.2f}")
    st.metric("Transacciones", len(df_filtrado))

    ventas_por_producto = df_filtrado.groupby("producto")["cantidad"].sum().reset_index()
    fig = px.bar(ventas_por_producto, x="producto", y="cantidad", title="Productos más vendidos")
    st.plotly_chart(fig, use_container_width=True)
