import psycopg2
import pandas as pd
from dotenv import load_dotenv
from google.oauth2 import service_account
import os

load_dotenv()

class PostgreCollector():
    def __init__(self):
        return None
    
    def start(self):
        conn = self.inputCredentials()
        df = self.tableToDataframe(conexao=conn)
        self.exportToCloud(dataframe=df)
        return True
    
    def inputCredentials(self):
        conexao = psycopg2.connect(
            host = os.environ.get("DB_HOST"),
            user = os.environ.get("DB_USER"),
            password = os.environ.get("DB_PASSWORD"),
            port = os.environ.get("DB_PORT"),
            database = os.environ.get("DB_DATABASE"),
        )
        return conexao
    
    def tableToDataframe(self, conexao):
        dataframe = pd.read_sql_query("SELECT id_venda, id_funcionario, id_categoria, TO_CHAR(data_venda,'YYYY-MM-DD') as data_venda, venda FROM PUBLIC.VENDA", conexao)
        return dataframe

    def exportToCloud(self,dataframe:pd.DataFrame):
        key_path = os.environ.get("GCP_KEY_PATH")
        credentials = service_account.Credentials.from_service_account_file(key_path)
        dataframe.to_gbq(credentials=credentials, destination_table='raw_data.vendas', if_exists="replace")
        return None