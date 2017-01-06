from .compat import ConfigParser


__all__ = ['parsed_file', 'packages', 'Command', 'commands']


def parsed_file(config_file):
    """Parse an ini-style config file."""
    parser = ConfigParser(allow_no_value=True)
    parser.readfp(config_file)
    return parser


def packages(config):
    """Return the packages defined in the config file as tuple."""
    _assert_section(config, 'packages')
    return tuple(config.options('packages'))


class Command:
    """Command which can be executed."""

    def __init__(self, command, precondition=''):
        self.command = command
        self.precondition = precondition

    def __repr__(self):
        """Representation of this wrapper."""
        p = " if {0!r}".format(self.precondition) if self.precondition else ""
        return "<Command {0!r}{1}>".format(self.command, p)

    def __eq__(self, other):
        """Compare two command instances."""
        if not isinstance(other, Command):
            return False
        return (self.command == other.command and
                self.precondition == other.precondition)

    def __ne__(self, other):
        """Own __eq__ requires own __ne__."""
        return not self.__eq__(other)


def commands(config, names):
    """Return the list of commands to run."""
    commands = {cmd: Command(**dict(config.items(cmd)))
                for cmd in config.sections()
                if cmd != 'packages'}
    try:
        return tuple(commands[x] for x in names)
    except KeyError as e:
        raise RuntimeError(
            'Section [commands] in the config file does not contain the '
            'key {.args[0]!r} you requested to execute.'.format(e))


def _assert_section(config, name):
    """Make sure that a section exists in the config file."""
    if name not in config.sections():
        raise RuntimeError(
            'Missing the section [{}] in the config file.'.format(name))
