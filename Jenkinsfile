pipeline {
    agent any

    environment {
        // Remplacez 'KUBECONFIG_CRED_ID' par l'ID que vous donnerez dans Jenkins
        KUBECONFIG = credentials('my-kubeconfig-id')
    }

    stages {
        stage('Build Docker') {
            steps {
                // Utilisation de double quotes pour Jenkins/Groovy
                bat "docker build -t webapp:latest ."
            }
        }

        stage('Deploy Kubernetes') {
            steps {
                script {
                    // On force l'utilisation du fichier de config via la variable d'env
                    bat "kubectl --kubeconfig=${KUBECONFIG} apply -f deployment.yaml"
                    bat "kubectl --kubeconfig=${KUBECONFIG} apply -f service.yaml"
                }
            }
        }

        stage('Status') {
            steps {
                bat "kubectl --kubeconfig=${KUBECONFIG} get pods"
                bat "kubectl --kubeconfig=${KUBECONFIG} get svc webapp-service"
            }
        }
    }
    
    post {
        failure {
            echo "Le déploiement a échoué. Vérifiez la connexion au cluster."
        }
    }
}