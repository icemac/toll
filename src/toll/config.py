import configparser


class Configuration:
    """Configuration for the test runs."""

    commands = None  # dict of commands mapping type to command
    packages = None  # list of paths to packages to be tested

    def __init__(self, config_file):
        config = configparser.ConfigParser(allow_no_value=True)
        config.read_file(config_file)
        self.commands = self._extract_commands(config)
        self.packages = self._extract_packages(config)

    @classmethod
    def _extract_commands(cls, config):
        cls._assert_section(config, 'commands')
        commands = config['commands']
        if 'test' not in commands:
            raise RuntimeError(
                'Section [commands] in the config file does not contain the '
                'key "test" which is needed to define the test command.')
        return commands

    @classmethod
    def _extract_packages(cls, config):
        cls._assert_section(config, 'packages')
        return list(config['packages'].keys())

    @classmethod
    def _assert_section(cls, config, name):
        if name not in config.sections():
            raise RuntimeError(
                'Missing the section [{}] in the config file.'.format(name))
