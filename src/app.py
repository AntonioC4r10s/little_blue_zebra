import streamlit as st
import pandas as pd
from model import cities, update
from databases import read_df_info, read_df_forecast
import datetime
import altair as alt


# load datas
df_info = read_df_info()
df_forecast = read_df_forecast()

# Sidebar
city = cities
st.set_page_config(layout='wide', initial_sidebar_state='expanded')
st.sidebar.header('Dashboard - vs 1.0')
st.sidebar.button('Re-run')
selected_option_city = st.sidebar.selectbox('Select a city:', options=city)

data_default = datetime.date.today()
print(data_default)

date_min = datetime.datetime.strptime(df_forecast['time'].min().split()[0], "%Y-%m-%d").date()
date_max = datetime.datetime.strptime(df_forecast['time'].max().split()[0], "%Y-%m-%d").date()
data_init = st.sidebar.date_input("Select start date:", date_min)
data_end = st.sidebar.date_input("Select the end date:", date_max)


# Data

def data_city(city):
    last_occurrence_index = df_info[df_info['name'] == city].index[-1]
    penult_occurrence_index = df_info[df_info['name'] == city].index[-2]
    data_filtred_city = df_info.loc[last_occurrence_index]
    data_filtred_city_penult = df_info.loc[penult_occurrence_index]
    df_forecast['time'] = pd.to_datetime(df_forecast['time'])
    df_forecast_filtred = df_forecast.loc[(df_forecast['time'] >= str(data_init)) & (df_forecast['time'] <= str(data_end))]
    df_forecast_filtred_city = df_forecast_filtred[df_forecast['name'] == f'{city}']

    return data_filtred_city, data_filtred_city_penult, df_forecast, df_forecast_filtred, df_forecast_filtred_city

data_filtred_city, data_filtred_city_penult, df_forecast, df_forecast_filtred, df_forecast_filtred_city = data_city(selected_option_city)

# Row A
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


# Row B
c1, c2 = st.columns((7, 3))

with c1:
    st.markdown('### Data Forecast')
    st.dataframe(df_forecast_filtred_city, height=300, width=700)

with c2:
    st.markdown('### Rain (mm) in the next days')
    rain_mm = [df_forecast_filtred_city['rain'].sum()]
    print(rain_mm)
    st.bar_chart(rain_mm, color='#5B2C6F', height=310)
    # st.text('rain')


# Row C
c1, c2 = st.columns((5, 5))

with c1:
    st.markdown('### Forecast Temperature (°C)')
    chart = st.line_chart(df_forecast_filtred_city.set_index('time')['temperature'], color='#ffaa00')

with c2:
    st.markdown('### Forecast Apparent Temperature (°C)')
    chart = st.line_chart(df_forecast_filtred_city.set_index('time')['apparent_temperature'], color='#DE3163')


# Row D
c1, c2 = st.columns((5, 5))

with c1:
    st.markdown('### Forecast Relative Humidity (%)')
    chart = st.line_chart(df_forecast_filtred_city.set_index('time')['relative_humidity'], color='#6495ED')
    

with c2:
    st.markdown('### Expected Rain (mm)')
    chart = st.line_chart(df_forecast_filtred_city.set_index('time')['rain'], color='#2ECC71')

# Row E
st.markdown('### All Data')
st.dataframe(df_forecast_filtred, width=1000)

