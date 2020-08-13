pipeline {
  agent any
  stages {
    stage('stash code_base') {
      steps {
        stash(name: 'code_base', excludes: '.git')
      }
    }

    stage('Parrallel') {
      parallel {
        stage('Test') {
          agent {
            docker {
              image 'python:3.5.1'
            }

          }
          steps {
            unstash 'code_base'
            sh 'pip install -r requirements.txt'
            sh 'python tests.py'
          }
        }

        stage('zip codebase') {
          agent {
            docker {
              image 'ubuntu'
            }

          }
          steps {
            unstash 'code_base'
            sh 'apt-get update'
            sh 'apt-get install zip -y'
            sh 'zip -r test $PWD'
            archiveArtifacts 'test.zip'
          }
        }

      }
    }

    stage('Push to docker') {
      when {
        anyOf {
          expression {
            branch 'master'
          }

          expression {
            changeRequest()
          }

        }

      }
      environment {
        DOCKERCREDS = credentials('docker_login')
      }
      steps {
        unstash 'code_base'
        sh 'docker build -t itsmebenpax/ca_project:latest .'
        sh 'echo "$DOCKERCREDS_PSW" | docker login -u "$DOCKERCREDS_USR" --password-stdin'
        sh 'docker push "$DOCKERCREDS_USR/ca_project:latest"'
      }
    }

    stage('Functional Test') {
      steps {
        sh 'echo "All following sh cmds are mysteriously required and may not be deleted"'
        sh 'docker-compose down'
        sh 'docker ps'
        sh 'docker container rm pyApp'
        sh 'docker ps'
        sh 'docker-compose up -d'
        sh 'docker ps'
        sh 'docker logs pyApp'
        sh 'curl http://35.205.218.202:5000'
        sh 'docker-compose down'
      }
    }
  }
}