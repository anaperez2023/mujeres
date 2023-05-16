import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from multiapp import MultiApp
import plotly.graph_objs as go
import plotly.express as px
from plotly.subplots import make_subplots
import geopandas as gpd
import folium
import branca
import json
from streamlit.components.v1 import components
import requests


# CONFIGURACIÓN DE PÁGINA
st.set_page_config(page_title="Desigualdad de género", page_icon=":🟣:", layout="wide")

def app_home():
        # st.title("Mujeres: análisis de la desigualdad de género en España y el mundo")
        # st.write("xxxxxx")
        st.image('img/PORTADAinicio.png')
        
            
def app_internacional():
    st.title("Internacional")
    
    st.write("El dataset Women, Business and the Law Data for 1971-2023 es un proyecto de The World Bank que recopila datos únicos sobre las leyes y regulaciones que restringen las oportunidades económicas de las mujeres.")  
    st.write("Desde 2009, este proyecto ha mejorado el estudio de la igualdad de género y abierto el debate sobre cómo mejorar las oportunidades económicas y el empoderamiento de las mujeres.")
    WBL_Panel_2023 = pd.read_csv('data/WBL_Panel_2023.csv')
    st.dataframe(WBL_Panel_2023)
    st.write('A nivel mundial, las mujeres todavía acceden a solo tres cuartas partes de los derechos reconocidos a los hombres, lo que se traduce en una puntuación total de 76,5 sobre 100 puntos, que indicaría la existencia de una paridad jurídica completa. Sin embargo, a pesar del efecto desproporcionado que la pandemia mundial ha generado en la vida y los medios de subsistencia de las mujeres, 23 países reformaron sus leyes en el 2021 y dieron pasos muy necesarios para promover la inclusión económica de las mujeres, según el informe.')
    st.write('El informe Women, Business and the Law mide las leyes y regulaciones en ocho áreas que afectan la participación económica de las mujeres en 190 países. Las ocho áreas son Movilidad, Trabajo, Remuneración, Matrimonio, Parentalidad, Empresariado, Activos y Jubilación. Los datos ofrecen puntos de referencia objetivos y medibles para analizar el avance a nivel mundial hacia la igualdad de género.')
    
    col1, col2 = st.columns(2)
    with col1:
        st.image('img/INTGENERAL.png', width=350)

    with col2:
        st.image('img/INTGENERAL(2).png', width=350)
        
        
    st.subheader("Algunas cifras calculadas con los indicadores de desigualdad:")
    st.subheader("EMPRESA")
    st.image('img/INTEmpresa2.png', width=350)
    st.subheader("MOVILIDAD")
    st.image('img/INTmovilidad.png', width=350)
    st.subheader("TRABAJO")
    st.image("img/INTtrabajo.png")
    st.subheader("MATERNIDAD")
    st.image('img/INTMaternidad.png', width=350)
    
    # Mapa mundial maternidad    
    df = pd.read_csv("data/df_parenthood.csv")

    # Crear la figura del mapa mundial
    figJ = px.choropleth(df, locations="ISO Code",
                        color="Length of paid maternity leave",
                        hover_name="Economy",
                        projection="natural earth",
                        color_continuous_scale=px.colors.sequential.Plasma,
                        range_color=(0, 365))

    # Personalizar el mapa
    figJ.update_layout(title_text="Días de baja pagada por maternidad en el mundo",
                    geo=dict(showframe=False, showcoastlines=False,
                            projection_type='equirectangular'))

    # Mostrar el mapa interactivo en Streamlit
    st.plotly_chart(figJ)
    
    st.subheader('Días de baja pagada por maternidad en el mundo')
    df['Paid Maternity Leave Grouped'] = pd.cut(df['Length of paid maternity leave'], 
                                            bins=range(0, 401, 50), 
                                            labels=[f'{i}-{i+50}' for i in range(0, 400, 50)])

    # Crear el gráfico de burbujas
    figO = px.scatter(df, x='Length of paid maternity leave', y='Region', size='Length of paid maternity leave',
                 color='Paid Maternity Leave Grouped', hover_name='Economy', log_x=True)

    # Personalizar el gráfico
    figO.update_layout(title=' ',
                    title_font_size=10,
                    title_x=0.5,
                    title_y=0.95,
                    xaxis_title='Días de baja pagada por maternidad',
                    yaxis_title='Región')

    # Mostrar el gráfico interactivo
    st.plotly_chart(figO)
    
    st.subheader("VIOLENCIA CONTRA LAS MUJERES")
    st.image('img/1decada3_ok.png', width=500)
    st.image('img/cuadritos.png', width=500)

    
