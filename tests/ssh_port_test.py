import subprocess
import pytest

CONTAINER_NAME = "ansible-test"
EXPECTED_PORT = "4242"

def get_ssh_port_from_container(container_name: str) -> str:
    """
    Reads the SSH port from /etc/ssh/sshd_config inside the Docker container.
    """
    try:
        # Run `grep` inside the container
        result = subprocess.run(
            ["docker", "exec", container_name, "grep", "^Port", "/etc/ssh/sshd_config"],
            capture_output=True,
            text=True,
            check=True
        )
        # Example output: "Port 4242"
        line = result.stdout.strip()
        if not line:
            return None
        return line.split()[1]  # get the port number
    except subprocess.CalledProcessError:
        return None

def test_ssh_port():
    port = get_ssh_port_from_container(CONTAINER_NAME)
    assert port == EXPECTED_PORT, f"SSH port is {port}, expected {EXPECTED_PORT}"
