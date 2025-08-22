import paramiko
from socket import timeout

class SshSession:
    def __init__(self):
        self._connect()

    def _connect(self):
        self.client = paramiko.SSHClient()
        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        
        try:
            print(f"Connecting...")
            self.client.connect(hostname="localhost", username="ich", port=4242, timeout=5)
            print("Connection successful.")
        except timeout:
            print("Connection timed out after 20 seconds.")
        except paramiko.AuthenticationException:
            print("Authentication failed. Please check your credentials.")
        except Exception as e:
            print(f"An error occurred: {e}")
    
    def close(self):
        if 'client' in locals() and self.client.get_transport() and self.client.get_transport().is_active():
            print("Closing the connection.")
            self.client.close()

    def exec(self, cmd):
        _, stdout, stderr = self.client.exec_command(f"source ~/.zshrc >> /dev/null; {cmd}")

        output = stdout.read().decode('utf-8').strip()
        if output:
            return output
        
        return stderr.read().decode('utf-8').strip()
