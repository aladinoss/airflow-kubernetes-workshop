
Installing KEDA on your cluster

```shell script
helm repo add kedacore https://kedacore.github.io/charts
helm repo update
kubectl create namespace keda
helm install keda kedacore/keda --namespace keda 
```

Add KEDA to existing deployment(wait for running pods to finish first)
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

