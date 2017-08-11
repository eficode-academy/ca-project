node {
    stage ('Preparation'){
        checkout scm
    }
    stage('DockerImageBuild'){
        sh 'docker build -t codechan .'
    }
    stage('Python test'){
	sh 'docker run -i --rm codechan python tests.py'
    }
}
