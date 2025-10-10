from utils.expect import expect


def test_that_nvm_directory_exist_for_root():
    expect("ls -la /root").to_contain(".nvm")

def test_that_nvm_directory_exist_for_user_ich():
    expect("ls -la /home/ich").to_contain(".nvm")

def test_that_nvm_is_installed_for_root():
    expect("nvm", interactive_shell=True).to_contain("Node Version Manager")

def test_that_node_is_installed_for_root():
    expect("node --version", interactive_shell=True).to_contain("v")

def test_that_nvm_is_installed_for_user_ich():
    expect("zsh -i -c nvm", user="ich", interactive_shell=True).to_contain("Node Version Manager")

def test_that_node_is_installed_for_user_ich():
    expect("node --version", user="ich", interactive_shell=True).to_contain("v")

