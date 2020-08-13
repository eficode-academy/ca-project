pipeline {
  agent any
  environment {
    docker_username = 'sieben8nein'
  }
  stages {
    stage('Clone down') {
      steps {
        stash(excludes: '.git', name: 'code')
      }
    }
    stage('Test') {
      steps{
        unstash 'code'
        sh 'apt-get update && apt-get install -y python3-pip'
        sh 'pip3 install -r app/requirements.txt'
        sh 'python3 tests.py'
      }
    }
    stage("Dockerize & Archive artifacts") {
      parallel {
        stage("Dockerize") {
          environment {
            DOCKERCREDS = credentials('docker_login') //use the credentials just created in this stage
            }
            steps {
            unstash 'code'
            sh 'echo "$DOCKERCREDS_PSW" | docker login -u "$DOCKERCREDS_USR" --password-stdin'
            sh 'docker build -t $docker_username/devopsproject .'
            stash(name: 'image')
          }
        }
      stage("Archive artifacts") {
        steps {
          unstash 'code'
          sh 'apt-get update && apt-get install -y zip unzip'
          sh 'zip -r project_artifact.zip .'
          sh 'ls -l project_artifact.zip'
          archive "project_artifact.zip"
        }
      }
    }
  }
    stage("Push docker image"){
      environment {
        DOCKERCREDS = credentials('docker_login') //use the credentials just created in this stage
      }
      steps{
        unstash 'image'
        sh 'echo "$DOCKERCREDS_PSW" | docker login -u "$DOCKERCREDS_USR" --password-stdin'
        sh 'docker push $docker_username/devopsproject'
      }
    }
  }
}
