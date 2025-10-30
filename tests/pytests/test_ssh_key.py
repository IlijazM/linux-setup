from utils.expect import expect

def test_that_ssh_key_exists_for_user_ich():
    expect("ls -a /home/ich/.ssh").to_contain("id_ecdsa").to_contain("id_ecdsa.pub")

def test_that_ssh_key_exists_for_root():
    expect("ls -a /root/.ssh").to_contain("id_ecdsa").to_contain("id_ecdsa.pub")
