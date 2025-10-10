from utils.expect import expect

def test_that_zoxide_is_available():
    # zoxide provides zoxide binary
    expect("which zoxide").to_contain("zoxide")

def test_zoxide_setup_script_present():
    expect("ls -la /usr/local/etc/sh").to_contain("20_setup_zoxide")
