from utils.expect import expect


def test_cargo_is_installed():
    # cargo should be on PATH
    expect("which cargo").to_contain("cargo")


def test_cargo_reports_version():
    # cargo --version prints version info
    expect("cargo --version").to_contain("cargo")
