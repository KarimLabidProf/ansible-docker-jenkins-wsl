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
                    def winPath = pwd()
                    def wslPath = winPath.replaceAll('\\\\', '/')
                                         .replaceFirst('([a-zA-Z]):', '/mnt/$1')
                                         .toLowerCase()

                    echo "WSL path: ${wslPath}"

                    // Rendre le script exécutable
                    bat "wsl chmod +x ${wslPath}/dynamic_inventory.py"

                    // Exécuter le playbook via WSL
                    def command = "wsl ansible-playbook ${wslPath}/install-apache.yml -i ${wslPath}/dynamic_inventory.py"

                    echo "Exécution de la commande : ${command}"
                    def result = bat(script: command, returnStatus: true)

                    if (result != 0) {
                        error "Le playbook Ansible a échoué avec le code ${result}"
                    }
                }
            }
        }
    }
}
