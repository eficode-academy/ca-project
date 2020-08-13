apt-get install -y zip unzip
zip -r ca-build.zip ./ -x '*.git*' '*.md*' '*Dockerfile*' '*Jenkinsfile*' '*.sh*' '*.png*'
