import streamlit as st
import pandas as pd
import datetime
import altair as alt
from model import cities, update
from databases import read_df_info, read_df_forecast

# Load datas
df_info = read_df_info()
df_forecast = read_df_forecast()

# Convert 'time' column to datetime
df_forecast['time'] = pd.to_datetime(df_forecast['time'])

# Sidebar
city = cities
st.set_page_config(layout='wide', initial_sidebar_state='expanded')
st.sidebar.header('Dashboard - version 1')

# Função para criar o gráfico de linha
def create_line_chart(df_forecast_filtred):
    chart = alt.Chart(df_forecast_filtred).mark_line(color='#ffaa00').encode(
        x='time:T',
        y='temperature:Q'
    ).properties(
        width=600,
        height=400
    )
    return chart

# Função para filtrar os dados do dataframe df_forecast
def filter_forecast_data(df_forecast, city, start_date, end_date):
    last_occurrence_index = df_info[df_info['name'] == city].index[-1]
    data_filtred_city = df_info.loc[last_occurrence_index]
    df_forecast_filtred = df_forecast.loc[(df_forecast['time'] >= start_date) & (df_forecast['time'] <= end_date)]
    return df_forecast_filtred, data_filtred_city

# Widgets na barra lateral
selected_option_city = st.sidebar.selectbox('Select a city:', options=city)
if st.sidebar.button('Update Data'):
    update()
    st.experimental_rerun()

data_min = df_forecast['time'].min().date()
data_max = df_forecast['time'].max().date()
data_init = st.sidebar.date_input("Selecione a data inicial:", data_min)
data_end = st.sidebar.date_input("Selecione a data final:", data_max)

# Filtrar os dados do dataframe df_forecast
df_forecast_filtred, data_filtred_city = filter_forecast_data(df_forecast, selected_option_city, data_init, data_end)

# Row A
st.markdown('### Metrics:' + f" {selected_option_city} - {data_filtred_city['country']}")
st.markdown('###### Updated in ' + f"{data_filtred_city['time']}")            
col1, col2, col3 = st.columns(3)
col1.metric("Temperature", f"{data_filtred_city['temperature']} °C")
col2.metric("Wind", f"{data_filtred_city['wind']} mph")
col3.metric("Humidity", f"{data_filtred_city['humidity']}%")

# Row B
c1, c2 = st.columns((7, 3))

with c1:
    st.markdown('### Forecast Temperature °C')
    chart = create_line_chart(df_forecast_filtred)
    st.altair_chart(chart, use_container_width=True)

with c2:
    st.markdown('### Histogram Relative Humidity')
    hist = alt.Chart(df_forecast_filtred).mark_bar().encode(
        alt.X('temperature', bin=alt.Bin(maxbins=20)),
        alt.Y('count()', title='Frequency')
    ).properties(
        title='Histogram of Temperature'
    )
    st.altair_chart(hist, use_container_width=True)
