import streamlit as st  # Importa a biblioteca Streamlit para criar o dashboard
import streamlit.components.v1 as components  # Importa o módulo de componentes do Streamlit
import pandas as pd  # Importa a biblioteca pandas para manipulação de dataframes
import datetime  # Importa a biblioteca datetime para manipulação de datas e horas

from model import cities, update  # Importa a lista de cidades e a função update para atualizar os dados climáticos
from databases import read_df_info, read_df_forecast  # Importa funções para ler os dados climáticos do banco de dados


# Carrega os dataframes com os dados climáticos do banco de dados
df_info = read_df_info()
df_forecast = read_df_forecast()


# Sidebar
city = cities
st.set_page_config(layout='wide', initial_sidebar_state='expanded')
st.sidebar.header('Blue Zebra Board - v0.0')

# Botão para recarregar a página e atualizar os dados
if st.sidebar.button('Reset'):
    st.experimental_rerun()


# Seleção da cidade na barra lateral
selected_option_city = st.sidebar.selectbox('Select a city:', options=city)


# Data inicial e final para a seleção do período de previsão do tempo
date_min = datetime.datetime.strptime(df_forecast['time'].min().split()[0], "%Y-%m-%d").date()
date_max = datetime.datetime.strptime(df_forecast['time'].max().split()[0], "%Y-%m-%d").date()
data_init = st.sidebar.date_input("Select start date:", date_min)
data_end = st.sidebar.date_input("Select the end date:", date_max)


# Função para filtrar os dados da cidade selecionada
def data_city(city):
    # Última e penúltima ocorrência da cidade nos dados climáticos atuais
    last_occurrence_index = df_info[df_info['name'] == city].index[-1]
    penult_occurrence_index = df_info[df_info['name'] == city].index[-2]
    data_filtred_city = df_info.loc[last_occurrence_index]
    data_filtred_city_penult = df_info.loc[penult_occurrence_index]
    
    # Filtra os dados de previsão do tempo para a cidade e para o período selecionado
    df_forecast['time'] = pd.to_datetime(df_forecast['time'])
    df_forecast_filtred = df_forecast.loc[(df_forecast['time'] >= str(data_init)) & (df_forecast['time'] <= str(data_end))]
    df_forecast_filtred_city = df_forecast_filtred[df_forecast['name'] == f'{city}']

    return data_filtred_city, data_filtred_city_penult, df_forecast, df_forecast_filtred, df_forecast_filtred_city


# Obtém os dados filtrados para a cidade selecionada
data_filtred_city, data_filtred_city_penult, df_forecast, df_forecast_filtred, df_forecast_filtred_city = data_city(selected_option_city)


# Row A: Exibe métricas para a cidade selecionada
st.markdown('# Metrics for' + f" {selected_option_city} - {data_filtred_city['country']}")
st.markdown('###### Updated in ' + f"{data_filtred_city['time']}, " \
             f"lat: {data_filtred_city['lat']} & lon: {data_filtred_city['lon']}")            
col1, col2, col3 = st.columns(3)
col1.metric("Temperature", f"{data_filtred_city['temperature']} °C", 
            f"{round(data_filtred_city['temperature'] - data_filtred_city_penult['temperature'], 2)} °C")
col2.metric("Wind", f"{data_filtred_city['wind']} mph", 
            f"{round(((data_filtred_city['wind'] - data_filtred_city_penult['wind']) / data_filtred_city_penult['wind'])*100, 2)}%")
col3.metric("Humidity", f"{data_filtred_city['humidity']}%",
             f"{round(data_filtred_city['humidity'] - data_filtred_city_penult['humidity'], 2)}%")


# Row B: Exibe os dados de previsão do tempo e a quantidade de chuva
c1, c2 = st.columns((7, 3))
with c1:
    st.markdown('### Data Forecast')
    st.dataframe(df_forecast_filtred_city, height=300, width=700)

with c2:
    st.markdown('### Rain (mm) in the next days')
    rain_mm = [df_forecast_filtred_city['rain'].sum()]
    print(rain_mm)
    st.bar_chart(rain_mm, color='#5B2C6F', height=310)


# Row C: Exibe o tráfego ao vivo na cidade selecionada usando um iframe do Waze
st.markdown(f'### Traffic live in {selected_option_city}')
st.markdown('###### Use Ctrl+scroll to zoom')
iframe_html = f"""
            <iframe 
            src="https://embed.waze.com/fr/iframe?zoom=12&lat={data_filtred_city['lat']}&lon={data_filtred_city['lon']}
            &pin=1&locale=pt_BR"
            width="1000" 
            height="300">
            </iframe> 
            """
components.html(iframe_html, height=400)


# Row D: Exibe gráficos de previsão de temperatura e temperatura aparente
c1, c2 = st.columns((5, 5))
with c1:
    st.markdown('### Forecast Temperature (°C)')
    chart = st.line_chart(df_forecast_filtred_city.set_index('time')['temperature'], color='#ffaa00')
with c2:
    st.markdown('### Forecast Apparent Temperature (°C)')
    chart = st.line_chart(df_forecast_filtred_city.set_index('time')['apparent_temperature'], color='#CB4335')


# Row E: Umidade Relativa e Expectativa de chuvas
c1, c2 = st.columns((5, 5))

with c1:
    st.markdown('### Forecast Relative Humidity (%)')
    chart = st.line_chart(df_forecast_filtred_city.set_index('time')['relative_humidity'], color='#6495ED')
    

with c2:
    st.markdown('### Expected Rain (mm)')
    chart = st.line_chart(df_forecast_filtred_city.set_index('time')['rain'], color='#2ECC71')


# Row F: Exibe um dataframe com todos os dados armazenados para verificação ou consulta 
st.markdown('### All Data')
st.dataframe(df_forecast_filtred, width=1100)