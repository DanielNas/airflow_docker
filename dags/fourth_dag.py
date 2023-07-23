from airflow import DAG
from airflow.operators.bash import BashOperator 
from datetime import datetime

with DAG('fourth_dag', description="My fourth dag", 
          schedule_interval=None, start_date=datetime(2023,3,5),
          catchup=False) as dag:

    task_1 = BashOperator(task_id= "tsk1", bash_command="sleep 5" )
    task_2 = BashOperator(task_id= "tsk2", bash_command="sleep 5" )
    task_3 = BashOperator(task_id= "tsk3", bash_command="sleep 5" )

task_1.set_upstream(task_2)
task_2.set_upstream(task_3)