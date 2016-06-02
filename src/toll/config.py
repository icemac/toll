from .compat import ConfigParser


class Configuration:
    """Configuration for the test runs."""

    command = None  # command to run
    packages = None  # list of paths to packages to be tested

    def __init__(self, config_file):
        config = ConfigParser(allow_no_value=True)
        config.readfp(config_file)
        self.command = self._extract_command(config)
        self.packages = self._extract_packages(config)

    @classmethod
    def _extract_command(cls, config):
        cls._assert_section(config, 'commands')
        commands = dict(config.items('commands'))
        if 'test' not in commands:
            raise RuntimeError(
                'Section [commands] in the config file does not contain the '
                'key "test" which is needed to define the test command.')
        return commands['test']

    @classmethod
    def _extract_packages(cls, config):
        cls._assert_section(config, 'packages')
        return config.options('packages')

    @classmethod
    def _assert_section(cls, config, name):
        if name not in config.sections():
            raise RuntimeError(
                'Missing the section [{}] in the config file.'.format(name))
