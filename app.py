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
import pandas as pd
import plotly.express as px

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
        "No", "No", "No", "SI", "Si", "No", "No", "No", "No", "Si",
        "No", "Si", "No", "Si", "No", "No", "Si", "No", "Si", "No",
        "Si", "No", "No", "No", "No", "No", "No", "Si", "No", "No",
        "No", "No", "Si", "Si", "No", "No", "No", "No", "Si", "Si",
        "No", "No", "No", "No", "No", "No"
    ],
    "Detalle": [
        "I-209:Incidencia conexión de unidades programadas al momento del reporte / Estado Zoho : Hecho / Estado Real: Hecho",
        "I-105:Actualización de causas de no cumplimiento listado / Estado Zoho : Hecho / Estado Real: Hecho",
        "I-210:Demoras en reportes deavances, conexión visual con elreporte. / Estado Zoho : Hecho / Estado Real: Hecho",
        "I-211:No se permite programarcomplementarias en semanal / Estado Zoho : Hecho / Estado Real: Hecho",
        "I-212:Diferenciación de actividadesprogramadas actuales y de la semana anterior / Estado Zoho : Hecho / Estado Real: Hecho",
        "I-82:Tener doble porcentaje para alistamiento / Estado Zoho : Hecho / Estado Real: Hecho",
        "X1-I87 -(I-13):Visor estado de trámite / Estado Zoho : Hecho / Estado Real: En pausa",
        "I-33:Incidencia decimales programación de avances / Estado Zoho : Hecho / Estado Real: Hecho",
        "I-98:Conexión con grilla con sellos de calidad / Estado Zoho : Hecho / Estado Real: Hecho",
        "I-30:Incluir actividades complementarias en grilla / Estado Zoho : Hecho / Estado Real: Hecho",
        "X1-I13- (I-9):Notificaciones por correo electronico, restricciones y compromisos / Estado Zoho : Hecho / Estado Real: No hecho",
        "X1-I29 - (I-10):Agregar correo de contratistas / Estado Zoho : Hecho / Estado Real: No hecho",
        "I-11:Notificación de correo a contratistas / Estado Zoho : Hecho / Estado Real: No hecho",
        "I-94:Alerta de bajo rendimiento de programación / Estado Zoho : Hecho / Estado Real: Hecho",
        "I-80:Validaciones de tope de cantidades en semanal / Estado Zoho : Hecho / Estado Real: Hecho",
        "I-91:Vincular CNC con tableros de rendimientos / Estado Zoho : Hecho / Estado Real: No hecho",
        "C9-I114 - (C9-I23):Visual de kits / Estado Zoho : Hecho / Estado Real: No hecho",
        "I-77:PAC Preliminar / Estado Zoho : Hecho / Estado Real: No hecho",
        "I-106:Vincular contratistas a las actividades / Estado Zoho :  / Estado Real: ",
        "I-28:Visual actividades sin restricción, consultar restricciones de una actividad restricción- huerfanas / Estado Zoho : Hecho / Estado Real: Hecho",
        "I-40:Tablero de preconstrucción / Estado Zoho : No hecho / Estado Real: No hecho",
        "I-61:Botón para descargar avance last planner, desde retrocesso ( Todas actividades) / Estado Zoho : Hecho / Estado Real: Hecho",
        "I-108:Permisos de cambio de fechade legalización cuando este vencidasolo para preconstrucción / Estado Zoho : Hecho / Estado Real: No hecho",
        "I-217:Actividades complementariaperdidas / Estado Zoho : Hecho / Estado Real: Hecho",
        "I-104:Avance preliminar en grilla / Estado Zoho : Hecho / Estado Real: No hecho",
        "X1-I31 - (C9-I12):Copia información del acta / Estado Zoho : No hecho / Estado Real: No hecho",
        "I-26:Secuencia constructiva en grilla / Estado Zoho : No hecho / Estado Real: Hecho",
        "X1-I28 - (C9-I57):Migración responsabiliades por rotación de personal / Estado Zoho : Hecho / Estado Real: No hecho",
        "I-66:Ajuste bandera nuevo paraactivar proyectos pruebas / Estado Zoho : Hecho / Estado Real: Hecho",
        "C9-I151:Programación y reporte de unidades grilla (fuera de reunión) / Estado Zoho : No hecho / Estado Real: No hecho",
        "C9-152:Visibilidad de actividades afectadas por cierre anticipado de capitulos  / Estado Zoho : No hecho / Estado Real: Hecho",
        "C9-I67 - (C9-144):Restricciones automaticas de contratos / Estado Zoho : Hecho / Estado Real: No hecho",
        "C9-I147 y por sotec (aplica para Sky Tower):Unidades no aplica grilla / Estado Zoho : No hecho / Estado Real: No hecho",
        "X1-I90 - (C9-I16):Conexión restricciones de diseño, con cronogramas y concurrentes / Estado Zoho : No hecho / Estado Real: No hecho",
        "X1-I66- (C9-I40):Informe de preconstrucción ( registro y visualización) / Estado Zoho : No hecho / Estado Real: No hecho",
        "C9-I139:Modificar estado de actividad sobre unidades especificas en caso de reprocesos / Estado Zoho : No hecho / Estado Real: No hecho",
        "C9-I69:Modulo de interventoria / Estado Zoho : No hecho / Estado Real: No hecho",
        "C9-I129:Botón paradescargaravances en lastplanner / Estado Zoho : Hecho / Estado Real: Hecho",
        "X1-I87 - (C9-I111):Estado de tramite en avance de grilla / Estado Zoho : Hecho / Estado Real: No hecho",
        "X1-I86 - (C9-I7):Secuencia de actividades y peso de actividades para grilla / Estado Zoho : Hecho / Estado Real: No hecho",
        "X1-I80 - (C9-I48):Agregar restricciones parciales hijas / Estado Zoho : No hecho / Estado Real: No hecho",
        "X1-I81 - (C9-I49):Restricciones parciales (madres/hijas) en visual unidades restringir en grilla / Estado Zoho : No hecho / Estado Real: No hecho",
        "C9-I102:Ajuste de estado de actividad en grilla / Estado Zoho : Hecho / Estado Real: Hecho",
        "0:Reporte de avances mejora en rapidez / Estado Zoho : - / Estado Real: Hecho",
        "0:Incidente fechas licitación mal calculadas (marzo25), debe dejar solo 1 vencimiento y diagrama de árbol para mostrar las fechas / Estado Zoho : - / Estado Real: No hecho",
        "Sotec:Conexión con QNTRL: fecha de incio de fab y leg. Simbolos / Estado Zoho : - / Estado Real: -",
        "C9 - I154:Precortes de obra / Estado Zoho : No hecho / Estado Real: No hecho",
        "C9-I12:Copia info. actas, exportación de historico en excel y cierre de acta sea hasta las 23:59 con fecha del día / Estado Zoho : - / Estado Real: No hecho",
        "C9- I129:Botón para descargar avances en last planner / Estado Zoho : - / Estado Real: Hecho",
        "C9-I102:Ajuste de estado de actividad en grilla / Estado Zoho : - / Estado Real: Hecho",
        "I-104:Avance preliminar en grilla / Estado Zoho : - / Estado Real: No hecho",
        "0:Disminucion de avances / Estado Zoho : - / Estado Real: No hecho",
        "0:Duplicidad de avances dos clicks en guardar todo en reportar avance / Estado Zoho : - / Estado Real: No hecho",
        "0:Agregar CNC en reporte preliminar / Estado Zoho : - / Estado Real: No hecho",
        "0:Cuando se incumple una restricción, observacion y no cumplimiento debe serobligatorio / Estado Zoho : - / Estado Real: No hecho",
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
# 5. Gráfico
# --------------------------------------------------
fig = px.scatter(
    df_count,
    x='Periodo',
    y='Categoria',
    size='Conteo',
    size_max=35,
    text='Conteo',
    template='plotly_white',
    title="<b>Matriz de Cumplimiento: rendimiento discreto por periodo de registro de historias de usuario (HU)</b>"
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
    title_standoff=40    # ← CLAVE: separa el título del eje
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
        y=-0.40,          # ← bajamos los KPI
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

fig.show()

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
