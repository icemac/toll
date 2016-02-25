import os
import subprocess


class Runner:
    """Run the tests."""

    def __init__(self, config):
        self.config = config

    def __call__(self):
        cwd = os.getcwd()
        try:
            return self.test(
                self.config.commands['test'], self.config.packages)
        finally:
            os.chdir(cwd)

    def test(self, cmd, packages):
        for package in packages:
            print('Testing', package)
            os.chdir(package)
            status, output = subprocess.getstatusoutput(cmd)
            print(output)
            if status != 0:
                self.render_failure()
                return False
        self.render_success()
        return True

    def render_failure(self):
        print('FAILURE :-(')

    def render_success(self):
        print('SUCCESS :-)')
