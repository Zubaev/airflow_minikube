from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime



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
    'depends_on_past': False,
    'start_date': datetime(2023, 7, 19),
    'email_on_failure': False,
    'email_on_retry': False,
}

dag = DAG('pascal', default_args=default_args, schedule_interval='@daily')

python_task = PythonOperator(
    task_id='python_task',
    python_callable=pascal_triangle(10),
    dag=dag,
)
