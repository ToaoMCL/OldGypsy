pipeline {
    agent any
    environment {
        DB_URI = credentials("gcp-db-uri") 
        app_version = "v1.3.0"
    }
    stages {
        stage("Test") {
            steps {
                sh "bash jenkins-scripts/run_tests.sh"
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
                sh "bash jenkins-scripts/deploy.sh" 
            }
        }
    }
    post{
        always{
            junit "**/junit.xml"
            cobertura coberturaReportFile: "**/coverage.xml", failNoReports: false, failUnstable: false, onlyStable: false
        }
    }
}