apt-get install -y zip unzip
sudo zip -r ca-build.zip ./ -x '*.git*' '*.md*' '*Dockerfile*' '*Jenkinsfile*' '*.sh*' '*.png*'
