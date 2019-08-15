#!/bin/sh

docker container stop $(docker ps -a -q)
docker container prune -f
docker pull grameaway/codechan:latest
docker container run -p 5000:5000 --rm --name codechan grameaway/codechan
