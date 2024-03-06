from extract.PostgreSQL.postgre_collector import PostgreCollector
from extract.API.api_collector import APICollector
from extract.ParquetFile.parquet_collector import ParquetFileCollector

PostgreCollector().start()
APICollector().start()
ParquetFileCollector().start()