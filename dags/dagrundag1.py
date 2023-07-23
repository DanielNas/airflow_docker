from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.utils.task_group import TaskGroup
from datetime import datetime
from airflow.operators.trigger_dagrun import TriggerDagRunOperator

dag = DAG('dagrundag1', description="Dag run Dag", 
          schedule_interval=None, start_date=datetime(2023,3,5),
          catchup=False)

task_1 = BashOperator(task_id= "tsk1", bash_command="sleep 5", dag= dag )
task_2 = TriggerDagRunOperator(task_id= "tsk2", trigger_dag_id="dagrundag2", dag= dag )


task_1 >> task_2
