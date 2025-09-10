import subprocess

CONTAINER_NAME = "ansible-test"

class ExpectCommand:
    def __init__(self, command: str, container: str = CONTAINER_NAME):
        self.command = command
        self.container = container
        self._result = None
        self._error = None
        self._run_command()

    def _run_command(self):
        print("Running command: " + " ".join(["docker", "exec", self.container] + self.command.split()))
        try:
            self._result = subprocess.run(
                ["sudo", "podman", "exec", self.container] + self.command.split(),
                capture_output=True,
                text=True,
                check=True
            )
            self._error = None
        except subprocess.CalledProcessError as e:
            self._result = e
            self._error = e

    def to_return(self, expected: str):
        """
        Assert that the command output equals the expected string.
        """
        output = self._result.stdout.strip() if self._result else ""
        assert output == expected, f"Expected '{expected}', but got '{output}'"
        return self

    def to_contain(self, expected: str, ignore_case = False):
        """
        Assert that the command output contains the expected string.
        """
        output = self._result.stdout.strip() if self._result else ""
        if ignore_case:
            output = output.lower()
            excepted = expected.lower()
        assert expected in output, f"Expected output to contain '{expected}', but got '{output}'"
        return self
    
    def to_not_contain(self, unexpected: str):
        """
        Assert that the command output does not contain the unexpected string.
        """
        output = self._result.stdout.strip() if self._result else ""
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

def expect(command: str, container: str = CONTAINER_NAME) -> ExpectCommand:
    """
    Main entry point for the utility.
    Usage: expect("grep '^Port' /etc/ssh/sshd_config").to_return("Port 4242").to_not_fail()
    """
    return ExpectCommand(command, container)
