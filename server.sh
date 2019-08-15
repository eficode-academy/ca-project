docker container stop $(docker ps -a -q)
docker image rm grameaway/codechan
docker container run -p 5000:5000 --rm --name codechan grameaway/codechan
