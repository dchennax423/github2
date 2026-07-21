pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                git credentialsId: 'dchenna423',
                    url: 'https://github.com/dchennax423/github2.git'
            }
        }

        stage('Build') {
            steps {
                sh 'npm install'
            }
        }

        stage('Health Check') {
            steps {
                echo 'Running Server Health Check...'
                sh 'python3 health_check.py'
            }
        }

        stage('Test') {
            steps {
                sh 'npm test'
            }
        }

        stage('Deploy') {
            steps {
                sh '''
                  pm2 stop app || true
                  pm2 start index.js --name app
                '''
            }
        }
    }

    post {
        success {
            echo '✅ Build & Deploy Successful'
        }
        failure {
            echo '❌ Pipeline Failed'
        }
    }
}
