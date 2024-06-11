import pandas as pd  # Importa a biblioteca pandas para manipulação de dataframes
import warnings  # Importa a biblioteca warnings para lidar com avisos
import datetime  # Importa a biblioteca datetime para manipulação de datas e horas
from weather_api import API_WEATHER_KEY, cities, data_weather_now, coord, data_example, main_data_weather  # Importa funções e constantes relacionadas à API de clima
from databases import df_info_to_sql, df_forecast_to_sql, read_df_info  # Importa funções para trabalhar com bancos de dados

warnings.simplefilter(action='ignore', category=FutureWarning)  # Ignora futuros avisos


# Função para atualizar os dados climáticos
def update():
    data = main_data_weather(cities=cities)  # Obtém os dados climáticos para todas as cidades
    data = extract(data=data)  # Extrai os dados e converte para dataframes
    df_info_to_sql(df_info=data[0][0])  # Salva os dados climáticos atuais no banco de dados
    df_forecast_to_sql(df_forecast=data[0][1])  # Salva os dados de previsão do tempo no banco de dados
    print('updated!')  # Imprime uma mensagem indicando que os dados foram atualizados com sucesso


# Função para extrair os dados climáticos e convertê-los para dataframes
def extract(data: list):

    data_tuples = []  # Inicializa uma lista para armazenar tuplas de dataframes
    index_data_actual = 1  # Inicializa o índice dos dados climáticos atuais

    # Dataframe para armazenar informações climáticas atuais
    df_info = pd.DataFrame(columns=['name', 'country', 'lat', 'lon', 'wind', 'humidity', 'temperature', 'time'])

    # Dataframe para armazenar informações de previsão do tempo
    df_forecast = pd.DataFrame(columns=['name', 'time', 'temperature', 'relative_humidity', 
                                         'apparent_temperature', 'rain'])

    # Itera sobre os dados climáticos de cada cidade
    for data_city in data:
        data_actual = data_city[0]  # Dados climáticos atuais da cidade
        data_forecast = data_city[1]  # Dados de previsão do tempo da cidade
        data_past = data_city[2]  # Dados climáticos passados da cidade

        # Adiciona as informações climáticas atuais à dataframe df_info
        df_info = pd.concat([df_info, 
                            pd.DataFrame({'name': data_actual['name'], 
                                          'country': data_actual['sys']['country'], 
                                          'lat': data_actual['coord']['lat'], 
                                          'lon': data_actual['coord']['lon'],
                                          'wind': data_actual['wind']['speed'],
                                          'humidity': data_actual['main']['humidity'],
                                          'temperature': kelvin_to_celsius(data_actual['main']['temp']),
                                          'time': unix_to_utc(data_actual['dt'])},
                                          index=[index_data_actual]).dropna(axis=1, how='all')])
        
        index_data_actual += 1  # Incrementa o índice dos dados climáticos atuais

        # Adiciona as informações de previsão do tempo à dataframe df_forecast
        df_forecast = pd.concat([df_forecast, 
                                pd.DataFrame({'name': data_actual['name'],
                                              'time': data_forecast['hourly']['time'],
                                              'temperature': data_forecast['hourly']['temperature_2m'],
                                              'relative_humidity': data_forecast['hourly']['relative_humidity_2m'], 
                                              'apparent_temperature': data_forecast['hourly']['apparent_temperature'], 
                                              'rain': data_forecast['hourly']['rain']}).dropna(axis=1, how='all')])
        
        # Converte a coluna 'time' para o tipo de data e hora
        df_forecast['time'] = pd.to_datetime(df_forecast['time'])

    # Adiciona as dataframes df_info e df_forecast à lista de tuplas de dataframes
    data_tuples.append((df_info, df_forecast))
    
    return data_tuples  # Retorna a lista de tuplas de dataframes


# Função para converter a temperatura de Kelvin para Celsius
def kelvin_to_celsius(kelvin):
    celsius = kelvin - 273.15  # Converte Kelvin para Celsius
    celsius = round(celsius, 2)  # Arredonda para duas casas decimais
    return celsius  # Retorna a temperatura em Celsius


# Função para converter o timestamp UNIX para UTC
def unix_to_utc(unix):
    utc = datetime.datetime.utcfromtimestamp(unix)  # Converte o timestamp UNIX para UTC
    return utc  # Retorna o tempo em UTC

# update()  # Chama a função update para atualizar os dados climáticos
