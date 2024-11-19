from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime


n = 10

def pascal_triangle(n):
    matrix = []
    for x in range(n):
        rows = []
        for y in range(x + 1):
            result = comb(x, y)
            rows.append(result)
        matrix.append(rows)
    return matrix

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
