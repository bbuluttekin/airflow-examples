import datetime
import logging

from airflow import DAG
from airflow.operators.python_operator import PythonOperator


def first_prog():
    logging.info("This is my very first program for airflow")


dag = DAG(
    'lesson1.exercise1',
    start_date=datetime.datetime.now())

greet_task = PythonOperator(
    task_id="first_airflow_program",
    python_callable=first_prog,
    dag=dag
)
