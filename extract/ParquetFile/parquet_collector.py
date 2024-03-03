from google.cloud import bigquery
from google.oauth2 import service_account
import os
from dotenv import load_dotenv

load_dotenv()

class ParquetFileCollector():
    def __init__(self):
        pass

    def start(self):
        self.exportToCloud()
        return None

    def exportToCloud(self):
        key_path = os.environ.get("GCP_KEY_PATH")
        credentials = service_account.Credentials.from_service_account_file(key_path)
        client = bigquery.Client(credentials=credentials)
        
        source_uri = "https://storage.googleapis.com/challenge_junior/categoria.parquet"

        table_ref = client.dataset('raw_data').table('categorias')

        job_config = bigquery.LoadJobConfig()
        job_config.source_format = bigquery.SourceFormat.PARQUET
        job_config.autodetect = True

        job = client.load_table_from_uri(
            source_uri, table_ref, job_config=job_config
        )
        job.result()
        return None