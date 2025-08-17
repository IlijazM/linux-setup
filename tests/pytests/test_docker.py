from utils.expect import expect

def test_docker_installed():
    expect("docker --version").to_contain("docker", ignore_case = True)

def test_docker_compose_working():
    expect("docker compose --version").to_contain("docker compose", ignore_case = True)