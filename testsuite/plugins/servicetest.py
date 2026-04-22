import asyncio
import traceback
import pytest
OUTPUT_PREFIX = '[service-runner] '

class Hookspec:

    def pytest_servicetest_modifyitem(self, session, item):
        """Modify items for servicetest runner."""
        pass

class ServiceTestRunner:

    def __init__(self, config):
        self.config = config
        self.service_started = False

    @property
    def reporter(self):
        pass

    @pytest.hookimpl(trylast=True)
    def pytest_collection_modifyitems(self, session, items):
        pass

    def pytest_sessionstart(self, session):
        pass

    def pytest_runtestloop(self, session):
        pass

    @pytest.hookimpl(hookwrapper=True, tryfirst=True)
    def pytest_runtest_call(self, item):
        pass

def pytest_addoption(parser):
    pass

def pytest_configure(config):
    pass

def pytest_addhooks(pluginmanager):
    pass

def pytest_servicetest_modifyitem(session, item):
    pass

@pytest.fixture
async def _servicetest_endless_sleep(pytestconfig, _global_daemon_store):
    pass
