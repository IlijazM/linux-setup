#!/usr/bin/env bash
set -e

CID=""

cleanup() {
  echo "cleanup"
  podman stop $CID
  podman rm $CID
}
trap cleanup EXIT INT ERR

podman stop -i ansible-test

# Build test image
podman build -t ansible-test -f Dockerfile.test tests

# Start container in background
podman network create ansible-test-network || true
CID=$(podman run -d --rm --network ansible-test-network -p 4242:4242 -p 2222:22 -p 8080:80 -p 4430:443 --name ansible-test ansible-test)

# Wait for sshd
sleep 2

echo "docker container has the id $CID"

# Run Ansible
ansible-playbook \
  -i "localhost," \
  -e "ansible_port=2222 ansible_host=127.0.0.1 ansible_user=root ansible_ssh_common_args='-o StrictHostKeyChecking=no'" \
  -c ssh \
  ansible/playbook.yml

podman restart ansible-test

read -p "Press any key to continue..." -n 1 -s

# Tests
pytest tests
