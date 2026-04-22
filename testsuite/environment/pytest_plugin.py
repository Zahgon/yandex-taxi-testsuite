import pathlib
import pytest
from . import control, utils

class Hookspec:

    def pytest_service_register(self, register_service):
        """Register testsuite environment service."""
        pass

class TestsuiteEnvironmentPlugin:
    _env: control.TestsuiteEnvironment | None

    def __init__(self):
        self._env = None

    def ensure_started(self, service_name, **kwargs):
        pass

    def pytest_sessionstart(self, session):
        pass

    def pytest_sessionfinish(self, session):
        pass

    def pytest_addhooks(self, pluginmanager):
        pass

    def pytest_report_header(self, config):
        pass

def pytest_addoption(parser):
    pass

def pytest_configure(config):
    pass

@pytest.fixture(scope='session')
def ensure_service_started(pytestconfig):
    pass
