#!/bin/sh

docker container prune -f
docker pull grameaway/codechan:latest
docker container run -d -p 5000:5000 --rm --name codechan grameaway/codechan

touch response.txt
sleep 3
curl -sL -w "%{http_code}" -I "$1:5000" -o /dev/null > response.txt
if grep -q 200 "response.txt"; then
    docker container stop $(docker ps -a -q)
    echo "Succes!"
    exit 0
fi
docker container stop $(docker ps -a -q)
echo "Failed!"
exit N
