import sqlite3  # Importa o módulo sqlite3 para trabalhar com bancos de dados SQLite
import pandas as pd  # Importa a biblioteca pandas para manipulação de dataframes


# Definindo o caminho e o nome do banco de dados
PATH = ''
NAME_DB = PATH + 'little_blue_zebra.db'


# Nomes das tabelas no banco de dados
DATA_INFO_TABLE_NAME = 'actual_data'
DATA_FORECAST_TABLE_NAME = 'forecast_data'


# Função para inicializar o banco de dados
def init_db():
    db_connection = sqlite3.connect(NAME_DB)  # Conecta ao banco de dados
    db_connection.close()  # Fecha a conexão


# Função para salvar um dataframe no banco de dados (tabela actual_data)
def df_info_to_sql(df_info: pd.DataFrame):
    db_connection = sqlite3.connect(NAME_DB)  # Conecta ao banco de dados
    # Salva o dataframe na tabela 'actual_data', adicionando os dados à tabela existente
    df_info.to_sql(DATA_INFO_TABLE_NAME, con=db_connection, if_exists='append', index=False)
    db_connection.close()  # Fecha a conexão


# Função para salvar um dataframe no banco de dados (tabela forecast_data)
def df_forecast_to_sql(df_forecast: pd.DataFrame):
    db_connection = sqlite3.connect(NAME_DB)  # Conecta ao banco de dados
    # Salva o dataframe na tabela 'forecast_data', substituindo os dados existentes
    df_forecast.to_sql(DATA_FORECAST_TABLE_NAME, con=db_connection, if_exists='replace', index=False)
    db_connection.close()  # Fecha a conexão


# Função para ler todos os dados da tabela actual_data e retornar como um dataframe
def read_df_info():
    db_connection = sqlite3.connect(NAME_DB)  # Conecta ao banco de dados
    # Executa uma consulta SQL para ler todos os dados da tabela 'actual_data'
    df_info = pd.read_sql_query(f'SELECT * FROM {DATA_INFO_TABLE_NAME}', db_connection)
    print(df_info)  # Imprime o dataframe
    db_connection.close()  # Fecha a conexão
    return df_info  # Retorna o dataframe


# Função para ler todos os dados da tabela forecast_data e retornar como um dataframe
def read_df_forecast():
    db_connection = sqlite3.connect(NAME_DB)  # Conecta ao banco de dados
    # Executa uma consulta SQL para ler todos os dados da tabela 'forecast_data'
    df_forecast = pd.read_sql_query(f'SELECT * FROM {DATA_FORECAST_TABLE_NAME}', db_connection)
    # print(df_forecast)  # Imprime o dataframe (comentado)
    db_connection.close()  # Fecha a conexão
    return df_forecast  # Retorna o dataframe


# Função para ler dados da tabela actual_data filtrados por cidade e imprimir como um dataframe
def read_df_info_to_city(city):
    db_connection = sqlite3.connect(NAME_DB)  # Conecta ao banco de dados
    # Executa uma consulta SQL para ler dados da tabela 'actual_data' filtrados por cidade
    df_info = pd.read_sql_query(f"SELECT * FROM {DATA_INFO_TABLE_NAME} WHERE name='{city}'", db_connection)
    print(df_info)  # Imprime o dataframe
    db_connection.close()  # Fecha a conexão


# Função para ler dados da tabela forecast_data filtrados por cidade e imprimir como um dataframe
def read_df_forecast_to_city(city):
    db_connection = sqlite3.connect(NAME_DB)  # Conecta ao banco de dados
    # Executa uma consulta SQL para ler dados da tabela 'forecast_data' filtrados por cidade
    df_forecast = pd.read_sql_query(f"SELECT * FROM {DATA_FORECAST_TABLE_NAME} WHERE name='{city}'", db_connection)
    print(df_forecast)  # Imprime o dataframe
    db_connection.close()  # Fecha a conexão
