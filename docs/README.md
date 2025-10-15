# Ansible Apps & Configurations

This project automates the setup of a Linux system using Ansible. Below is a list of all apps and configurations managed by the playbooks and roles in this repository.

## Apps & Roles

- **docker**: Installs Docker using the `geerlingguy.docker` role.
- **eza**: Installs the `eza` modern replacement for `ls`, sets up apt keyrings, GPG keys, and aliases.
- **fastfetch**: Installs `fastfetch` and copies a welcome script for shell integration.
- **nginx**: Installs and configures `nginx`, sets up SSL with `certbot`, manages default site and certificates.
- **node**: Installs Node.js for both `root` and `ich` users using NVM (via `morgangraphics.ansible-role-nvm`), ensures correct permissions.
- **setup**: Handles user creation (`root`, `ich`), group configuration, SSH setup, and directory structure.
- **zoxide**: (Role exists, but no main task file found. Likely manages `zoxide` shell tool.)
- **zsh**: Installs Zsh, sets it as the default shell for users, copies dotfiles (`.zshrc`, `.zprofile`, `.p10k.zsh`), and ensures plugin directories exist.

## External Roles

- **geerlingguy.docker**: Used for Docker installation and configuration.
- **morgangraphics.ansible-role-nvm**: Used for Node.js version management via NVM.

## Configuration Highlights

- **User & Group Management**: Automated creation and configuration of users and groups.
- **SSH Configuration**: Automated SSH setup for secure access.
- **Dotfiles**: Copies and manages shell configuration files for a consistent environment.
- **Aliases & Shell Scripts**: Installs helpful aliases and shell scripts for improved usability.

---

For more details, see the individual role directories in `ansible/roles/` and the main playbook in `ansible/playbook.yml`.
