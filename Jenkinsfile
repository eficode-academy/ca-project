pipeline {
  agent any
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