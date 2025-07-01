pipeline {
  agent any

  environment {
    ANSIBLE_HOST_KEY_CHECKING = "False"
    PYTHONIOENCODING = "utf-8"
  }

  stages {
    stage('Exécuter le script Python (Windows)') {
      steps {
        bat '"C:\Users\karim\AppData\Local\Programs\Python\Python310\python.exe" dynamic_inventory.py > inventory.json'
      }
    }

    stage('Déploiement avec Ansible (WSL)') {
      steps {
        sh 'wsl ansible-playbook -i inventory.json install-apache.yml'
      }
    }
  }

  post {
    success {
      echo "✅ Déploiement terminé avec succès"
    }
    failure {
      echo "❌ Une erreur s’est produite"
    }
  }
}
