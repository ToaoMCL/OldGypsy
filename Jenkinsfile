pipeline {
    agent any
    stages {
        stage("Test") {
            steps {
                sh "echo 2" 
            }
        }
        stage("Build") {
            steps {
                sh "ls"
                sh "docker-compose build"    
            }
        }       
        stage("Push") {
            steps {
                sh "echo 3"
            }
        }
        stage("Ansible enviroment setup") {
            steps{
                sh "/home/jenkins/.local/bin/ansible --version"
                sh "/home/jenkins/.local/bin/ansible-playbook -i ansible/inventory.yaml ansible/playbook.yaml"
            }
        }
        stage("Deploy") {
            steps {
                sh "docker-compose up -d" 
            }
        }
    }
}