def app_ingresos():
    st.title("Brecha salarial en España")
    st.write("Según la Encuesta de Estructura Salarial del 2020, **el salario promedio de los hombres en España es de 27.643 euros**, mientras que **el salario de las mujeres es de 22.467 euros**, lo que representa un 81,3% en comparación con el de los hombres.")
    st.write("Es importante señalar que durante la última década se ha producido una reducción en la brecha salarial de género, disminuyendo en un 4,3% desde el 77,0% en 2011 hasta el 81,3% actual. A modo de comparación, en 2011, los hombres ganaban en promedio 25.668 euros, mientras que las mujeres ganaban 19.768 euros.")
    st.write("Estos datos muestran que la desigualdad salarial entre hombres y mujeres sigue siendo una realidad en España, aunque ha habido cierta reducción en la brecha en los últimos años. Sin embargo, aún queda mucho por hacer para lograr la igualdad salarial de género en el país.")

    with st.container():
    # Gráfico salarios 1
        salarios_hym = pd.read_csv('C:/Users/User/Desktop/BOOTCAMP-DATA-ANALYTICS-Upgrade_Hub/BOOTCAMP/DATA/WOMEN/data/salarios_hym.csv')

        trace_hombres = go.Scatter(
        x=salarios_hym["Año"],
        y=salarios_hym["Salario Hombres"],
        name="Salario Hombres",
        line=dict(color="#FF8C00")
        )

        trace_mujeres = go.Scatter(
        x=salarios_hym["Año"],
        y=salarios_hym["Salario Mujeres"],
        name="Salario Mujeres",
        line=dict(color="#8B008B")
        )

    # Crear el layout del gráfico
        layout = go.Layout(
        title="Evolución de salarios de hombres y mujeres",
        xaxis=dict(title="Año"),
        yaxis=dict(title="Salario")
        )

        # Crear la figura y mostrar el gráfico
        fig1 = go.Figure(data=[trace_hombres, trace_mujeres], layout=layout)
        st.plotly_chart(fig1)
        
        
    with st.container():
    # Gráfico salarios 2  
        
    # Crear la figura de Plotly
        fig2 = go.Figure()

    # Agregar las barras de salario de hombres
        fig2.add_trace(go.Bar(
        x=salarios_hym['Salario Hombres'],
        y=salarios_hym['Año'],
        name='Salario Hombres',
        orientation='h',
        marker_color='#FF8C00',
        width=0.4,
        offset=0.2,
        hovertemplate='<b>Año</b>: %{y} <br>' +
                  '<b>Salario Hombres</b>: %{x:.2f} €<extra></extra>'
    ))

    # Agregar las barras de salario de mujeres
        fig2.add_trace(go.Bar(
        x=salarios_hym['Salario Mujeres'],
        y=salarios_hym['Año'],
        name='Salario Mujeres',
        orientation='h',
        marker_color='#8B008B',
        width=0.4,
        offset=-0.2,
        hovertemplate='<b>Año</b>: %{y} <br>' +
                  '<b>Salario Mujeres</b>: %{x:.2f} €<extra></extra>'
    ))

    # Establecer el título y los ejes
        fig2.update_layout(
        title='Evolución de los salarios de hombres y mujeres',
        xaxis_title='Salario medio (€)',
        yaxis_title='Año',
        barmode='group',
        bargap=0.2
    )

    # Mostrar la figura en Streamlit
    st.plotly_chart(fig2)
        
    with st.container():
    # Gráfico salarios 3  

        fig3 = px.scatter(salarios_hym, x='Año', y='Diferencia en euros', size_max=10)

        # Establecer el título y los ejes
        fig3.update_layout(
        title='Aumento de la diferencia de salarios entre hombres y mujeres',
        xaxis_title='Año',
        yaxis_title='Diferencia en euros'
        )

        # Mostrar la figura
        st.plotly_chart(fig3)
        
    st.title("Pensiones")
    st.write("En diciembre de 2022, la pensión media total de las mujeres era de 887,4 euros al mes, lo que supone tan solo un 67,0% de la pensión media de los hombres que asciende a 1.323,9 euros.")
    st.write("Si desagregamos según el tipo de pensión, en las pensiones de jubilación el porcentaje que cobra una mujer es del 67,9% en relación a los hombres (982,3 frente a 1.447,2). Solo en las pensiones más bajas como son las de viudedad, orfandad y a favor de familiares las cantidades medias de la mujer son similares o incluso superiores a las de los hombres.")

