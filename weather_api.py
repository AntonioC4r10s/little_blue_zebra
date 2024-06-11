import requests  # Importa o módulo requests para fazer solicitações HTTP
import time  # Importa o módulo time para lidar com o tempo

# Minha chave de API do OpenWeatherMap
API_WEATHER_KEY = ''

# Lista de cidades importantes no mundo
cities = ['New York', 'London', 'Tokyo', 'Barcelona', 'Rio de Janeiro']

# Função para obter informações climáticas atuais de uma cidade
def data_weather_now(city):
    # Faz uma solicitação GET para a API do OpenWeatherMap para obter os dados climáticos atuais
    response = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_WEATHER_KEY}')
    
    if response.status_code == 200:  # Verifica se a solicitação foi bem-sucedida
        return response.json()  # Retorna os dados climáticos no formato JSON
    else:  # Se a solicitação não foi bem-sucedida
        print(f'Erro: {response.status_code}')  # Imprime o código de erro

# Função para obter as coordenadas geográficas de uma cidade
def coord(city):
    # Faz uma solicitação GET para a API do OpenWeatherMap para obter os dados climáticos
    response = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_WEATHER_KEY}')

    if response.status_code == 200:  # Verifica se a solicitação foi bem-sucedida
        data = response.json()  # Converte os dados recebidos para o formato JSON
        lat = float(data['coord']['lat'])  # Obtém a latitude da cidade
        lon = float(data['coord']['lon'])  # Obtém a longitude da cidade
        lat = round(lat, 2)  # Arredonda a latitude para duas casas decimais
        lon = round(lon, 2)  # Arredonda a longitude para duas casas decimais
        return lat, lon  # Retorna as coordenadas geográficas da cidade
    else:  # Se a solicitação não foi bem-sucedida
        print(f'Erro: {response.status_code}')  # Imprime o código de erro

# Função para obter previsões climáticas futuras para uma cidade
def forecast(city):
    lat, lon = coord(city)  # Obtém as coordenadas geográficas da cidade
    # Monta o link da API para obter a previsão do tempo com base nas coordenadas da cidade
    API_LINK = f'https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&hourly=temperature_2m,'\
                'relative_humidity_2m,apparent_temperature,rain&daily=temperature_2m_max,temperature_2m_min'
    response = requests.get(API_LINK)  # Faz uma solicitação GET para a API de previsão do tempo
    response = response.json()  # Converte os dados recebidos para o formato JSON
    return response  # Retorna a previsão do tempo em formato JSON


def past():
    return ''


# Função principal para obter dados climáticos para várias cidades
def main_data_weather(cities: list):
    all_data = []  # Inicializa uma lista vazia para armazenar os dados de todas as cidades
    for city in cities:  # Itera sobre todas as cidades na lista de cidades
        actual_city = data_weather_now(city)  # Obtém os dados climáticos atuais para a cidade
        forecast_city = forecast(city)  # Obtém a previsão do tempo para a cidade
        past_city  = past()  # Obtém dados climáticos passados para a cidade
        city_info = (actual_city, forecast_city, past_city)  # Combina os dados em uma tupla
        all_data.append(city_info)  # Adiciona a tupla à lista de dados
    return all_data  # Retorna todos os dados climáticos para todas as cidades

data_example = ''  # Exemplo de dados, inicialmente vazio, mas pode ser usados para testes offline
