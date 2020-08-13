pipeline {   
   environment {
    docker_username = 'mathn16'
  }
  agent {label 'master-label'}
  stages {
    stage('Dockerrize app') {
      parallel {
        stage('Dockerrize app') {
          steps {
            sh './build_script.sh'
            stash name: 'code', excludes:'.git'
          }
        }

        stage('Artifacts') {
          steps {
            skipDefaultCheckout(true)
            sh './build_zip.sh'
            archiveArtifacts artifacts: 'ca-build.zip'
          }
        }
      }
    }
    stage('Unit testing'){
      agent {
        label 'test'
      }
      steps{
        sh './run_tests.sh'
        unstash 'code'
      }
    }
    stage('DockerHub push') {
      environment{
        DOCKERCREDS = credentials('docker_login')
      }
      when {
        anyOf{
          branch 'master';
          changeRequest()
        }
      }
      steps {
        skipDefaultCheckout(true) 
        unstash 'code'
        sh 'echo "$DOCKERCREDS_PSW" | docker login -u "$DOCKERCREDS_USR" --password-stdin'
        sh './push_to_hub.sh'
      }
    }
  }
}
