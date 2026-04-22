import argparse
import contextlib
import importlib
import logging
import pathlib
import subprocess
import sys
from testsuite.utils import colors
from . import control, shell, utils
DEFAULT_SERVICE_PLUGINS = ['testsuite.databases.mongo.pytest_plugin', 'testsuite.databases.pgsql.pytest_plugin', 'testsuite.databases.redis.pytest_plugin', 'testsuite.databases.mysql.pytest_plugin', 'testsuite.databases.clickhouse.pytest_plugin', 'testsuite.databases.rabbitmq.pytest_plugin', 'testsuite.databases.kafka.pytest_plugin']
logger = logging.getLogger(__name__)

class ColoredLevelFormatter(logging.Formatter):
    LEVEL_COLORS = {logging.DEBUG: colors.Colors.GRAY, logging.INFO: colors.Colors.BRIGHT_GREEN, logging.WARNING: colors.Colors.YELLOW, logging.ERROR: colors.Colors.RED, logging.CRITICAL: colors.Colors.BRIGHT_RED}

    def __init__(self, *, colors_enabled=False):
        super().__init__()
        self._colors_enabled = colors_enabled

    def format(self, record: logging.LogRecord):
        pass

def csv_arg(value: str):
    pass

def main(args=None, service_plugins=None):
    pass

def _setup_logging(log_level):
    pass

def _command_start(env, args):
    pass

def _command_stop(env, args):
    pass

def _command_run(env, args):
    pass

def _register_services(service_plugins=None):
    pass
if __name__ == '__main__':
    main()
