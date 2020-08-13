echo "Hello world"
#!/bin/bash
echo "Hello world 2"
[[ -z "${GIT_COMMIT}" ]] && Tag='local' || Tag="${GIT_COMMIT::4}"
[[ -z "${docker_username}" ]] && DockerRepo='' || DockerRepo="${docker_username}/"
docker build -t "${DockerRepo}flaskproject:latest" -t "${DockerRepo}flaskproject:1.0-$Tag" app/