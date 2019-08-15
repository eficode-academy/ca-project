#!/bin/bash

docker container stop $(docker ps -a -q)
docker container rm $(docker ps -a -q)

docker image rm dueruen/ca-project:$TARGET
docker container run --name=$TARGET -d -p 80:5000 -v "$(pwd)"/app.db:/app/app.db dueruen/ca-project:$TARGET
