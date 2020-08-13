pipeline {
  agent {
    docker {
      image 'python:3.5.1'
    }

  }
  stages {
    stage('stash code_base') {
      steps {
        stash(name: 'code_base', excludes: '.git')
      }
    }

    stage('Test') {
      parallel {
        stage('Test') {
          steps {
            sh 'pip install -r requirements.txt'
            sh 'python tests.py'
          }
        }

        stage('zip codebase') {
          steps {
            sh 'echo \'hello zip\' '
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