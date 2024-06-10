import requests

lat, lon = 41.39, 2.16
# api = 'https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&hourly=temperature_2m'
api = 'https://api.open-meteo.com/v1/forecast?latitude=41.39&longitude=2.16&hourly=temperature_2m,relative_humidity_2m,apparent_temperature,rain&daily=temperature_2m_max,temperature_2m_min'
print(lat, lon)
response = requests.get(api)
response = response.json()
print(response)