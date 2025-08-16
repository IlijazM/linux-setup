#!/usr/bin/env bash
set -e

CID=""

cleanup() {
  echo "cleanup"
  docker stop $CID
  docker rm $CID
}
trap cleanup EXIT INT ERR

docker stop -i ansible-test

# Build test image
docker build -t ansible-test -f Dockerfile.test tests

# Start container in background
CID=$(docker run -d --rm -p 4242:4242 -p 2222:22 --name ansible-test ansible-test)

# Wait for sshd
sleep 2

echo "docker container has the id $CID"

# Run Ansible
ansible-playbook \
  -i "localhost," \
  -e "ansible_port=2222 ansible_host=127.0.0.1 ansible_user=root ansible_ssh_common_args='-o StrictHostKeyChecking=no'" \
  -c ssh \
  ansible/playbooks/main.yml

sleep 10000000000

# Run verification
# python3 tests/test_basic.py
