pipeline {
  agent any
  enviornment {
    docker_username = 'mathn16'
  }
  stages {
    stage('Dockerrize app') {
      parallel {
        stage('Dockerrize app') {
          steps {
            stash name: 'code', exclude '.git'
            sh 'build_script.sh'
          }
        }

        stage('Artifacts') {
          steps {
            archiveArtifacts 'app/'
          }
        }
      }
    }
    stage('Unit testing'){
      steps{
        unstash 'code'
        sh 'run_tests.sh'
      }
    }
    stage('DockerHub push') {
      when {
        anyOf{
          branch 'master'
          changeRequest()
        }
      }
      enviornment{
        DOCKERCREDS = credentials('docker_login')
      }
      steps {
        sh 'echo "Hello World"'
      }
    }

  }
}