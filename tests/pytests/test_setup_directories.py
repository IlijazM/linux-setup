from utils.expect import expect


def test_dotfiles_directory_exists_and_perms():
    # Verify directory exists
    expect("test -d /usr/local/etc/dotfiles").to_not_fail()

    # Verify owner and group
    expect("stat -c '%U %G' /usr/local/etc/dotfiles").to_return("root sysconf")

    # Verify permissions (mode)
    # stat prints numeric mode like 0774 or 774; strip leading 0
    expect("stat -c '%a' /usr/local/etc/dotfiles").to_return("774")


def test_shell_files_directory_exists_and_perms():
    expect("test -d /usr/local/etc/sh").to_not_fail()
    expect("stat -c '%U %G' /usr/local/etc/sh").to_return("root sysconf")
    expect("stat -c '%a' /usr/local/etc/sh").to_return("774")


def test_bin_files_directory_exists_and_perms():
    expect("test -d /usr/local/bin").to_not_fail()
    expect("stat -c '%U %G' /usr/local/bin").to_return("root sysconf")
    expect("stat -c '%a' /usr/local/bin").to_return("774")


def test_srv_root_exists_and_perms():
    expect("test -d /srv").to_not_fail()
    expect("stat -c '%U %G' /srv").to_return("root sysconf")
    # /srv expected to be world-writable in the playbook (777)
    expect("stat -c '%a' /srv").to_return("777")
