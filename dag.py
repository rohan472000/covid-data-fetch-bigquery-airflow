from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.utils.dates import days_ago
import requests
from datetime import timedelta
import json
from google.cloud import bigquery
from function import fetch_cases, save_cases

default_args = {
    'owner': 'my-covid-dag',
    'start_date': days_ago(2),
    'depends_on_past': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'covid_cases_fetch_push',
    default_args=default_args,
    description='Fetch daily COVID-19 case data and store it in BigQuery',
    schedule_interval='@daily',
)

fetch_cases_task = PythonOperator(
    task_id='fetch_cases',
    python_callable=fetch_cases,
    dag=dag,
)

save_cases_task = PythonOperator(
    task_id='save_cases',
    python_callable=save_cases,
    provide_context=True,
    dag=dag,
)


fetch_cases_task >> save_cases_task