# Gráfico pensiones

    df_pensiones = pd.read_csv('C:/Users/User/Desktop/BOOTCAMP-DATA-ANALYTICS-Upgrade_Hub/BOOTCAMP/DATA/WOMEN/pensiones.csv')

    fig = go.Figure()
    fig.add_trace(go.Bar(x=df_pensiones['Clase de pensión'], y=df_pensiones['Hombres'], name='Hombres', marker=dict(color='#FF8C00')))
    fig.add_trace(go.Bar(x=df_pensiones['Clase de pensión'], y=df_pensiones['Mujeres'], name='Mujeres', marker=dict(color='#8B008B')))

    fig.update_layout(title='Pensión media por clase de pensión y sexo en España (Dic.2022)',
                  xaxis_title="Clase de pensión",
                  yaxis_title="Pensión media",
                  barmode='group',
                  legend=dict(title="Sexo"))

    # Mostrar la figura
    st.plotly_chart(fig)   
        
  
def app_cuidados():
    st.title("Cuidados")
    st.write("La mayoría de los cuidados a largo plazo son proporcionados por mujeres, tanto en el ámbito formal como informal, y a menudo se realizan sin remuneración ni reconocimiento social. Esta situación ha llevado a una feminización de los cuidados y a una brecha de género en la distribución del trabajo de cuidados.")
    st.write("En los últimos años, se han puesto en marcha diversas políticas y programas para abordar estos desafíos, como la Ley de Dependencia y el Plan Nacional de Alzheimer. Además, la pandemia de COVID-19 ha exacerbado la precariedad de las condiciones de trabajo en el sector de los cuidados y ha evidenciado la necesidad de mejorar y reforzar los servicios de cuidados en España.")

    st.subheader("Responsables de los cuidados")

    # Gráfico responsables de los cuidados
    
    st.write("El dominio “Tiempo” del Índice Europeo de Igualdad proporciona valiosa información sobre cómo utilizan el tiempo disponible hombres y mujeres, esta información se obtiene de EUROFOUND.")
    st.write("Los últimos datos disponibles nos muestran lo siguiente:") 
    st.write("Existe un mayor porcentaje de mujeres que de hombres que cuidan de otras personas a diario, 39,8% frente al 27,7%. El porcentaje de mujeres que realizan tareas domésticas a diario es muy superior al de los hombres (84,5% frente a 41,9%).")
  
    with st.container():
        # Gráfico salarios 3  
        # Porcentaje de personas que se encargan de cuidados diarios en España y Europa
        women_spain = 39.8
        men_spain = 27.7
        women_europe = 37
        men_europe = 24.6

        fig7 = go.Figure(data=[
        go.Bar(name='Mujeres', x=['España', 'Europa'], y=[women_spain, women_europe], marker=dict(color='#8B008B')),
        go.Bar(name='Hombres', x=['España', 'Europa'], y=[men_spain, men_europe], marker=dict(color='#FF8C00'))
        ])

        fig7.update_layout(
        title={
        'text': '% personas que cuidan o educan a hijos, nietos, ancianos o personas con discapacidades todos los días',
        'font': {'size': 15.5}
        },
        xaxis_title='Países',
        yaxis_title='Porcentaje',
        barmode='group',
        legend=dict(title='Género')
        )

        # Mostrar la figura
        st.plotly_chart(fig7)
        
    st.subheader("Horas semanales de cuidados")
    
    st.write("Los datos de la Encuesta de Calidad de vida del año 2016, nos muestran que las horas semanales que las mujeres dedican al cuidado y tareas del hogar son superiores que las que dedican los hombres.")
    st.write("Al cuidado o la educación de los hijos, las mujeres dedican casi el doble de horas semanales, 38 horas por 23 de los hombres.")
    st.write("A cocinar o realizar tareas domésticas, mientras que las mujeres dedican 20 horas semanales, ellos dedican 11.")
    st.write("Respecto al cuidado de familiares, vecinos o amigos enfermos, las mujeres emplean más horas de media que los hombres, entre 18 y 20 para las mujeres frente a las 14 de los hombres.")

    # Gráfico horas semanales
    
    tareas = ['Hijos', 'Nietos', 'Hogar', 'Personas < 75 años', 'Personas > 75 años']
    hombres = [23, 16, 11, 14, 14]
    mujeres = [38, 16, 20, 20, 18]

    fig9 = go.Figure()
    fig9.add_trace(go.Bar(x=tareas, y=mujeres, name='Mujeres', marker_color='#8B008B'))
    fig9.add_trace(go.Bar(x=tareas, y=hombres, name='Hombres', marker_color='#FF8C00'))

    fig9.update_layout(title='Horas semanales dedicadas a tareas de cuidado', xaxis_title='Tareas', yaxis_title='Horas semanales', xaxis={'tickmode':'linear', 'ticktext': tareas})
    st.plotly_chart(fig9)
    
    st.subheader("Excedencias")
    
    st.write("En 2021, las mujeres son quienes mayoritariamente tomaron excedencias por cuidado de hijas/os, con un 87,39%, aunque existe una leve tendencia a aumentar el número de hombres que las toman.")


