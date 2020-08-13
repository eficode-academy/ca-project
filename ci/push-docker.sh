#!/bin/bash

docker push "$docker_username/flaskproject:1.0-${GIT_COMMMIT::4}"
docker push "$docker_username/flaskproject:latest"
wait