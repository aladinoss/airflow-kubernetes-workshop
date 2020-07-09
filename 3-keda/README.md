
## Step 1:Install KEDA on your cluster

KEDA acts as a [Custom Controller](https://kubernetes.io/docs/concepts/architecture/controller/). 
Airflow users only need to deploy a single instance of KEDA *per cluster.*

To install KEDA use the following commands:
```shell script
helm repo add kedacore https://kedacore.github.io/charts
helm repo update
kubectl create namespace keda
helm install keda kedacore/keda --namespace keda 
```

## Step 2: Turn on KEDA for your airflow deployment
Once the KEDA deployment is running, set the following flags
to re-launch your airflow instance using the KEDA autoscaler.

```shell script
helm upgrade airflow \
  --reuse-values \
  --set workers.keda.enabled=true \
  --set env[0].name=AIRFLOW__CORE__PARALLELISM \
  --set env[0].value=30 \
  --set env[1].name=AIRFLOW__CORE__DAG_CONCURRENCY \
  --set env[1].value=30 \
  --namespace=${NAMESPACE} \
  .
```

