pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                sh "docker-compose build"    
            }
        }
        stage('Test') {
            steps {
                sh "echo 2" 
            }
        }
        stage('Deploy') {
            steps {
                sh "docker-compose up -d" 
            }
        }
    }
}