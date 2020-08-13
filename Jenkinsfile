pipeline {
  agent {
    docker {
      image 'python'
    }

  }
  stages {
    stage('error') {
      steps {
        sh 'echo "hej"'
      }
    }

    stage('Test') {
      steps {
        sh 'pip3 install -r requirements.txt'
        sh 'python3 tests.py'
      }
    }

  }
}