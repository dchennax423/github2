pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                echo 'Stage: Checkout'
                git 'https://github.com/dchennax423/github2.git'
            }
        }

        stage('Setup Python venv') {
            steps {
                echo 'Stage: Setup Python venv'
                sh '''
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install --upgrade pip
                '''
            }
        }

        stage('Install Dependencies') {
            steps {
                echo 'Stage: Install Dependencies'
                sh '''
                    . venv/bin/activate
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                echo 'Stage: Run Tests (pytest)'
                sh '''
                    . venv/bin/activate
                    pytest -v
                   # python -m unittest discover -s tests
                '''
            }
        }
    }

    post {
        success {
            echo '✅ All Tests Passed'
        }
        failure {
            echo '❌ Some Tests Failed'
        }
    }
}
