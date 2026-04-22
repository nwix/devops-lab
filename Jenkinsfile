pipeline { 
    agent any 
    stages {
        stage('Clone') { 
            steps {
                // Remplacez USER par votre nom GitHub 
                git 'https://github.com/nwix/devops-lab.git' 
            }
        }
        stage ('Build Docker') { 
            steps {
                bat 'docker build -t webapp:latest .' 
            }
        }
        stage('Deploy Kubernetes') { 
            steps {
                bat 'kubectl apply -f deployment.yaml' 
                bat 'kubectl apply -f service.yaml' 
            }
        }
    }
}