pipeline {
 agent any
 environment {
       docker_username = 'simonmdsn'
   }
 stages {
stage('Clone down') {
    steps {
        stash excludes: '.git', name: 'code'
    }
}
   stage('Build docker image'){
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
   stage('Run python tests') {
       agent {
           docker {
               image: 'python:3'
           }
       } 
        steps {
            unstash 'code'
            sh 'ci/python-test.sh'
            stash excludes: '.git', name: 'code' //Is this step optionally
        } 
       
   }
 }
}