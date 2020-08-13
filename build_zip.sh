apt-get install -y zip unzip
zip -r cabuild.zip ./ -x '*.git*' '*.md*' '*Dockerfile*' '*Jenkinsfile*' '*.sh*' '*.png*'
