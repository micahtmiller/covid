from google.cloud import bigquery
from google.cloud.bigquery import SchemaField

class BigQuery:
    def __init__(self):
        pass

    def upload_data(self, table_id, df, schema):
        client = bigquery.Client()
        job_config = bigquery.LoadJobConfig(schema=schema)
        job = client.load_table_from_dataframe(
            df, table_id, job_config=job_config
        )
        job.result()