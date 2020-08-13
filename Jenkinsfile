pipeline {
  agent {
    docker {
      image 'https://hub.docker.com/r/mifor16/flaskproject'
    }

  }
  stages {
    stage('Python tests') {
      steps {
        sh 'python tests.py'
      }
    }

  }
}