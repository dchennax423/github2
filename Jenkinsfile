pipeline {
    agent any

    stages {

        stage('Clone Code') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/USERNAME/devops-demo-app.git',
                    credentialsId: 'github-creds'
            }
        }

        stage('Build') {
            steps {
                echo "Building application..."
                sh 'npm install'
            }
        }

        stage('Test') {
            steps {
                echo "Running tests..."
                sh 'npm test || true'
            }
        }

        stage('Deploy') {
            steps {
                echo "Deploying application..."
                sh 'pm2 restart app || pm2 start index.js --name app'
            }
        }
    }

    post {
        success {
            echo "✅ Build & Deploy Successful"
        }
        failure {
            echo "❌ Build Failed"
        }
    }
}
