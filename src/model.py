from weather_api import API_WEATHER_KEY, cities, data_weather_now, coord, data_example, main_data_weather
import pandas as pd
import warnings
from databases import df_info_to_sql, df_forecast_to_sql


warnings.simplefilter(action='ignore', category=FutureWarning)


def update():
    data = main_data_weather(cities=cities)
    data = extract(data=data)
    df_info_to_sql(df_info=data[0][0])
    df_forecast_to_sql(df_forecast=data[0][1])
    # print(data[0][0])
    print('updated!')


def extract(data: list):

	data_tuples = []	
	index_data_actual = 1
	df_info = pd.DataFrame(columns=['name', 'country', 'lat', 'lon'])
	df_forecast = pd.DataFrame(columns=['name', 'time', 'temperature', 'relative_humidity', 
									 	'apparent_temperature', 'rain'])
	for data_city in data:
		data_actual = data_city[0]
		data_forecast = data_city[1]
		data_past = data_city[2]
		df_info = pd.concat([df_info, pd.DataFrame({'name': data_actual['name'], 
											 	'country': data_actual['sys']['country'], 
												'lat': data_actual['coord']['lat'], 
												'lon': data_actual['coord']['lon']}, 
												index=[index_data_actual]).dropna(axis=1, how='all')])
		index_data_actual += 1
		df_forecast = pd.concat([df_forecast, pd.DataFrame({'name': data_actual['name'],
													  		'time': data_forecast['hourly']['time'],
													  		'temperature': data_forecast['hourly']['temperature_2m'],
										   					'relative_humidity': data_forecast['hourly']['relative_humidity_2m'], 
									 						'apparent_temperature': data_forecast['hourly']['apparent_temperature'], 
															'rain': data_forecast['hourly']['rain']}).dropna(axis=1, how='all')])
		df_forecast['time'] = pd.to_datetime(df_forecast['time'])
	data_tuples.append((df_info, df_forecast))
	return data_tuples

