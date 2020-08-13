pipeline {
  agent {
    docker {
      image 'python'
    }

  }
  stages {
    stage('clone down') {
      steps {
        stash excludes: '.git', name: 'code'
      }
    }

    stage('Test') {
      steps {
        unstash 'code'
        sh 'pip3 install -r requirements.txt'
        sh 'python3 tests.py'
        stash excludes: '.git', name: 'code'
      }
    }

  }
}