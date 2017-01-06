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
                if not self.run(
                        command.command, command.precondition, package):
                    self.render_failure()
                    return False
        self.render_success()
        return True

    def run(self, cmd, precondition, package):
        cwd = os.getcwd()
        os.chdir(package)
        try:
            if self._precodition_is_met(precondition):
                print('Running', cmd, 'on', package)
                return self._run_cmd(cmd)
            else:
                print('Not running', cmd, 'on', package)
                print('Precondition', precondition, 'on', package, 'not met.')
                return True
        finally:
            os.chdir(cwd)

    def _precodition_is_met(self, precondition):
        if not precondition:
            return True
        if self._run_cmd(precondition):
            return True
        return False

    def _run_cmd(self, cmd):
        process = subprocess.Popen(cmd.split())
        return process.wait() == 0

    def render_failure(self):
        print('FAILURE :-(')

    def render_success(self):
        print('SUCCESS :-)')
