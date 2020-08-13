pipeline {   
  environment {
    docker_username = 'mathn16'
  }
  agent any
  stages {
    stage('Dockerrize app') {
      parallel {
        stage('Dockerrize app') {
          steps {
            stash name: 'code', excludes:'.git'
            sh './build_script.sh'
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
        sh './run_tests.sh'
      }
    }
    stage('DockerHub push') {
      environment{
        DOCKERCREDS = credentials('docker_login')
      }
      steps {
        sh 'echo "Hello World"'
      }
    }
  }
}