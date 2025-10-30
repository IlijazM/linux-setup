from utils.expect import expect

def test_croc_installed_in_usr_local_bin():
    # Verify the croc binary exists and is executable in /usr/local/bin
    expect("test -x /usr/local/bin/croc").to_not_fail()

def test_croc_which_points_to_usr_local_bin():
    expect("which croc").to_contain("/usr/local/bin/croc")

def test_croc_version():
    expect("croc --version").to_contain("croc version").to_not_fail()