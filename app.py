import streamlit as st
import pandas as pd
import plotly.express as px
import time

# --------------------------------------------------
# 0. Configuración de página
# --------------------------------------------------
st.set_page_config(
    page_title="HEI - Matriz de Cumplimiento",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --------------------------------------------------
# 1. Datos
# --------------------------------------------------
data = {
    "Año": [
        2024, 2024, 2024, 2024, 2024, 2024, 2024, 2024, 2024, 2024,
        2023, 2023, 2024, 2024, 2024, 2024, 2024, 2024, 2025, 2024,
        2024, 2024, 2024, 2024, 2024, 2024, 2024, 2024, 2024, 2025,
        2025, 2024, 2025, 2024, 2024, 2025, 2024, 2025, 2024, 2024,
        2024, 2024, 2024, 2025, 2025, 2025, 2025, 2025, 2025, 2025,
        2025, 2025, 2025, 2025, 2025, 2025, 2025
    ],
    "Mes": [
        12, 11, 12, 12, 12, 8, 5, 5, 10, 4,
        11, 1, 6, 9, 12, 9, 6, 8, 10, 4,
        5, 2, 11, 12, 11, 2, 4, 1, 7, 7,
        7, 7, 5, 5, 5, 2, 7, 2, 5, 5,
        5, 5, 11, 10, 10, 9, 10, 10, 10, 10,
        10, 10, 10, 10, 10, 10
    ],
    "Categoria": [
        "Si", "Si", "Si", "Si", "Si", "Si", "No", "Si", "Si", "Si",
        "No", "No", "No", "Si", "Si", "No", "No", "No", "No", "Si",
        "No", "Si", "No", "Si", "No", "No", "Si", "No", "Si", "No",
        "Si", "No", "No", "No", "No", "No", "No", "Si", "No", "No",
        "No", "No", "Si", "Si", "No", "No", "No", "No", "Si", "Si",
        "No", "No", "No", "No", "No", "No"
    ],
    "Detalle": [
        "I-209:Incidencia conexión de unidades programadas al momento del reporte / Estado Zoho : Hecho / Estado Real: Hecho",
        "I-105:Actualización de causas de no cumplimiento listado / Estado Zoho : Hecho / Estado Real: Hecho",
        "I-210:Demoras en reportes deavances, conexión visual con elreporte. / Estado Zoho : Hecho / Estado Real: Hecho",
        # ...continúa toda la lista de detalles...
        "0:CNC cuando se hace reducción / Estado Zoho : - / Estado Real: No hecho"
    ]
}

# --------------------------------------------------
# 2. Blindaje de longitudes
# --------------------------------------------------
min_len = min(len(v) for v in data.values())
data = {k: v[:min_len] for k, v in data.items()}
df = pd.DataFrame(data)

# --------------------------------------------------
# 3. Preparación
# --------------------------------------------------
df['Categoria'] = df['Categoria'].str.strip().str.capitalize()
df['Mes'] = df['Mes'].astype(int)

meses = {
    1:'Enero',2:'Febrero',3:'Marzo',4:'Abril',
    5:'Mayo',6:'Junio',7:'Julio',8:'Agosto',
    9:'Septiembre',10:'Octubre',11:'Noviembre',12:'Diciembre'
}

df['Mes_Nombre'] = df['Mes'].map(meses)
df['Periodo'] = df['Año'].astype(str) + '-' + df['Mes_Nombre']
df['Periodo_Orden'] = df['Año'] * 100 + df['Mes']

# --------------------------------------------------
# 4. Agregaciones
# --------------------------------------------------
df_count = (
    df.groupby(['Periodo','Categoria'], observed=True)
      .agg(
          Conteo=('Detalle','count'),
          Tooltip=('Detalle', lambda x: "<br>".join(f"• {d}" for d in x))
      )
      .reset_index()
      .merge(df[['Periodo','Periodo_Orden']].drop_duplicates(), on='Periodo')
      .sort_values('Periodo_Orden')
)

df_kpi = (
    df.groupby(['Periodo','Categoria'])
      .size()
      .unstack(fill_value=0)
      .reset_index()
      .merge(df[['Periodo','Periodo_Orden']].drop_duplicates(), on='Periodo')
      .sort_values('Periodo_Orden')
)

df_kpi['Cumplimiento'] = df_kpi.get('Si',0) / (df_kpi.get('Si',0) + df_kpi.get('No',0))
orden_periodos = df_kpi['Periodo'].tolist()

# --------------------------------------------------
# 5. Streamlit - Título
# --------------------------------------------------
st.title("Matriz de Cumplimiento: rendimiento discreto por periodo de HU")

# --------------------------------------------------
# 6. Gráfico
# --------------------------------------------------
fig = px.scatter(
    df_count,
    x='Periodo',
    y='Categoria',
    size='Conteo',
    size_max=35,
    text='Conteo',
    template='plotly_white'
)

fig.update_traces(
    customdata=df_count['Tooltip'],
    hovertemplate="<b>%{x}</b><br>Estado: %{y}<br>Conteo: %{marker.size}<br><br>%{customdata}<extra></extra>",
    textposition='top center'
)

fig.update_xaxes(
    categoryorder='array',
    categoryarray=orden_periodos,
    tickangle=-45,
    title_text='Periodo',
    title_standoff=40
)

fig.update_yaxes(
    categoryorder='array',
    categoryarray=['Si','No'],
    range=[-0.6, 1.6],
    title_text='Estado'
)

# KPI por periodo
for _, r in df_kpi.iterrows():
    fig.add_annotation(
        x=r['Periodo'],
        y=-0.40,
        yref='paper',
        text=f"{r['Cumplimiento']:.0%}",
        showarrow=False,
        font=dict(size=11)
    )

# KPI promedio
fig.add_annotation(
    x=0.5,
    y=1.14,
    xref='paper',
    yref='paper',
    text=f"<b>Cumplimiento promedio:</b> {df_kpi['Cumplimiento'].mean():.1%}",
    showarrow=False,
    font=dict(size=14)
)

fig.update_layout(
    height=760,
    margin=dict(l=60, r=60, t=140, b=260),
    showlegend=False
)

# --------------------------------------------------
# 7. Renderizar en Streamlit
# --------------------------------------------------
st.plotly_chart(fig, use_container_width=True)
