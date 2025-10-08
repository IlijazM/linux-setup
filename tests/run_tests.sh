#!/usr/bin/env bash
set -e

CID=""

cleanup() {
  echo "cleanup"
  sudo podman stop $CID
  sudo podman rm $CID
}
trap cleanup EXIT INT ERR

sudo podman stop -i ansible-test

# Build test image
sudo podman build -t ansible-test -f Dockerfile.test tests

# Start container in background
sudo podman network create ansible-test-network || true
CID=$(sudo podman run -d --rm --network ansible-test-network -p 4242:4242 -p 2222:22 -p 8080:80 -p 4430:443 --name ansible-test ansible-test)

# Wait for sshd
sleep 2

echo "docker container has the id $CID"

# Run Ansible
ansible-playbook \
  -i "localhost," \
  -e "ansible_port=2222 ansible_host=127.0.0.1 ansible_user=root ansible_ssh_common_args='-o StrictHostKeyChecking=no'" \
  -c ssh \
  ansible/playbook.yml

sudo podman restart ansible-test

read -p "Press any key to continue..." -n 1 -s

# Tests
pytest tests
