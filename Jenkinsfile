pipeline {
  agent any
  environment{
      DOCKER_USER='d0wnt0wn3d'
  }
  stages {
    stage('clone') {
      steps {
        stash excludes: ".git/", name: "code"
      }
    }
    stage('parallel execution'){
      parallel{
        stage('build artifacts'){
            agent{
                docker{
                    image 'ubuntu:latest'
                }
            }
        options{
            skipDefaultCheckout()
        }
          steps{
            unstash 'code'
            sh 'apt-get update'
            sh 'apt-get install zip -y'
            sh 'zip -r artefacts.zip ./'
            archiveArtifacts 'artefacts.zip'
          }
        }
        stage('build docker image'){
            agent{
                docker{
                    image 'docker:latest'
                }
            }
            options{
                skipDefaultCheckout()
            }
          steps{
            unstash 'code'
            sh 'docker build -t ${DOCKER_USER}/codechan .'
            sh 'docker image ls'
            
            
          }
        }
      }
    }
    stage('test'){
        agent{
            docker{
                    image 'python:latest'
                }
        }
        options{
            skipDefaultCheckout()
        }
      steps{
        sh 'ls'
        sh 'pip install -r requirements.txt'
        sh 'python tests.py'
        sh 'python badtest.py'

      }
    }

    stage('push to docker'){
      steps{
        sh 'echo "hello world!"'
      }
    }
    
    stage('deploy on server'){
      steps{
        sh 'echo "hello world!"'
      }
    }

  }
}