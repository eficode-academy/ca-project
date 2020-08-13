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
            sh 'zip test $PWD'
            archiveArtifacts 'test.zip'
          }
        }

      }
    }

    stage('Push to docker') {
      environment {
        DOCKERCREDS = credentials('docker_login')
      }
      steps {
        unstash 'code_base'
        sh 'ci/build-docker.sh'
        sh 'echo "$DOCKERCREDS_PSW" | docker login -u "$DOCKERCREDS_USR" --password-stdin'
        sh 'ci/push-docker.sh'
      }
    }

  }
}