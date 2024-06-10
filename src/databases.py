import sqlite3
import pandas as pd


NAME_DB = 'little_blue_zebra.db'
DATA_INFO_TABLE_NAME = 'actual_data'
DATA_FORECAST_TABLE_NAME = 'forecast_data'


def init_db():
    db_connection = sqlite3.connect(NAME_DB)
    db_connection.close()
    

def df_info_to_sql(df_info: pd.DataFrame):
    db_connection = sqlite3.connect(NAME_DB)
    df_info.to_sql(DATA_INFO_TABLE_NAME, con=db_connection,if_exists='replace', index=False)
    db_connection.close()


def df_forecast_to_sql(df_forecast: pd.DataFrame):
    db_connection = sqlite3.connect(NAME_DB)
    df_forecast.to_sql(DATA_FORECAST_TABLE_NAME, con=db_connection, if_exists='replace', index=False)
    db_connection.close()


def read_df_info():
    db_connection = sqlite3.connect(NAME_DB)
    df_info = pd.read_sql_query(f'SELECT * FROM {DATA_INFO_TABLE_NAME}', db_connection)
    print(df_info)
    db_connection.close()
    

def read_df_forecast():
    db_connection = sqlite3.connect(NAME_DB)
    df_forecast = pd.read_sql_query(f'SELECT * FROM {DATA_FORECAST_TABLE_NAME}', db_connection)
    print(df_forecast)
    db_connection.close()
    

def read_df_info_to_city(city):
    db_connection = sqlite3.connect(NAME_DB)
    df_info = pd.read_sql_query(f"SELECT * FROM {DATA_INFO_TABLE_NAME} WHERE name='{city}'", db_connection)
    print(df_info)
    db_connection.close()


def read_df_forecast_to_city(city):
    db_connection = sqlite3.connect(NAME_DB)
    df_forecast = pd.read_sql_query(f"SELECT * FROM {DATA_FORECAST_TABLE_NAME} WHERE name='{city}'", db_connection)
    print(df_forecast)
    db_connection.close()

