## Launching the Airflow Helm Chart

Because Helm 3 no longer has a tiller, we need to create a namespace for our airflow deployment before we use it.

Please feel free to use any namespace of your choosing. All following commands will follow the template

```shell script
NAMESPACE=airflow
kubectl create namespace $NAMESPACE
```


```shell script
helm install airflow \
    --set executor=CeleryExecutor \
    --namespace=${NAMESPACE} \
    --set workers.persistence.enabled=false \
    .
```

## Adding DAGs to the Airflow Helm Chart

```shell script
USERNAME=<your username>
VERSION=0.0.1
```

### Step 1: Create the docker image
```shell script
docker build -t ${USERNAME}/helm-test-image:${VERSION} .
```

### Step 2: Run the image to ensure DAGs have been copies

```shell script
docker run -it ${USERNAME}/helm-test-image:${VERSION}  bash
```

allowed commands on prod image:
* bash "@"
* python "@"
* airflow "@"

```shell script
docker push ${USERNAME}/helm-test-image:${VERSION} 
```

### Step 3: Deploy new image using helm

```shell script
helm upgrade airflow \
    --reuse-values \
    --set images.airflow.repository=${USERNAME}/helm-test-image \
    --set images.airflow.tag=${VERSION}  \
    --namespace=${NAMESPACE} \
    .
```