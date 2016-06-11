from . import config
from .run import Runner
import argparse


def main(raw_args=None):
    """Console script entry point."""
    parser = argparse.ArgumentParser(
        description="poor man's integration testing")
    parser.add_argument(
        '-c', '--config', dest='file', type=argparse.FileType('r'),
        default='toll.ini',
        help='ini-style file to read the configuration from')

    args = parser.parse_args(raw_args)
    config_file = config.parsed_file(args.file)
    command = config.commands(config_file, ['test'])[0]
    packages = config.packages(config_file)
    runner = Runner(command, packages)
    return runner()
