from .compat import ConfigParser


__all__ = ['parsed_file', 'packages', 'commands']


def parsed_file(config_file):
    """Parse an ini-style config file."""
    parser = ConfigParser(allow_no_value=True)
    parser.readfp(config_file)
    return parser


def packages(config):
    """Return the packages defined in the config file as tuple."""
    _assert_section(config, 'packages')
    return tuple(config.options('packages'))


def commands(config, names):
    """Return the list of commands to run."""
    _assert_section(config, 'commands')
    commands = dict(config.items('commands'))
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
