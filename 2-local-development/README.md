# Local Development

To best create a Local Development environment that mimics a Kubernetes deployment,
 we recommend you use a Docker Compose. The upstream airflow commmunity is currently working
 on an official docker-compose image, but until that is upstreamed please feel free to check out
[the docker-compose astronomer uses](https://github.com/astronomer/astro-cli/blob/master/airflow/include/composeyml.go)
for our deployments.