pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                git url: 'https://github.com/dchennax423/github2.git', branch: 'master'
            }
        }
        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt || true'
            }
        }
        stage('Run Tests') {
            steps {
                sh 'python -m unittest discover -s tests'
            }
        }
    }
    post {
        always {
            echo 'Build finished'
        }
    }
}
