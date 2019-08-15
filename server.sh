#!/bin/bash

docker container stop $(docker ps -a -q)
docker container rm $(docker ps -a -q)

docker image rm dueruen/ca-project:latest
docker container run --name=server -d -p 80:5000 -v app.db:/app/ dueruen/ca-project:latest
