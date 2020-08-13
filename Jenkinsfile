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
   stage('Run python tests') {
       agent {
           docker {
               image 'python:3'
           }
       } 
        steps {
            skipDefaultCheckout(true)
            unstash 'code'
            sh 'ci/python-test.sh'
            stash excludes: '.git', name: 'code' //Is this step optionally
        }    
   }
   stage('Parallel') {
       parallel{
           stage('Create artifacts') {
               steps {
            skipDefaultCheckout(true)
                   sh '''mkdir ./artifacts
                        tar -zcvf ./artifacts/flaskproject.tar.gz .'''
                    archiveArtifacts artifacts: 'artifacts/'
               }
           }
            stage('Build docker image'){
        agent any
        environment {
            DOCKERCREDS = credentials('docker_login') //use the credentials just created in this stage
        }
        steps {
            skipDefaultCheckout(true)
            unstash 'code' //unstash the repository code
            sh 'ci/build-docker.sh'
            stash excludes: '.git', name: 'code'
        }
   }

   }
   }
   
   stage('Push docker image') {
       agent any
       when {
           branch 'master'
       }
       environment {
           DOCKERCREDS = credentials('docker_login')
       }
       steps {
            skipDefaultCheckout(true)
        unstash 'code' //unstash the repository code
        sh 'echo "$DOCKERCREDS_PSW" | docker login -u "$DOCKERCREDS_USR" --password-stdin' //login to docker hub with the credentials above
        sh 'ci/push-docker.sh'
        stash excludes: '.git', name: 'code'
     }
   }
   stage('Deploy to production') {
       agent any
       when {
           branch 'master'
       }
       steps {
            skipDefaultCheckout(true)
            unstash 'code'
            sshagent (credentials: ['ubuntu']) {
                //sh 'scp -o StrictHostKeyChecking=no ./docker-compose.yml ubuntu@34.78.185.127:./docker-compose.yml'
                sh 'ssh -o StrictHostKeyChecking=no ubuntu@34.78.185.127 cd ca-project && git pull && docker-compose down && sleep 5 && docker-compose up'
            }

       }
   }

   stage('Deploy to test') {
       agent any 
       when {
         not {
           branch 'master'
           }
       }
       steps {
            skipDefaultCheckout(true)
            unstash 'code'
           sh 'echo hello test1'
       }
   }

 }
}