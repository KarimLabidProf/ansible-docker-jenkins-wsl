pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Run Ansible playbook with dynamic inventory') {
            steps {
                script {
                    // Récupérer chemin absolu du workspace (chemin Windows)
                    def repoPath = pwd()
                    // Conversion du chemin Windows vers chemin WSL (/mnt/c/...)
                    def wslPath = repoPath.replaceAll('\\\\', '/').replaceFirst('([a-zA-Z]):', '/mnt/$1').toLowerCase()

                    // Construire la commande ansible-playbook
                    def ansibleCmd = "wsl ansible-playbook ${wslPath}/install_apache.yml -i ${wslPath}/dynamic_inventory.py"

                    echo "Exécution de la commande : ${ansibleCmd}"

                    // Donner les droits d’exécution au script (important)
                    sh "wsl chmod +x ${wslPath}/dynamic_inventory.py"

                    // Exécuter le playbook, récupérer le code retour
                    def status = sh(script: ansibleCmd, returnStatus: true)

                    if (status != 0) {
                        error "Le playbook Ansible a échoué avec le code ${status}"
                    }
                }
            }
        }
    }
}
