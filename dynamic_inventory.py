#!/usr/bin/env python3
import subprocess
import json

inventory = {
    "all": {"hosts": [], "vars": {"ansible_user": "root"}},
    "_meta": {"hostvars": {}}
}

# Liste les conteneurs Docker actifs
result = subprocess.run(["docker", "ps", "--format", "{{.Names}}"], capture_output=True, text=True)

for name in result.stdout.strip().splitlines():
    # Inspecter chaque conteneur
    inspect = subprocess.run(["docker", "inspect", name], capture_output=True, text=True)
    data = json.loads(inspect.stdout)[0]

    # Vérifier s’il expose le port 22
    ports = data["NetworkSettings"]["Ports"]
    if "22/tcp" in ports and ports["22/tcp"]:
        host_port = ports["22/tcp"][0]["HostPort"]
        inventory["all"]["hosts"].append(name)
        inventory["_meta"]["hostvars"][name] = {
            "ansible_host": "127.0.0.1",
            "ansible_port": int(host_port),
            "ansible_user": "root",
            "ansible_password": "root",  # ajoute le mot de passe SSH
            "ansible_connection": "ssh",
            "ansible_python_interpreter": "/usr/bin/python3"
        }

print(json.dumps(inventory, indent=2))
