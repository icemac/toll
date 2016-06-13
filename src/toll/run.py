from __future__ import print_function
import os
import subprocess


class Runner:
    """Run the tests."""

    def __init__(self, commands, packages):
        self.commands = commands
        self.packages = packages

    def __call__(self):
        for command in self.commands:
            for package in self.packages:
                if not self.run(command, package):
                    self.render_failure()
                    return False
        self.render_success()
        return True

    def run(self, cmd, package):
        print('Running', cmd, 'on', package)
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
