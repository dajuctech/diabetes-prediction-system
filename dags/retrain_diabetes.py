from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta
import os

def retrain():
    os.system("python src/model/train.py")

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2023, 1, 1),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

with DAG('retrain_diabetes_model',
         default_args=default_args,
         schedule_interval='@daily',
         catchup=False) as dag:

    task = PythonOperator(
        task_id='retrain_model',
        python_callable=retrain
    )
