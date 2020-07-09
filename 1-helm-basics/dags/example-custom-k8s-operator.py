from airflow import DAG
from datetime import datetime, timedelta
from airflow.contrib.operators.kubernetes_pod_operator import KubernetesPodOperator
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

dag = DAG('example_custom_kubernetes_pod',
          schedule_interval='@once',
          default_args=default_args)

compute_resource = {'request_cpu': '200m', 'request_memory': '1Gi', 'limit_cpu': '200m', 'limit_memory': '1Gi'}


class MyK8sOperator(KubernetesPodOperator):
    def __init__(self, namespace, name, env_vars=None, *args, **kwargs):
        my_labels = {
            **kwargs['labels'],
            "foo": "bar",
            "hello": "world",
        }

        image = "hello-world"
        env_vars = env_vars or {}
        all_env_vars = {
            **env_vars,
            "MY_EXTRA_ENV_VAR": "value"
        }

        super().__init__(namespace=namespace, image=image, name=name, labels=my_labels, env_vars=all_env_vars, *args, **kwargs)


with dag:
    k = MyK8sOperator(
        namespace=namespace,
        name="custom-pod",
        task_id='run_custom_pod',
        command='sleep $[ ( $RANDOM % 30 )  + 1 ]s && date',
        resources=compute_resource,
        labels={"initial_label": "true"},

    )
