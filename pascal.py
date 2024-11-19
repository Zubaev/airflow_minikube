from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime

def pascal_treug():
    n = 10
    for i in range(n):
        coef = 1
        for j in range(0, i + 1):
            print(coef, end=' ')
            coef = coef * (i - j) // (j + 1)
        print()

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 11, 19),
}

dag = DAG('pascal', default_args=default_args, schedule_interval='@daily')

python_task = PythonOperator(
    task_id='python_task',
    python_callable=my_function,
    dag=dag,
)
