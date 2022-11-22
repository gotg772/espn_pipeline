from airflow import DAG, Dataset
from airflow.decorators import task
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator
from airflow.sensors.filesystem import FileSensor
from airflow.providers.postgres.operators.postgres import PostgresOperator


from datetime import datetime



with DAG(
    dag_id = 'espn_pipeline',
    schedule = '@weekly',
    start_date = datetime(2022,8,1)
) as dag:

    api_data_fetch = BashOperator(
        task_id = 'fetch_data',
        bash_command = 'python /Users/colehoward/Documents/airflow-docker/dags/scripts/ingestion_script.py'
    )

    staging_ingestion = PostgresOperator(
        task_id = 'staging_ingestion',
        postgres_conn_id = 'espn_postgres',
        sql = '/Users/colehoward/Documents/airflow-docker/dags/sql/staging_ingestion.sql'
    )

    staging_to_prod = PostgresOperator(
        task_id = 'staging_to_prod',
        postgres_conn_id = 'espn_postgres',
        sql = '/Users/colehoward/Documents/airflow-docker/dags/sql/staging_to_prod.sql'


    )

