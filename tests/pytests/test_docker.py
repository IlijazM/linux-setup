from utils.expect import expect, run

def test_docker_installed():
    expect("docker --version").to_contain("docker", ignore_case=True)

def test_docker_compose_working():
    expect("docker compose --version").to_contain("docker compose", ignore_case=True)

def ensure_docker_daemon_running():
    run("sudo systemctl start docker")

# Tests not working
# To fix setup docker-in-podman
#
# def test_docker_run_container():
#     ensure_docker_daemon_running()
#     expect("docker run --rm hello-world").to_contain("Hello from Docker")
#
# def test_docker_run_container_as_ich():
#     ensure_docker_daemon_running()
#     expect("docker run --rm hello-world", user="ich").to_contain("Hello from Docker")