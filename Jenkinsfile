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
        sh 'python3 test.py'
      }
    }

  }
}