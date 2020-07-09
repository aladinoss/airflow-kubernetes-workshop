from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.bash_operator import BashOperator
from airflow import configuration as conf

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2019, 1, 1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

namespace = "airflow"

# This will detect the default namespace locally and read the
# environment namespace when deployed to Astronomer.
in_cluster = True
config_file = None

dag = DAG('example_kubernetes_executor',
          schedule_interval='@once',
          default_args=default_args)

compute_resource = {
    'request_cpu': '200m',
    'request_memory': '1Gi',
    'limit_cpu': '200m',
    'limit_memory': '1Gi', }

labels = {
    "foo": "bar",
    "hello": "world",
}
executor_config = \
    {"KubernetesExecutor":
        {
            **compute_resource,
            "labels": {
                **labels
            }
        }
    }

with dag:
    t3 = BashOperator(
        dag=dag,
        task_id='bash_print_date2',
        executor_config=executor_config,
        bash_command='sleep $[ ( $RANDOM % 30 )  + 1 ]s && date')
