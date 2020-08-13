pipeline {
  agent any
  stages {
    stage('initial') {
      steps {
        sh 'sh \'echo "hello world!"'
      }
    }
    parallel{
      stage('build artifacts'){
        steps{

        }
      }
      stage('build docker image'){
        steps{

        }
      }
    }
    stage('test'){
      steps{

      }
    }

    stage('push to docker'){
      steps{

      }
    }
    
    stage('deploy on server'){
      steps{
        
      }
    }

  }
}