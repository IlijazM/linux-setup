import subprocess
import shlex

CONTAINER_NAME = "ansible-test"

class ExpectCommand:
    def __init__(self, command: str, container: str = CONTAINER_NAME, user: str = "root", interactive_shell: bool = False):
        self.command = command
        self.container = container
        self.user = user
        self.interactive_shell = interactive_shell
        (self._result, self._error) = run(self.command, container=self.container, user=self.user, interactive_shell=self.interactive_shell)

    def to_return(self, expected: str):
        """
        Assert that the command output equals the expected string.
        """
        output = self._result if self._result else ""
        assert output == expected, f"Expected '{expected}', but got '{output}'"
        return self

    def to_contain(self, expected: str, ignore_case = False):
        """
        Assert that the command output contains the expected string.
        """
        output = self._result if self._result else ""
        if ignore_case:
            output = output.lower()
            excepted = expected.lower()
        assert expected in output, f"Expected output to contain '{expected}', but got '{output}'"
        return self
    
    def to_not_contain(self, unexpected: str):
        """
        Assert that the command output does not contain the unexpected string.
        """
        output = self._result if self._result else ""
        assert unexpected not in output, f"Did not expect output to contain '{unexpected}', but got '{output}'"
        return self

    def to_not_fail(self):
        """
        Assert that the command ran successfully (exit code 0).
        """
        assert self._error is None, f"Command failed with error: {self._error}"
        return self

    def to_fail(self):
        """
        Assert that the command failed (non-zero exit code).
        """
        assert self._error is not None, "Command was expected to fail but succeeded"
        return self

def expect(command: str, container: str = CONTAINER_NAME, user = "root", interactive_shell = False) -> ExpectCommand:
    """
    Main entry point for the utility.
    Usage: expect("grep '^Port' /etc/ssh/sshd_config").to_return("Port 4242").to_not_fail()
    """
    return ExpectCommand(command, container, user, interactive_shell)

def run(command: str, container=CONTAINER_NAME, user="root", interactive_shell=False) -> tuple[str, str]:
    cmd = []

    if container is not None:
        cmd += ["sudo", "podman", "exec", "--user", user, container]

    if container is not None and interactive_shell:
        cmd += ["zsh", "-i", "-c", command]
    elif container is not None:
        cmd += ["zsh", "-c", command]
    else:
        cmd += shlex.split(command)

    print("Running command:", shlex.join(cmd))

    try:
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            check=True
        )
        return (result.stdout.strip(), None)
    except subprocess.CalledProcessError as e:
        return (e.stderr, e.stderr)