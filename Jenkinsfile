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
<<<<<<< HEAD
        sh 'python tests.py'
=======
        sh 'python test.py'
>>>>>>> 0367c59422bd50b6a354f4499c54a7b754950c91
      }
    }
  }
}