pipeline {
 agent any
 environment {
       docker_username = 'simonmdsn'
   }
 stages {
   stage('Python tests'){
        agent any
        environment {
            DOCKERCREDS = credentials('docker_login') //use the credentials just created in this stage
        }
        steps {
            unstash 'code' //unstash the repository code
            sh 'ci/build-docker.sh'
            stash excludes: '.git', name: 'code'
        }
   }
 }
}