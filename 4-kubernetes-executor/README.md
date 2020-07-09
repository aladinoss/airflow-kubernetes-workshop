# The KubernetesExecutor


```shell script
VERSION=0.0.2
docker build -t ${USERNAME}/helm-test-image:${VERSION} .
docker push ${USERNAME}/helm-test-image:${VERSION} 
helm upgrade airflow \
    --reuse-values \
    --set executor=KubernetesExecutor \
    --set images.airflow.tag=${VERSION}  \
    --namespace=${NAMESPACE} \
    .
```