#codebase please add, improve, and enhance the tests given this description:

# Test Coverage for Ansible Roles

Below is a summary of test coverage for each app/configuration managed by the Ansible scripts, along with suggestions for improvement.

## docker

- **Tested:** Yes (`tests/pytests/test_docker.py`)
- **Improvements:** Add tests for Docker Compose, user permissions, and container startup verification.

## eza

- **Tested:** Yes (`tests/pytests/test_eza.py`)
- **Improvements:** Check for correct alias setup and verify `eza` is the default for `ls`.

## fastfetch

- **Tested:** Yes (`tests/pytests/test_fastfetch.py`)
- **Improvements:** Validate output of the welcome script and integration with shell startup.

## nginx

- **Tested:** Yes (`tests/pytests/test_nginx.py`)
- **Improvements:** Add tests for SSL certificate deployment, custom config validation, and service reloads.

## node

- **Tested:** Yes (`tests/pytests/test_node.py`)
- **Improvements:** Test multiple Node.js versions, global npm package installs, and user-specific setups.

## setup

- **Tested:** Partially (`tests/pytests/test_ssh_port.py` and others)
- **Improvements:** Expand tests for user/group creation, directory structure, and SSH key management.

## zoxide

- **Tested:** No dedicated test found.
- **Improvements:** Add tests to verify installation, shell integration, and alias functionality.

## zsh

- **Tested:** Yes (`tests/pytests/test_zsh.py`)
- **Improvements:** Test plugin installation, and default shell assignment for all users.

---

**General Suggestions:**

- Add negative tests (e.g., removal/uninstallation).
- Use Molecule for role-level testing and scenario coverage.
- Validate configuration files' syntax and runtime behavior.

Consider how the tests are designed right now and use or expand the existing utilities in the pytests directory
