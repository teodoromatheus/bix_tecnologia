import pandas as pd
from httpx import Client
from typing import List
import google.cloud
from google.oauth2 import service_account
import os
from dotenv import load_dotenv

load_dotenv()

class APICollector():
    def __init__(self):
        return None
    
    def start(self):
        lista = self.getAPI()
        df = self.listToDataframe(lista=lista)
        self.dataframeToCloud(df=df)
        return df

    def getAPI(self):
        lista = []
        BASE_URL = "https://us-central1-bix-tecnologia-prd.cloudfunctions.net/api_challenge_junior?id="
        client = Client()
        for post_id in range (1,10):
            try:
                response = client.get(f"{BASE_URL}{post_id}")
                lista.append([post_id,response.text])
            except Exception as e:
                print(f"Erro: {e}")
        client.close()
        return lista
    
    def listToDataframe(self, lista:List)->pd.DataFrame:
        df = pd.DataFrame(lista, columns=['id_funcionario','nome_funcionario'])
        return df
    
    def dataframeToCloud(self, df:pd.DataFrame):
        key_path = os.environ.get("GCP_KEY_PATH")
        credentials = service_account.Credentials.from_service_account_file(key_path)
        df.to_gbq(credentials=credentials, destination_table='raw_data.funcionarios', if_exists="replace")
        