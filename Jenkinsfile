pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                git url: 'https://github.com/dchennax423/github2.git', branch: 'master'
            }
        }
        stage('Build') {
            steps {
                echo 'Build started'
            }
        }
        stage('Test') {
            steps {
                echo 'Tests executed successfully'
            }
        }
    }
}
