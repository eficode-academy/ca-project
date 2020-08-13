pipeline {
  agent {
    docker {
      image 'python'
    }
  }
  environment {
    docker_username = 'nibug18'
  }
  stages {
    stage('clone down') {
      steps {
        stash excludes: '.git', name: 'code'
      }
    }
    stage('Push to docker') {
      when {
        branch 'master'
      }
      environment {
        DOCKERCREDS = credentials('docker_login')
      }
      steps {
        unstash 'code'
        sh 'ci/build-docker.sh'
        sh 'echo "$DOCKERCREDS_PSW" | docker login -u "$DOCKERCREDS_USR" --password-stdin'
        sh 'ci/push-docker.sh'
      }
    }
  
    stage('Test') {
      steps {
        unstash 'code'
        sh 'pip3 install -r requirements.txt'
        sh 'python3 tests.py'
      }
    }
  }
  }