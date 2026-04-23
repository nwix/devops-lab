pipeline {
    agent any

    stages {
        stage('Build Docker') {
            steps {
                bat 'docker build -t webapp:latest .'
            }
        }

        stage('Deploy Kubernetes') {
            steps {
                // FORCE l'ajout de --validate=false
                bat 'kubectl apply -f deployment.yaml --validate=false'
                bat 'kubectl apply -f service.yaml --validate=false'
            }
        }

        stage('Status') {
            steps {
                bat 'kubectl get pods'
                bat 'kubectl get svc webapp-service'
            }
        }
    }
}