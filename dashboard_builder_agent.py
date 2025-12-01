import os
import pandas as pd

class DashboardBuilderAgent:
    def __init__(self, output_dir="streamlit_dashboard_project"):
        self.output_dir = output_dir
        self._crear_estructura()

    def _crear_estructura(self):
        os.makedirs(f"{self.output_dir}/data", exist_ok=True)
        os.makedirs(f"{self.output_dir}/src", exist_ok=True)

    def generar_dataset(self):
        data = {
            "fecha": pd.date_range("2025-11-01", periods=10, freq="D"),
            "producto": ["Camiseta", "Pantalón", "Zapatillas", "Chaqueta", "Camiseta", "Zapatillas", "Pantalón", "Camiseta", "Chaqueta", "Zapatillas"],
            "cantidad": [2,1,1,3,1,2,1,4,2,1],
            "precio": [20,35,50,80,20,50,35,20,80,50],
            "cliente": ["Ana Gómez", "Luis Pérez", "Laura Ruiz", "Pedro López", "María Díaz",
                        "Carlos Ortega", "Lucía Romero", "Raúl Sánchez", "Elena Torres", "David Martín"],
            "ciudad": ["Madrid", "Barcelona", "Valencia", "Madrid", "Sevilla",
                       "Bilbao", "Zaragoza", "Madrid", "Valencia", "Barcelona"]
        }
        df = pd.DataFrame(data)
        df.to_csv(f"{self.output_dir}/data/ventas.csv", index=False)

    def generar_db_utils(self):
        contenido = '''import pandas as pd

def cargar_datos(ruta):
    return pd.read_csv(ruta, parse_dates=["fecha"])

def limpiar_datos(df):
    df = df.drop_duplicates()
    df = df.dropna()
    return df
'''
        with open(f"{self.output_dir}/src/db_utils.py", "w", encoding="utf-8") as f:
            f.write(contenido)

    def generar_dashboard(self):
        contenido = '''import streamlit as st
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
'''
        with open(f"{self.output_dir}/src/dashboard.py", "w", encoding="utf-8") as f:
            f.write(contenido)

    def generar_app(self):
        contenido = '''import streamlit as st
from src.db_utils import cargar_datos, limpiar_datos
from src.dashboard import mostrar_dashboard

st.set_page_config(page_title="Dashboard de Ventas", layout="wide")
st.title("Dashboard de Ventas")

df = cargar_datos("data/ventas.csv")
df_limpio = limpiar_datos(df)
mostrar_dashboard(df_limpio)
'''
        with open(f"{self.output_dir}/app.py", "w", encoding="utf-8") as f:
            f.write(contenido)

    def generar_requirements(self):
        contenido = "streamlit\npandas\nplotly\n"
        with open(f"{self.output_dir}/requirements.txt", "w", encoding="utf-8") as f:
            f.write(contenido)

    def generar_gitignore(self):
        contenido = "__pycache__/\n*.pyc\n.env\n"
        with open(f"{self.output_dir}/.gitignore", "w", encoding="utf-8") as f:
            f.write(contenido)

    def generar_readme(self):
        contenido = (
            "# Dashboard de Ventas con Streamlit\n\n"
            "Este proyecto fue generado automáticamente por el agente `DashboardBuilderAgent`.\n\n"
            "## Cómo ejecutarlo\n\n"
            "1. Accede a la carpeta del proyecto:\n"
            "```\n"
            f"cd {self.output_dir}\n"
            "```\n\n"
            "2. Instala dependencias:\n"
            "```\n"
            "pip install -r requirements.txt\n"
            "```\n\n"
            "3. Ejecuta la app:\n"
            "```\n"
            "streamlit run app.py\n"
            "```\n\n"
            "## Estructura del proyecto\n\n"
            "- `data/ventas.csv`: Datos simulados\n"
            "- `src/db_utils.py`: Carga y limpieza de datos\n"
            "- `src/dashboard.py`: Visualización con Streamlit y Plotly\n"
            "- `app.py`: Entrada principal del dashboard\n"
            "- `requirements.txt`: Dependencias del proyecto\n"
            "- `.gitignore`: Exclusiones para Git\n"
            "- `README.md`: Documentación del proyecto\n\n"
            "## Mejoras posibles\n\n"
            "- Filtros por fecha\n"
            "- Exportación de gráficos\n"
            "- Conexión a base de datos real\n"
            "- Despliegue en Streamlit Cloud"
        )
        with open(f"{self.output_dir}/README.md", "w", encoding="utf-8") as f:
            f.write(contenido)

    def run(self):
        self.generar_dataset()
        self.generar_db_utils()
        self.generar_dashboard()
        self.generar_app()
        self.generar_requirements()
        self.generar_gitignore()
        self.generar_readme()
        print(f"Proyecto generado en: {self.output_dir}")