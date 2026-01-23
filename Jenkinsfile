pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                echo '📥 Checkout Code'
                git 'https://github.com/dchennax423/github2.git'
            }
        }

        stage('Setup Python venv') {
            steps {
                sh '''
                python3 -m venv venv
                . venv/bin/activate
                pip install --upgrade pip
                '''
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                . venv/bin/activate
                pip install -r requirements.txt
                '''
            }
        }

        stage('Unit Tests') {
            steps {
                sh '''
                . venv/bin/activate
                pytest -v -m "not slow"
                '''
            }
        }

        stage('Long Running Tests') {
            options {
                timeout(time: 40, unit: 'SECONDS')
            }
            steps {
                sh '''
                . venv/bin/activate
                pytest -v -m slow
                '''
            }
        }
    }

    post {
        success {
            echo '✅ BUILD SUCCESS'
        }
        failure {
            echo '❌ BUILD FAILED'
        }
    }
}
