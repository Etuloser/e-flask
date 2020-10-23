import subprocess


class Command:
    def __init__(self):
        pass

    def get_status_output(self, cmd):
        return subprocess.getstatusoutput(cmd)
