pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // Récupérer le repo git
                checkout scm
            }
        }

        stage('Prepare inventory script') {
            steps {
                // S'assurer que le script dynamic_inventory.py a les bons droits dans WSL
                bat """
                wsl chmod +x /mnt/c/ProgramData/Jenkins/.jenkins/workspace/${env.JOB_NAME}/dynamic_inventory.py
                """
            }
        }

        stage('Run Ansible Playbook') {
            steps {
                // Lancer le playbook via WSL
                bat """
                wsl ansible-playbook /mnt/c/ProgramData/Jenkins/.jenkins/workspace/${env.JOB_NAME}/install-apache.yml -i /mnt/c/ProgramData/Jenkins/.jenkins/workspace/${env.JOB_NAME}/dynamic_inventory.py
                """
            }
        }
    }

    post {
        success {
            echo 'Playbook exécuté avec succès !'
        }
        failure {
            echo 'Erreur lors de l’exécution du playbook.'
        }
    }
}
