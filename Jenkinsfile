pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Setup venv') {
            steps {
                sh '''
                python3 -m venv venv
                . venv/bin/activate
                pip install -r requirements.txt
                '''
            }
        }

        stage('Run Fast Tests') {
            steps {
                sh '''
                . venv/bin/activate
                pytest -v -m "not slow"
                '''
            }
        }
    }

    post {
        success {
            echo "✅ FAST TESTS PASSED"
        }
        failure {
            echo "❌ FAST TESTS FAILED"
        }
    }
}
