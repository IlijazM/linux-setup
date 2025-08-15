# Use Debian base image
FROM debian:latest

# Install required packages and Ansible
RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y \
      ansible sudo openssh-client openssh-server && \
    rm -rf /var/lib/apt/lists/*

COPY setup.yml /server_setup_playbook.yml
COPY inventory.ini /inventory.ini

WORKDIR /

# Default command keeps the container alive
CMD ["/usr/sbin/sshd", "-D"]