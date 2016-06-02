from .config import Configuration
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
    config = Configuration(args.file)
    runner = Runner(config.command, config.packages)
    return runner()
