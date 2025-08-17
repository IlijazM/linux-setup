from utils.expect import expect

def test_that_zsh_is_installed():
    expect("which zsh").to_contain("zsh")

def test_that_zsh_files_exist():
    ls_results = expect("ls -la /usr/local/etc/dotfiles")
    
    ls_results.to_contain(".p10k.zsh")
    ls_results.to_contain(".zprofile")
    ls_results.to_contain(".zshrc")
    ls_results.to_contain(".zsh")

def test_that_all_repos_are_cloned():
    ls_results = expect("ls -la /usr/local/etc/dotfiles/.zsh")
    
    ls_results.to_contain("powerlevel10k")
    ls_results.to_contain("zsh-autosuggestions")
    ls_results.to_contain("zsh-syntax-highlighting")

def test_symlinks_for_root():
    ls_results = expect("ls -la /root")
    
    ls_results.to_contain(".p10k.zsh -> /usr/local/etc/dotfiles/.p10k.zsh")
    ls_results.to_contain(".zprofile -> /usr/local/etc/dotfiles/.zprofile")
    ls_results.to_contain(".zshrc -> /usr/local/etc/dotfiles/.zshrc")
    ls_results.to_contain(".zsh -> /usr/local/etc/dotfiles/.zsh")

def test_symlinks_for_ich():
    ls_results = expect("ls -la /home/ich")
    
    ls_results.to_contain(".p10k.zsh -> /usr/local/etc/dotfiles/.p10k.zsh")
    ls_results.to_contain(".zprofile -> /usr/local/etc/dotfiles/.zprofile")
    ls_results.to_contain(".zshrc -> /usr/local/etc/dotfiles/.zshrc")
    ls_results.to_contain(".zsh -> /usr/local/etc/dotfiles/.zsh")