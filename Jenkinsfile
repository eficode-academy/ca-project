node {
    stage ('Preparation'){
        git credentialsId: '982cea69-7c7b-430c-bc1e-36926dc38c8d', url: 'https://github.com/Knut-Aage-Hofseth/ca-project.git'
    }
    stage('DockerImageBuild'){
        sh 'docker build -t codechan .'
    }
    stage('Python test'){
        sh 'docker run -i --rm codechan pip install -r requirements.txt && python tests.py '
    }
}
