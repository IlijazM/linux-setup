from utils.expect import expect

def test_that_fastfetch_is_installed():
    expect("fastfetch").to_contain("Debian GNU")