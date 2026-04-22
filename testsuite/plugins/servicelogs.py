import asyncio
import io
import logging
import pathlib
import pytest
from testsuite._internal import logreader
logger = logging.getLogger(__name__)

class LogFileReporter(logreader.LogFile):

    def __init__(self, path: pathlib.Path, *, formatter_factory):
        super().__init__(path)
        self._formatter_factory = formatter_factory

    def make_report(self):
        pass

class ServiceLogsPlugin:
    _live_logs = None

    def __init__(self, *, config):
        self._config = config
        self._logs = {}
        self._flushers = []

    def pytest_sessionstart(self, session):
        pass

    def pytest_sessionfinish(self, session):
        pass

    def pytest_runtest_setup(self, item):
        pass

    @pytest.hookimpl(wrapper=True, tryfirst=True)
    def pytest_runtest_makereport(self, item, call):
        pass

    def register_flusher(self, func):
        pass

    def register_logfile(self, path: pathlib.Path, title: str, formatter_factory):
        pass

    def update_position(self):
        pass

    def _userver_report_attach(self, report):
        pass

    def _userver_report_attach_log(self, logfile, report, title):
        pass

    def _run_flushers(self):
        pass

def pytest_addoption(parser) -> None:
    pass

def pytest_configure(config):
    pass

@pytest.fixture(scope='session')
def servicelogs_register_logfile(_servicelogs_logging_plugin):
    pass

@pytest.fixture
def servicelogs_register_flusher(_servicelogs_logging_plugin: ServiceLogsPlugin):
    pass

@pytest.fixture(scope='session')
def service_logs_update_position(_servicelogs_logging_plugin: ServiceLogsPlugin):
    pass

@pytest.fixture(scope='session')
def _servicelogs_logging_plugin(pytestconfig) -> ServiceLogsPlugin:
    pass

def _live_logs_enabled(config):
    pass
