pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo 'Stage: Checkout'
                git url: 'https://github.com/dchennax423/github2.git', branch: 'master'
            }
        }

        stage('Install Dependencies') {
            steps {
                echo 'Stage: Install Dependencies'
                // Python dependencies install cheyyadam (requirements.txt optional)
                sh 'pip install -r requirements.txt || true'
            }
        }

        stage('Run Tests') {
            steps {
                echo 'Stage: Run Tests'
                // Python test cases run cheyyadam
                sh 'python -m unittest discover -s tests'
            }
        }
    }

    post {
        always {
            echo 'Build Finished'
        }
        success {
            echo '✅ All Tests Passed'
        }
        failure {
            echo '❌ Some Tests Failed'
        }
    }
}
