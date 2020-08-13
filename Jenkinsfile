pipeline {
  agent {
    docker {
      image 'python:3.5.1'
    }

  }
  stages {
    stage('build') {
      parallel {
        stage('build') {
          steps {
            sh 'pip install -r requirements.txt'
            sh 'python run.py'
          }
        }

        stage('Test') {
          steps {
            sh 'python tests.py'
          }
        }

      }
    }

    stage('Push to docker') {
      steps {
        sh 'echo "psuhing"'
      }
    }

  }
}