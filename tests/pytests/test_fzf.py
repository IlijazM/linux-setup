from utils.expect import expect

def test_that_fzf_is_installed():
    # fzf provides a binary
    expect("which fzf").to_contain("fzf")
