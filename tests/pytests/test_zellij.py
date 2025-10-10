from utils.expect import expect

def test_that_zellij_is_installed():
    expect("which zellij").to_contain("zellij")

def test_zellij_version_prints():
    expect("zellij --version").to_contain("zellij")
