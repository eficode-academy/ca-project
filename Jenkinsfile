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
      }
    }

    stage('push to docker'){
      when {branch "master"}
        environment {
          DOCKERCREDS = credentials('docker-login')
        }
        steps {
            unstash 'code' //unstash the repository code
            sh 'echo "$DOCKERCREDS_PSW" | docker login -u "$DOCKERCREDS_USR" --password-stdin' //login to docker hub with the credentials above
            sh 'docker push "$DOCKER_USER/codechan:latest"'
            sh 'echo "this is requested from develop branch!'
        }
    }
    
    stage('deploy on server'){
      steps{
        sh 'echo "hello world!"'
      }
    }

  }
}