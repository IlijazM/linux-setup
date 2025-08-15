import subprocess

def check(cmd, expected):
    out = subprocess.check_output(cmd, shell=True, text=True)
    assert expected in out, f"Expected '{expected}' in output, got:\n{out}"

# Check SSH config
check("docker exec $(docker ps -q --filter ancestor=server-test) grep '^Port 4242' /etc/ssh/sshd_config", "Port 4242")

# Check user exists
check("docker exec $(docker ps -q --filter ancestor=server-test) id ich", "ich")
