from __future__ import print_function
import os
import subprocess


class Runner:
    """Run the tests."""

    def __init__(self, command, packages):
        self.command = command
        self.packages = packages

    def __call__(self):
        for package in self.packages:
            if not self.test(self.command, package):
                self.render_failure()
                return False
        self.render_success()
        return True

    def test(self, cmd, package):
        print('Testing', package)
        cwd = os.getcwd()
        os.chdir(package)
        try:
            process = subprocess.Popen(cmd.split())
            return process.wait() == 0
        finally:
            os.chdir(cwd)

    def render_failure(self):
        print('FAILURE :-(')

    def render_success(self):
        print('SUCCESS :-)')
