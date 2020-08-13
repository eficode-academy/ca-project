pipeline {
  agent any
  environment {
    docker_username = 'nibug18'
  }
  stages {
    stage('Clone Down') {
      steps {
        stash excludes: '.git', name: 'code'
      }
    }

    stage('Test') {
      agent {
        docker {
          image 'python'
        }
      }
      options {
        skipDefaultCheckout(true)
      }
      steps {
        unstash 'code'
        sh 'pip3 install -r requirements.txt'
        sh 'python3 tests.py'
      }
    }

    stage('"Build"') {
      agent {
        docker {
          image 'python'
        }
      }
      options {
        skipDefaultCheckout(true)
      }
      steps {
        unstash 'code'
        sh 'python3 setup.py check'
        sh 'python3 setup.py sdist'
        stash 'code'
      }
    }

    stage('Parallel Stage') {
      parallel {
        stage('Package') {
          agent {
            docker {
              image 'python'
            }
          }
          options {
            skipDefaultCheckout(true)
          }
          steps {
            unstash 'code'
            archiveArtifacts 'dist/'
          }
        }
        stage('Push to docker') {
          when {
            branch 'master'
          }
          
          environment {
            DOCKERCREDS = credentials('docker_login')
          }
          steps {
            unstash 'code'
            sh 'ci/build-docker.sh'
            sh 'echo "$DOCKERCREDS_PSW" | docker login -u "$DOCKERCREDS_USR" --password-stdin'
            sh 'ci/push-docker.sh'
          }
        }
      }
    }
  }
}
