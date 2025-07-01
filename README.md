# Ansible + Docker + Jenkins (WSL)

## 🔧 Prérequis

- Jenkins installé sur Windows
- Python installé sur Windows
- Ansible installé dans WSL
- Docker Desktop fonctionnel
- Conteneurs Docker SSH-ready (mot de passe root = "root")

## 🚀 Utilisation

1. Cloner ce dépôt dans Jenkins
2. Créer un job pipeline avec ce `Jenkinsfile`
3. Lancer le pipeline

## 🛠️ Test manuel

```bash
python dynamic_inventory.py > inventory.json
wsl ansible-playbook -i inventory.json install-apache.yml
```

---
