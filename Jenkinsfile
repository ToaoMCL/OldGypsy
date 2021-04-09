pipeline {
    agent any
    stages {
        stage("Test Front End") {
            steps {
                sh "sudo apt-get update"
                sh "sudo apt-get install python3-pip"
                sh "pip3 install -r s1-front-end/requirements.txt"
                sh "cd s1-front-end"
                sh "pytest" 
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
                sh "docker-compose push"
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
                sh "ls"
                sh "pwd"
                sh "bash jenkins-scripts/deploy.sh" 
            }
        }
    }
}