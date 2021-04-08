pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                sh "sudo docker-compose build"    
            }
        }
        stage('Test') {
            steps {
                sh "echo 2" 
            }
        }
        stage('Deploy') {
            steps {
                sh "sudo docker-compose up -d" 
            }
        }
    }
}