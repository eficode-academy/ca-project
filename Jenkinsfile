pipeline {
    agent any
  stages {
    stage('stash code_base') {
      steps {
        stash(name: 'code_base', excludes: '.git')
      }
    }

    stage('Parrallel') {
      parallel {
        stage('Test') {
          agent {
             docker {
               image 'python:3.5.1'
             }
           }
          steps {
            sh 'pip install -r requirements.txt'
            sh 'python tests.py'
          }
     }

        stage('zip codebase') {
          agent {
            docker {
              image 'alpine'
           }
          }
           steps {
            unstash 'code_base'
            sh 'apt install zip'
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
