from utils.expect import expect

def test_that_www_fails():
    expect("waw").to_fail()


def test_that_nvm_directory_exist_for_root():
    expect("ls -la /root").to_contain(".nvm")

def test_that_nvm_directory_exist_for_user_ich():
    expect("ls -la /home/ich").to_contain(".nvm")

# def test_that_nvm_is_installed_for_root():
#     expect("nvm").to_not_fail()

# def test_that_nvm_is_installed_for_user_ich():
#     expect("sudo -u ich nvm").to_not_fail()

# def test_that_node_is_installed_for_root():
#     expect("node --version").to_not_fail()

# def test_that_node_is_installed_for_user_ich():
#     expect("sudo -u ich node --version").to_not_fail()
