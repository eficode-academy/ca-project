pipeline {
  agent {
    docker {
      image 'python:3.5.1'
    }

  }
  stages {
    stage('build') {
      steps {
        sh 'pip install -r requirements.txt'
        sh 'python run.py'
      }
    }

  }
}