import paramiko

class Pmiko:
    def __init__(self):
        pass

    def get_conn(self):
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(
            hostname="10.1.3.28",
            username="root",
            password="1qaz@WSX",
        )
        stdin, stdout, stderr = client.exec_command('fping -gu 10.1.3.0/24')
        for line in stdout:
            print(line.strip("\n"))
        client.close()


Pmiko().get_conn()