# Gráfico excedencias por cuidado de hijos
    exced_hijos = pd.read_csv('C:/Users/User/Desktop/BOOTCAMP-DATA-ANALYTICS-Upgrade_Hub/BOOTCAMP/DATA/WOMEN/exced_hijos.csv')
    porcentajes = (exced_hijos.loc[exced_hijos["nan"] != "Ambos sexos", "2021"] / exced_hijos.loc[exced_hijos["nan"] != "Ambos sexos", "2021"].sum()) * 100

    fig10 = make_subplots(rows=1, cols=1, specs=[[{"type": "pie"}]])
    fig10.add_trace(
    go.Pie(
        labels=exced_hijos.loc[exced_hijos["nan"] != "Ambos sexos", "nan"],
        values=porcentajes,
        textinfo="label+text+percent",
        hole=0.4,
        marker=dict(colors=['#8B008B','#FF8C00'])
        )
    )
    fig10.update_layout(
    title="Excedencia de hombres y mujeres para el cuidado de hijos/as (2021)",
    height=500, # ajustar la altura a 500 pixeles
    width=500   # ajustar el ancho a 500 pixeles
    )
    st.plotly_chart(fig10)
    
# Excedencias por cuidado de hijos: evolución por año 

# Gráfico de evolución por años

    datos_excH = {'Año': [2016, 2017, 2018, 2019, 2020, 2021],
        'Mujeres': [37531, 40536, 41302, 43091, 38467, 32645],
        'Hombres': [2986, 3363, 3947, 4297, 4759, 4709],
        'Total': [40517, 43899, 45249, 47388, 43226, 37354]}
    df_1 = pd.DataFrame(datos_excH)

    # Crear la figura interactiva
    fig11 = go.Figure()

    # Añadir la línea para los permisos por cuidado de hijos en mujeres
    fig11.add_trace(go.Scatter(x=df_1['Año'], y=df_1['Mujeres'], mode='lines', name='Mujeres', line=dict(color='#8B008B')))

    # Añadir la línea para los permisos por cuidado de hijos en hombres
    fig11.add_trace(go.Scatter(x=df_1['Año'], y=df_1['Hombres'], mode='lines', name='Hombres', line=dict(color='#FF8C00')))

    # Configurar el diseño del gráfico
    fig11.update_layout(title='Evolución de permisos por cuidado de hijos', xaxis_title='Año', yaxis_title='Número de permisos')

    # Mostrar el gráfico interactivo
    st.plotly_chart(fig11)
    

# Excedencias por cuidado de familiares
    st.subheader("Excedencias por cuidado de familiares")
    
# Gráfico excedencias por cuidado de familiares

    exced_fam = pd.read_csv('C:/Users/User/Desktop/BOOTCAMP-DATA-ANALYTICS-Upgrade_Hub/BOOTCAMP/DATA/WOMEN/exced_fam.csv')

    # Calcular los porcentajes
    porcentajes = (exced_fam.loc[exced_fam["nan"] != "Ambos sexos", "2021"] / exced_fam.loc[exced_fam["nan"] != "Ambos sexos", "2021"].sum()) * 100

    # Crear la figura
    fig11a = make_subplots(rows=1, cols=1, specs=[[{"type": "pie"}]])
    fig11a.add_trace(
    go.Pie(
        labels=exced_fam.loc[exced_fam["nan"] != "Ambos sexos", "nan"],
        values=porcentajes,
        textinfo="label+text+percent",
        hole=0.4,
        marker=dict(colors=['#8B008B','#FF8C00'])
        )
    )
    fig11a.update_layout(
    title="Excedencia de hombres y mujeres para el cuidado de familiares (2021)",
    height=500, # ajustar la altura a 700 pixeles
    width=500   # ajustar el ancho a 700 pixeles
    )
       
    # Mostrar el gráfico interactivo
    st.plotly_chart(fig11a)
    
    
