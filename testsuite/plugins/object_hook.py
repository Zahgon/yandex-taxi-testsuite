import pytest

class Hookspec:

    def pytest_register_object_hooks(self):
        pass

class ObjectHooksPlugin:

    def __init__(self):
        self._object_hooks = {}

    @property
    def object_hooks(self):
        pass

    def pytest_sessionstart(self, session):
        pass

    def pytest_addhooks(self, pluginmanager):
        pass

def pytest_configure(config):
    pass

@pytest.fixture(scope='session')
def _base_object_hook(request, pytestconfig, match_operator):
    pass

@pytest.fixture
def object_hook(request, _base_object_hook):
    pass
