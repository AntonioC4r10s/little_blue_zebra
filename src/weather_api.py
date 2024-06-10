import requests
import time


# My Api
API_WEATHER_KEY = 'aec33dc9860ee24df765420ab8a8dca1'


# Important cities in the world 
cities = ['New York', 'London']


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


# data_example = [({'coord': {'lon': -74.006, 'lat': 40.7143}, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}], 'base': 'stations', 'main': {'temp': 296.17, 'feels_like': 296.07, 'temp_min': 293.12, 'temp_max': 298.7, 'pressure': 1002, 'humidity': 59}, 'visibility': 10000, 'wind': {'speed': 8.05, 'deg': 308, 'gust': 10.73}, 'clouds': {'all': 75}, 'dt': 1717953966, 'sys': {'type': 2, 'id': 2008101, 'country': 'US', 'sunrise': 1717925084, 'sunset': 1717979176}, 'timezone': -14400, 'id': 5128581, 'name': 'New York', 'cod': 200}, {'latitude': 40.710335, 'longitude': -73.99307, 'generationtime_ms': 0.14400482177734375, 'utc_offset_seconds': 0, 'timezone': 'GMT', 'timezone_abbreviation': 'GMT', 'elevation': 27.0, 'hourly_units': {'time': 'iso8601', 'temperature_2m': '°C', 'relative_humidity_2m': '%', 'apparent_temperature': '°C', 'rain': 'mm'}, 'hourly': {'time': ['2024-06-09T00:00', '2024-06-09T01:00', '2024-06-09T02:00', '2024-06-09T03:00', '2024-06-09T04:00', '2024-06-09T05:00', '2024-06-09T06:00', '2024-06-09T07:00', '2024-06-09T08:00', '2024-06-09T09:00', '2024-06-09T10:00', '2024-06-09T11:00', '2024-06-09T12:00', '2024-06-09T13:00', '2024-06-09T14:00', '2024-06-09T15:00', '2024-06-09T16:00', '2024-06-09T17:00', '2024-06-09T18:00', '2024-06-09T19:00', '2024-06-09T20:00', '2024-06-09T21:00', '2024-06-09T22:00', '2024-06-09T23:00', '2024-06-10T00:00', '2024-06-10T01:00', '2024-06-10T02:00', '2024-06-10T03:00', '2024-06-10T04:00', '2024-06-10T05:00', '2024-06-10T06:00', '2024-06-10T07:00', '2024-06-10T08:00', '2024-06-10T09:00', '2024-06-10T10:00', '2024-06-10T11:00', '2024-06-10T12:00', '2024-06-10T13:00', '2024-06-10T14:00', '2024-06-10T15:00', '2024-06-10T16:00', '2024-06-10T17:00', '2024-06-10T18:00', '2024-06-10T19:00', '2024-06-10T20:00', '2024-06-10T21:00', '2024-06-10T22:00', '2024-06-10T23:00', '2024-06-11T00:00', '2024-06-11T01:00', '2024-06-11T02:00', '2024-06-11T03:00', '2024-06-11T04:00', '2024-06-11T05:00', '2024-06-11T06:00', '2024-06-11T07:00', '2024-06-11T08:00', '2024-06-11T09:00', '2024-06-11T10:00', '2024-06-11T11:00', '2024-06-11T12:00', '2024-06-11T13:00', '2024-06-11T14:00', '2024-06-11T15:00', '2024-06-11T16:00', '2024-06-11T17:00', '2024-06-11T18:00', '2024-06-11T19:00', '2024-06-11T20:00', '2024-06-11T21:00', '2024-06-11T22:00', '2024-06-11T23:00', '2024-06-12T00:00', '2024-06-12T01:00', '2024-06-12T02:00', '2024-06-12T03:00', '2024-06-12T04:00', '2024-06-12T05:00', '2024-06-12T06:00', '2024-06-12T07:00', '2024-06-12T08:00', '2024-06-12T09:00', '2024-06-12T10:00', '2024-06-12T11:00', '2024-06-12T12:00', '2024-06-12T13:00', '2024-06-12T14:00', '2024-06-12T15:00', '2024-06-12T16:00', '2024-06-12T17:00', '2024-06-12T18:00', '2024-06-12T19:00', '2024-06-12T20:00', '2024-06-12T21:00', '2024-06-12T22:00', '2024-06-12T23:00', '2024-06-13T00:00', '2024-06-13T01:00', '2024-06-13T02:00', '2024-06-13T03:00', '2024-06-13T04:00', '2024-06-13T05:00', '2024-06-13T06:00', '2024-06-13T07:00', '2024-06-13T08:00', '2024-06-13T09:00', '2024-06-13T10:00', '2024-06-13T11:00', '2024-06-13T12:00', '2024-06-13T13:00', '2024-06-13T14:00', '2024-06-13T15:00', '2024-06-13T16:00', '2024-06-13T17:00', '2024-06-13T18:00', '2024-06-13T19:00', '2024-06-13T20:00', '2024-06-13T21:00', '2024-06-13T22:00', '2024-06-13T23:00', '2024-06-14T00:00', '2024-06-14T01:00', '2024-06-14T02:00', '2024-06-14T03:00', '2024-06-14T04:00', '2024-06-14T05:00', '2024-06-14T06:00', '2024-06-14T07:00', '2024-06-14T08:00', '2024-06-14T09:00', '2024-06-14T10:00', '2024-06-14T11:00', '2024-06-14T12:00', '2024-06-14T13:00', '2024-06-14T14:00', '2024-06-14T15:00', '2024-06-14T16:00', '2024-06-14T17:00', '2024-06-14T18:00', '2024-06-14T19:00', '2024-06-14T20:00', '2024-06-14T21:00', '2024-06-14T22:00', '2024-06-14T23:00', '2024-06-15T00:00', '2024-06-15T01:00', '2024-06-15T02:00', '2024-06-15T03:00', '2024-06-15T04:00', '2024-06-15T05:00', '2024-06-15T06:00', '2024-06-15T07:00', '2024-06-15T08:00', '2024-06-15T09:00', '2024-06-15T10:00', '2024-06-15T11:00', '2024-06-15T12:00', '2024-06-15T13:00', '2024-06-15T14:00', '2024-06-15T15:00', '2024-06-15T16:00', '2024-06-15T17:00', '2024-06-15T18:00', '2024-06-15T19:00', '2024-06-15T20:00', '2024-06-15T21:00', '2024-06-15T22:00', '2024-06-15T23:00'], 'temperature_2m': [25.2, 23.4, 22.8, 22.2, 21.0, 20.2, 20.1, 18.9, 18.7, 19.2, 19.2, 20.4, 20.7, 20.1, 20.9, 20.1, 22.7, 23.6, 24.4, 24.3, 24.7, 25.0, 24.7, 24.2, 22.7, 20.9, 19.5, 18.7, 17.3, 16.2, 15.8, 15.2, 14.7, 14.5, 14.5, 16.1, 18.1, 19.9, 21.6, 23.0, 23.7, 24.0, 24.4, 23.6, 23.2, 22.9, 23.0, 22.4, 21.0, 19.3, 18.0, 17.0, 16.2, 15.4, 14.7, 14.2, 13.7, 13.2, 13.2, 15.2, 16.6, 17.4, 18.8, 20.3, 21.8, 23.1, 24.3, 24.7, 22.9, 22.0, 22.4, 22.9, 22.3, 21.5, 21.0, 20.4, 20.1, 19.8, 19.7, 19.4, 18.8, 17.6, 17.2, 18.0, 19.2, 20.8, 22.3, 23.6, 24.2, 24.1, 24.0, 24.1, 23.7, 23.9, 22.6, 22.1, 23.3, 22.9, 22.2, 21.4, 20.9, 20.4, 19.9, 19.5, 19.1, 18.7, 18.6, 19.2, 20.4, 22.2, 23.7, 25.0, 25.7, 25.7, 25.0, 24.2, 24.5, 24.6, 23.5, 26.0, 24.0, 22.9, 22.3, 21.8, 21.1, 21.1, 20.8, 20.4, 19.9, 19.8, 19.9, 20.3, 21.2, 23.1, 25.6, 26.8, 25.5, 23.1, 21.4, 21.3, 22.0, 22.5, 22.3, 21.9, 21.4, 20.7, 20.0, 19.3, 18.6, 18.0, 17.4, 16.8, 16.3, 16.1, 16.3, 16.9, 17.7, 18.8, 20.2, 21.6, 22.8, 24.0, 24.9, 25.5, 25.9, 26.0, 25.5, 24.6], 'relative_humidity_2m': [35, 41, 46, 48, 55, 57, 55, 67, 68, 62, 67, 66, 70, 69, 61, 75, 63, 56, 52, 48, 39, 37, 39, 36, 37, 43, 49, 51, 57, 61, 62, 64, 64, 66, 76, 74, 68, 61, 53, 46, 43, 42, 40, 40, 39, 39, 39, 39, 42, 46, 52, 58, 64, 69, 74, 78, 82, 84, 85, 82, 75, 54, 48, 43, 38, 34, 33, 35, 43, 50, 51, 50, 51, 52, 56, 61, 62, 64, 62, 60, 59, 60, 60, 57, 52, 47, 43, 40, 39, 41, 42, 44, 48, 48, 55, 60, 56, 57, 59, 62, 64, 66, 67, 68, 69, 70, 70, 67, 61, 53, 48, 43, 42, 44, 48, 52, 54, 55, 64, 54, 59, 60, 61, 63, 66, 65, 65, 69, 74, 78, 79, 78, 75, 68, 58, 55, 64, 79, 89, 89, 86, 83, 85, 89, 90, 87, 81, 77, 76, 75, 75, 75, 74, 73, 71, 69, 64, 55, 45, 36, 31, 29, 27, 25, 25, 25, 27, 31], 'apparent_temperature': [22.9, 22.1, 21.7, 21.4, 20.5, 19.9, 19.2, 18.8, 19.0, 19.2, 19.2, 20.0, 20.2, 18.9, 18.8, 19.2, 21.1, 23.4, 22.1, 22.1, 22.2, 21.7, 21.7, 20.9, 19.9, 18.9, 17.9, 16.8, 15.9, 15.2, 14.6, 13.9, 13.3, 12.9, 13.6, 15.5, 17.3, 18.5, 20.6, 21.6, 21.4, 21.5, 22.2, 20.4, 20.3, 20.0, 20.2, 19.6, 18.7, 17.4, 16.5, 15.6, 15.0, 14.4, 13.8, 13.4, 13.0, 12.2, 12.4, 14.5, 15.8, 14.9, 17.0, 19.5, 21.8, 23.6, 25.5, 24.9, 21.1, 19.1, 20.5, 22.3, 21.0, 19.4, 19.2, 18.9, 18.6, 18.8, 18.8, 18.0, 17.0, 15.6, 15.3, 16.3, 17.6, 19.6, 22.3, 24.7, 25.4, 24.7, 23.7, 23.3, 21.9, 21.9, 20.8, 20.4, 22.9, 22.8, 21.5, 20.8, 20.4, 20.0, 19.7, 19.1, 18.8, 18.4, 18.3, 18.9, 20.0, 21.7, 23.5, 25.2, 25.9, 25.7, 24.3, 22.7, 22.4, 22.3, 21.4, 24.8, 22.4, 20.7, 20.5, 20.0, 19.6, 19.7, 19.2, 19.0, 18.9, 19.0, 19.3, 19.8, 20.8, 23.0, 25.8, 27.9, 26.9, 24.9, 23.3, 23.4, 24.3, 24.7, 24.5, 23.8, 23.2, 22.8, 19.9, 17.3, 16.5, 16.4, 16.4, 15.9, 15.4, 15.0, 15.0, 15.2, 15.5, 16.0, 17.1, 18.7, 20.4, 22.3, 23.4, 23.8, 23.7, 23.0, 22.0, 21.5], 'rain': [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.3, 0.3, 0.3, 0.2, 0.2, 0.2, 0.1, 0.1, 0.1, 0.05, 0.05, 0.05, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]}, 'daily_units': {'time': 'iso8601', 'temperature_2m_max': '°C', 'temperature_2m_min': '°C'}, 'daily': {'time': ['2024-06-09', '2024-06-10', '2024-06-11', '2024-06-12', '2024-06-13', '2024-06-14', '2024-06-15'], 'temperature_2m_max': [25.2, 24.4, 24.7, 24.2, 26.0, 26.8, 26.0], 'temperature_2m_min': [18.7, 14.5, 13.2, 17.2, 18.6, 19.8, 16.1]}}, 0)]

