from utils.expect import expect

def test_ssh_port():
    expect("grep ^Port /etc/ssh/sshd_config").to_contain("4242").to_not_contain("22")

def test_permit_root_login_disabled():
    expect("grep ^PermitRootLogin /etc/ssh/sshd_config").to_contain("PermitRootLogin no")

def test_authorized_keys_exists_for_root():
    expect(r"stat -c '%U %G %a' /root/.ssh/authorized_keys").to_contain("root")

def test_authorized_keys_exists_for_ich():
    expect(r"stat -c '%U %G %a' /home/ich/.ssh/authorized_keys").to_contain("ich")

def test_git_installed():
    expect("which git").to_contain("/git")

def test_curl_installed():
    expect("which curl").to_contain("/curl")

def test_dotfiles_directory_exists():
    expect(r"stat -c '%F' /usr/local/etc/dotfiles").to_contain("directory")