pipeline {
  agent any
  environment {
    docker_username = 'sieben8nein'
  }
  stages {
    stage('HelloWorld') {
      steps {
        sh 'echo "hello world"'
      }
    }
    stage('clone down') {
      steps {
        stash(excludes: '.git', name: 'code')
      }
    }
    stage('Test'){
      steps{
        unstash 'code'
        sh 'apt-get update && apt-get install -y python3-pip'
        sh 'pip3 install -r app/requirements.txt'
        sh 'python3 tests.py'
      }
    }
    stage("dockerize"){
      environment {
        DOCKERCREDS = credentials('docker_login') //use the credentials just created in this stage
      }
      steps{
        unstash 'code'
        sh 'echo "$DOCKERCREDS_PSW" | docker login -u "$DOCKERCREDS_USR" --password-stdin'
        sh 
        sh 'docker build -t $docker_username/devopsproject .'
      }
    }

  }
}