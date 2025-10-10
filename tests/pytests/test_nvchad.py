from utils.expect import expect

def test_neovim_installed():
    expect("which nvim").to_contain("nvim")

def test_nvchad_config_cloned():
    # NVChad installs into dotfiles config path
    expect("ls -la /usr/local/etc/dotfiles/.config").to_contain("nvim")
