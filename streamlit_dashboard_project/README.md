# Dashboard de Ventas con Streamlit

Este proyecto fue generado automáticamente por el agente `DashboardBuilderAgent`.

## Cómo ejecutarlo

1. Accede a la carpeta del proyecto:
```
cd streamlit_dashboard_project
```

2. Instala dependencias:
```
pip install -r requirements.txt
```

3. Ejecuta la app:
```
streamlit run app.py
```

## Estructura del proyecto

- `data/ventas.csv`: Datos simulados
- `src/db_utils.py`: Carga y limpieza de datos
- `src/dashboard.py`: Visualización con Streamlit y Plotly
- `app.py`: Entrada principal del dashboard
- `requirements.txt`: Dependencias del proyecto
- `.gitignore`: Exclusiones para Git
- `README.md`: Documentación del proyecto

## Mejoras posibles

- Filtros por fecha
- Exportación de gráficos
- Conexión a base de datos real
- Despliegue en Streamlit Cloud