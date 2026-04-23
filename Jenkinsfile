pipeline {
    agent any

    environment {
        // Cette ligne va extraire le chemin temporaire du fichier secret créé plus haut
        KUBECONFIG_FILE = credentials('my-kubeconfig-id')
    }

    stages {
        stage('Build Docker') {
            steps {
                bat "docker build -t webapp:latest ."
            }
        }

        stage('Deploy Kubernetes') {
            steps {
                // On passe le chemin du fichier config à kubectl via l'option --kubeconfig
                bat "kubectl --kubeconfig=\"%KUBECONFIG_FILE%\" apply -f deployment.yaml"
                bat "kubectl --kubeconfig=\"%KUBECONFIG_FILE%\" apply -f service.yaml"
            }
        }

        stage('Status') {
            steps {
                bat "kubectl --kubeconfig=\"%KUBECONFIG_FILE%\" get pods"
                bat "kubectl --kubeconfig=\"%KUBECONFIG_FILE%\" get svc webapp-service"
            }
        }
    }

    post {
        failure {
            echo "Le déploiement a échoué. Vérifiez l'ID du credential 'my-kubeconfig-id' dans Jenkins."
        }
    }
}