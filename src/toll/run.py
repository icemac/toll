from __future__ import print_function

from .compat import get_terminal_size
from colorama import Fore, Style
import os
import subprocess


GREEN = Fore.GREEN + Style.BRIGHT
YELLOW = Fore.YELLOW + Style.BRIGHT
RED = Fore.RED + Style.BRIGHT


class Runner:
    """Run the tests."""

    def __init__(self, commands, packages):
        self.commands = commands
        self.packages = packages

    def __call__(self):
        for command in self.commands:
            for package in self.packages:
                if not self.run(
                        command.command, command.precondition,
                        command.ignore_exit_code, package):
                    self.render_failure()
                    return False
        self.render_success()
        return True

    def run(self, cmd, precondition, ignore_exit_code, package):
        cwd = os.getcwd()
        os.chdir(package)
        try:
            if self._precodition_is_met(precondition):
                self._draw_line('*', Fore.GREEN)
                print(GREEN + 'Running', cmd, GREEN + 'on', package)
                result = self._run_cmd(cmd)
                if ignore_exit_code:
                    return True
                else:
                    return result
            else:
                self._draw_line('#', Fore.YELLOW)
                print(YELLOW + 'Not running', cmd, YELLOW + 'on', package)
                print(YELLOW + 'Precondition', precondition, YELLOW + 'on',
                      package, YELLOW + 'not met.')
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

    def _draw_line(self, char, colour):
        length = get_terminal_size().columns
        print(colour + char * length)

    def render_failure(self):
        print(RED + 'FAILURE :-(')

    def render_success(self):
        print(GREEN + 'SUCCESS :-)')
