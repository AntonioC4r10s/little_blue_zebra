import requests
import time


# My Api
API_WEATHER_KEY = 'aec33dc9860ee24df765420ab8a8dca1'


# Important cities in the world 
cities = ['New York', 'London', 'Tokyo']


# Function to return json informations
def data_weather_now(city):
    response = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_WEATHER_KEY}')
    if response.status_code == 200:
        # print(response.json())
        return response.json()
    
    else: 
        print(f'Erro: {response.status_code}')    


# Function to return coord city informations
def coord(city):
    response = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_WEATHER_KEY}')

    if response.status_code == 200:
        data = response.json()
        lat = float(data['coord']['lat'])
        lon = float(data['coord']['lon'])
        lat = round(lat, 2)
        lon = round(lon, 2)
        # print(f'lat: {lat}, lon: {lon}')
        return lat, lon

    else: 
        print(f'Erro: {response.status_code}')

def past():
    return 0


def forecast(city):
    lat, lon = coord(city)
    API_LINK = f'https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&hourly=temperature_2m,'\
                'relative_humidity_2m,apparent_temperature,rain&daily=temperature_2m_max,temperature_2m_min'
    response = requests.get(API_LINK)
    response = response.json()
    # print(response)
    return response


def main_data_weather(cities: list):
    all_data = []
    for city in cities:
        actual_city = data_weather_now(city)
        forecast_city = forecast(city)
        past_city  = past()
        city_info = (actual_city, forecast_city, past_city)
        all_data.append(city_info)
    return all_data


data_example = ''
