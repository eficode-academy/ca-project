pipeline {
  agent any
  stages {
    stage('initial') {
      steps {
        sh 'echo "hello world!"'
      }
    }
    parallel{
      stage('build artifacts'){
         steps{
          sh 'echo "hello world!"'
         }
      }
      stage('build docker image'){
        steps{
          sh 'echo "hello world!"'
        }
      }
    }
    stage('test'){
      steps{
        sh 'echo "hello world!"' 
      }
    }

    stage('push to docker'){
      steps{
        sh 'echo "hello world!"'
      }
    }
    
    stage('deploy on server'){
      step{
        sh 'echo "hello world!"'
      }
    }

  }
}