#!/usr/bin/env python3
import json
import subprocess

result = subprocess.run(
    ['docker', 'ps', '--format', '{{.Names}} {{.ID}}'],
    stdout=subprocess.PIPE
)

containers = result.stdout.decode().strip().split('\n')

inventory = {
    "all": {
        "hosts": {}
    }
}

for line in containers:
    if not line:
        continue
    name, cid = line.split()
    ip_result = subprocess.run(
        ['docker', 'inspect', '-f', '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}', name],
        stdout=subprocess.PIPE
    )
    ip = ip_result.stdout.decode().strip()
    inventory["all"]["hosts"][name] = {
        "ansible_host": ip,
        "ansible_user": "root",
        "ansible_connection": "ssh",
        "ansible_ssh_pass": "root"
    }

with open("inventory.json", "w") as f:
    json.dump(inventory, f, indent=2)
