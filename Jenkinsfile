pipeline {
  agent any
  stages {
    stage('HelloWorld') {
      steps {
        sh 'echo "hello world"'
      }
    }
    stage('clone down') {
      steps {
        stash(excludes: '.git', name: 'code')
      }
    }
    stage('Test'){
      steps{
        unstash 'code'
        sh 'apt-get update && apt-get install -y python3-pip'
        sh 'pip3 install -r app/requirements.txt'
        sh 'python3 tests.py'
      }
    }
  }
}