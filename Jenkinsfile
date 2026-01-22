pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                echo 'Stage: Checkout'
                git url: 'https://github.com/dchennax423/github2.git', branch: 'master'
            }
        }

        stage('Setup Python Virtual Env') {
            steps {
                echo 'Stage: Setup Python venv'
                sh '''
                python3 -m venv venv
                . venv/bin/activate
                pip install --upgrade pip
                '''
            }
        }

        stage('Run Tests') {
            steps {
                echo 'Stage: Run Tests'
                sh '''
                . venv/bin/activate
                python3 -m unittest discover -s tests
                '''
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
