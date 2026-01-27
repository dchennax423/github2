pipeline {
    agent any

    stages {

        stage('Checkout Code') {
            steps {
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

        stage('Run Unit Tests') {
            steps {
                sh '''
                . venv/bin/activate
                pytest -v -m "not slow"
                '''
            }
        }

        stage('Run Long Tests (Nightly)') {
            when {
                expression { env.BUILD_CAUSE == 'TIMERTRIGGER' }
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
