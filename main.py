from extract.PostgreSQL.postgre_collector import PostgreCollector
from extract.API.api_collector import APICollector
from extract.ParquetFile.parquet_collector import ParquetFileCollector
import os
import schedule
import time
import subprocess

def run_pipeline():
    # Executa funções de extração
    PostgreCollector().start()
    APICollector().start()
    ParquetFileCollector().start()
    time.sleep(5)
    # Executa o dbt
    os.chdir('transform')
    subprocess.run(['dbt','run'])

schedule.every().day.at("20:00").do(run_pipeline())

while True:
    schedule.run_pending()
    time.sleep(1)