# Gráfico de evolución por años en la excedencia por cuidado de familiares

    datos_excF = {'Año': [2016, 2017, 2018, 2019, 2020, 2021],
        'Mujeres': [8421, 9398, 9734, 9798, 9239, 8428],
        'Hombres': [1599, 1836, 2074, 2260, 2258, 2173],
        'Total': [10020, 11234, 11808, 12058, 11497, 10601]}
    df_2 = pd.DataFrame(datos_excF)

    # Crear la figura interactiva
    fig12 = go.Figure()

    # Añadir la línea para los permisos por cuidado de hijos en mujeres
    fig12.add_trace(go.Scatter(x=df_2['Año'], y=df_2['Mujeres'], mode='lines', name='Mujeres', line=dict(color='#8B008B')))

    # Añadir la línea para los permisos por cuidado de hijos en hombres
    fig12.add_trace(go.Scatter(x=df_2['Año'], y=df_2['Hombres'], mode='lines', name='Hombres', line=dict(color='#FF8C00')))

    # Configurar el diseño del gráfico
    fig12.update_layout(title='Evolución de permisos por cuidado de familiares (2021)', xaxis_title='Año', yaxis_title='Número de permisos')

    # Mostrar el gráfico interactivo
    st.plotly_chart(fig12)
    
    
    # Inactividad por cuidados
    
    st.subheader("Inactividad por cuidados")

    st.write("Los datos de la EPA del último trimestre de 2022 sobre la causa de la inactividad, nos muestran que mientras 64.000 mujeres dejaron su trabajo para cuidar a niños, adultos, enfermos, incapacitados o mayores, (un 92,0% del total), solo lo hicieron 5.600 hombres.")

    
# Gráfico inactividad por cuidados

    labels = ['Mujeres', 'Hombres']
    values = [92, 8]
    colors = ['#8B008B', '#FF8C00']

    trace = go.Pie(labels=labels, values=values, hoverinfo='label+percent',
               marker=dict(colors=colors))

    outside_legend = dict(orientation='v', traceorder='reversed', yanchor='middle', y=0.5,
                      xanchor='right', x=1.5,
                      font=dict(size=12),
                      bgcolor='rgba(255, 255, 255, 0.7)', bordercolor='#000000', borderwidth=2)

    layout = go.Layout(width=500, height=400,
                   title='% Personas que dejaron su trabajo por cuidados',
                   font=dict(size=12),
                   title_x=0.5)

    fig13 = go.Figure(data=[trace], layout=layout)
    fig13.update_layout(legend=outside_legend)
    
    # Mostrar el gráfico interactivo
    st.plotly_chart(fig13)  
    

# Inactividad
    st.write("En cuanto al motivo de no buscar empleo, observamos que 638.400 mujeres no están buscando empleo por cuidar a niños, adultos enfermos, incapacitados o mayores (un 92,1% del total) mientras que esa cifra es de 55.000 para los hombres.")

    st.write("Finalmente, la población inactiva según clase principal de inactividad nos aporta información sobre las personas que no trabajan por estar al cuidado del hogar, se puede observar que mientras que 2.985.300 mujeres son inactivas debido a que se dedican a las labores del hogar (un 87,7% del total), 417.700 hombres son inactivos por este motivo.")

    # GRÁFICO
    # Datos
    causas = ['Dejan empleo por cuidados', 'No buscan empleo por cuidados', 'Inactividad por labores del hogar']
    mujeres = [64000, 638400, 2985300]
    hombres = [5600, 55000, 417700]

    # Creamos los datos de las barras para cada género con colores personalizados y porcentajes
    datos_mujeres = go.Bar(
    x=causas,
    y=mujeres,
    name='Mujeres',
    marker=dict(color='#8B008B')
    )

    datos_hombres = go.Bar(
    x=causas,
    y=hombres,
    name='Hombres',
    marker=dict(color='#FF8C00')
    )

    # Creamos el layout con escala logarítmica y texto horizontal para la tercera barra
    layout = go.Layout(
    title='Causas de inactividad por género (2022)',
    xaxis=dict(title='Causas de inactividad'),
    yaxis=dict(title='Número de personas', type='log', autorange=True),
    barmode='group',
    annotations=[
        dict(
            x='Inactividad por labores del hogar',
            y=dato_hombre + 0.05,
            showarrow=False,
            xanchor='center',
            yanchor='bottom',
            font=dict(color='black')
        ) for dato_hombre in hombres
        ]
    )

    # Creamos la figura con los datos y el layout, y la mostramos
    fig14 = go.Figure(data=[datos_mujeres, datos_hombres], layout=layout)
    st.plotly_chart(fig14) 
  

