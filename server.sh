#/bin/bash

docker stop $(docker ps -a -q)
docker rm $(docker ps -a -q)

docker images rm dueruen/ca-project:latest
docker run dueruen/ca-project:latest
