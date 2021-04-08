pipeline {
    agent any
    stages {
        stage("Build") {
            steps {
                sh "ls"
                sh "docker-compose build"    
            }
        }
        stage("Test") {
            steps {
                sh "echo 2" 
            }
        }
        stage("Push") {
            steps {
                sh "echo 3"
            }
        }
        stage("Ansible enviroment setup") {
            steps{
                sh "ansible-playbook -i ansible/inventory.yaml ansible/playbook.yaml"
            }
        }
        stage("Deploy") {
            steps {
                sh "docker-compose up -d" 
            }
        }
    }
}