def app_violencia():
    st.title("Violencia de género en España")
  
 
# Crear los botones para las subsecciones
    if st.sidebar.button('Datos'):
        mostrar_datosVG()
    if st.sidebar.button('Mapas'):
        mostrar_mapas()
    if st.sidebar.button('Modelo predictivo'):
        mostrar_modelo_predictivo()
        
def mostrar_datosVG():
    st.header('Datos oficiales')
    
    st.markdown(
        f'<div style="max-width:1024px"><iframe title="Report Section" width="600" height="373.5" src="https://app.powerbi.com/view?r=eyJrIjoiZGFlOWRkOTAtZWI2Yy00MzA0LTllYjEtNjU1MzJiMDVjODY0IiwidCI6IjhhZWJkZGI2LTM0MTgtNDNhMS1hMjU1LWI5NjQxODZlY2M2NCIsImMiOjl9" frameborder="0" allowFullScreen="true"></iframe></div>',
        unsafe_allow_html=True,
    )

def mostrar_mapas():
    st.header('Mapa de mujeres víctimas mortales por Comunidad Autónoma')
    
    # MAPA 5: Nº MUJERES VÍCTIMAS MORTALES POR CCAA   

    with open ('data/mapa5.html', 'r') as f:
        mapa_html = f.read()
        
    st.components.v1.html(mapa_html, width=700, height=500)
    
    st.header('Mapa de mujeres víctimas mortales por Provincia')
   
    # MAPA 6: Nº MUJERES VÍCTIMAS MORTALES POR PROVINCIA

    with open ('data/mapa6.html', 'r') as f:
            mapa_html6 = f.read()
            
    st.components.v1.html(mapa_html6, width=700, height=500)

def mostrar_modelo_predictivo():
    st.header('Modelo predictivo de violencia de género')

    st.write("Teniendo en cuenta los datos oficiales ofrecidos por el Ministerio de Igualdad sobre el número de víctimas mortales por violencia de género desde el año 2003 hasta el 2022, se ha implementado un modelo predictivo NeuralProphet con el objetivo de predecir el número de víctimas en los próximos dos años.")

    st.image('img/modeloVG_info_modelo.png', use_column_width=True)

    st.write('Modelo NeuralProphet')
    st.write('[00:14<00:00, 67.43it/s, SmoothL1Loss=0.0198, MAE=3.76, RMSE=4.93, Loss=0.0145, RegLoss=0, MAE_val=3.23, RMSE_val=3.89, SmoothL1Loss_val=0.0124]')

    st.image('img/modeloVG_estimacion.png', use_column_width=True)

    st.header('Conclusiones')

    st.write('En resumen, los valores de MAE y RMSE indican que el modelo está cometiendo errores de alrededor de 3.76 y 4.93 víctimas mortales en promedio, respectivamente. Además, los valores de MAE_val y RMSE_val indican que el modelo también está haciendo predicciones precisas en el conjunto de validación.')

    st.header("Estimación para los próximos dos años:")

    st.write('2023: 49 víctimas')
    st.write('2024: 48 víctimas')


def app_mas_info():
    st.image('img/mas_info.png', use_column_width=True)
    
def app_gracias():
    st.image('img/despedida.png', use_column_width=True)
    
# def app_conclusiones():
#         st.image('img/despedida.png', use_column_width=True)


# Crear el objeto MultiApp
app = MultiApp()

# Agregar las diferentes aplicaciones
app.add_app("Inicio", app_home)
app.add_app("Internacional", app_internacional)
app_esp = MultiApp()
app_esp.add_app("Ingresos", app_ingresos)
app_esp.add_app("Cuidados", app_cuidados)
app_esp.add_app("Violencia de género", app_violencia)
app.add_app("España", app_esp.run)
# app.add_app("Conclusiones", app_conclusiones)
app.add_app("Más información", app_mas_info)
app.add_app("Gracias", app_gracias)


# Ejecutar la aplicación seleccionada
app.run()


