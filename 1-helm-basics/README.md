# Launching the Airflow Helm Chart

```shell script
kubectl create namespace airflow
NAMESPACE=airflow
```


```shell script
helm install airflow \
    --set executor=CeleryExecutor \
    --namespace=${NAMESPACE} \
    --set workers.persistence.enabled=false \
    .
```


# Adding DAGs to the Airflow Helm Chart

```shell script
USERNAME=<your username>
VERSION=0.0.1
```
## Step 1: Create the docker image
```shell script
docker build -t ${USERNAME}/helm-test-image:${VERSION} .
```

## Step 2: Run the image to ensure DAGs have been copies

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
## Step 3: Install helm

```shell script
$ curl -fsSL -o get_helm.sh https://raw.githubusercontent.com/helm/helm/master/scripts/get-helm-3
$ chmod 700 get_helm.sh
$ ./get_helm.sh
```

## Step 4: Deploy using helm

We need to set our deployed image to use our test image


```shell script
helm upgrade airflow \
    --reuse-values \
    --set images.airflow.repository=${USERNAME}/helm-test-image \
    --set images.airflow.tag=${VERSION}  \
    --namespace=${NAMESPACE} \
    .
```