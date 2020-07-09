USERNAME=dimberman
VERSION=$1
docker build -t ${USERNAME}/helm-test-image:${VERSION} .
docker push ${USERNAME}/helm-test-image:${VERSION}
