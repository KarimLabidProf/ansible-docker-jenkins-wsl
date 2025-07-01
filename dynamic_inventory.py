#!/usr/bin/env python3
import json
import subprocess

result = subprocess.run(
    ['docker', 'ps', '--format', '{{.Names}} {{.ID}}'],
    stdout=subprocess.PIPE
)

containers = result.stdout.decode().strip().split('\n')

inventory = {
    "_meta": {
        "hostvars": {}
    },
    "all": {
        "hosts": [],
        "vars": {
            "ansible_user": "root",
            "ansible_connection": "ssh",
            "ansible_ssh_pass": "root"
        }
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
    inventory["all"]["hosts"].append(name)
    inventory["_meta"]["hostvars"][name] = {
        "ansible_host": ip
    }

print(json.dumps(inventory, indent=2))
