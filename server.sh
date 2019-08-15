#!/bin/bash

docker container stop $(docker ps -a -q)
docker container rm $(docker ps -a -q)

docker image rm dueruen/ca-project:latest
docker container run dueruen/ca-project:lates -d
