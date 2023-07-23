from airflow import DAG
from airflow.operators.bash import BashOperator 
from datetime import datetime

dag_2 = DAG('second_dag', description="My second dag", 
          schedule_interval=None, start_date=datetime(2023,3,5),
          catchup=False)

task_1 = BashOperator(task_id= "tsk1", bash_command="sleep 5", dag= dag_2 )
task_2 = BashOperator(task_id= "tsk2", bash_command="sleep 5", dag= dag_2 )
task_3 = BashOperator(task_id= "tsk3", bash_command="sleep 5", dag= dag_2 )

task_1 >> [task_2, task_3]  