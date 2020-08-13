#!/bin/bash

docker push "$docker_username/codechan-app:1.0-${GIT_COMMIT::4}" 
docker push "$docker_username/codechan-app:latest" &
wait