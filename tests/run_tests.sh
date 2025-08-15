#!/usr/bin/env bash
set -e

CID=""

cleanup() {
    docker stop $CID
    docker rm $CID
}
trap cleanup EXIT INT ERR


# Build test image
docker build -t server-test -f tests/Dockerfile.test .

# Start container in background
CID=$(docker run -d -p 2222:22 server-test)

# Wait for sshd
sleep 2

# Run Ansible
ansible-playbook \
  -i "all, ansible_port=2222 ansible_host=127.0.0.1 ansible_user=root ansible_password=root ansible_ssh_common_args='-o StrictHostKeyChecking=no'" \
  ansible/playbooks/main.yml


# Run verification
python3 tests/test_basic.py
