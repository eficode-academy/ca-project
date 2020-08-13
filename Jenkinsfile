pipeline {
  agent any
  stages {
    stage('Dockerrize app') {
      parallel {
        stage('Dockerrize app') {
          steps {
            sh 'docker build -t ca-project'
          }
        }

        stage('Artifacts') {
          steps {
            archiveArtifacts 'app/build/libs'
          }
        }

      }
    }

    stage('DockerHub push') {
      steps {
        sh 'echo "Hello World"'
      }
    }

  }
}