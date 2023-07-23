from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.utils.task_group import TaskGroup
from datetime import datetime, timedelta
from airflow.operators.trigger_dagrun import TriggerDagRunOperator

default_args = {
    'depends_on_past' : False,
    'start_date': datetime(2023,7,11),
    'email' : ['test@gmail.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retray_delay': timedelta(seconds=10)
}

dag = DAG('defaults_args', description = "Example Dag",
        default_args = default_args,
        schedule_interval = '@hourly', start_date = datetime (2023,7,11),
        catchup=False, default_view = 'graph', tags = ['process', 'tag', 'pipeline'])

task_1 = BashOperator(task_id = "task_1", bash_command = "sleep 5", dag = dag, retries = 3)
task_2 = BashOperator(task_id = "task_2", bash_command = "sleep 5", dag = dag)
task_3 = BashOperator(task_id = "task_3", bash_command = "sleep 5", dag = dag)

task_1 >> task_2 >> task_3
