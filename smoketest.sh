#!/bin/sh
docker container stop $(docker ps -a -q)
docker container prune -f
docker pull grameaway/codechan:latest
docker container run -d -p 5000:5000 --rm --name codechan grameaway/codechan

touch response.txt
sleep 10
curl -sL -w "%{http_code}" -I "$1:5000" -o /dev/null > response.txt
if grep -q 200 "response.txt"; then
    echo "Succes!"
    exit 0
fi
echo "Failed!"
exit N
