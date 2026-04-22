import pytest
from testsuite import matching

def _default_regex_match(doc: dict):
    pass

def _default_partial_dict_match(doc: dict):
    pass

def _match_unordered_list(doc: dict):
    pass

def _match_list_of(doc):
    pass

def _match_dict_of(doc):
    pass

def pytest_register_matching_hooks():
    pass

class Hookspec:

    def pytest_register_matching_hooks(self):
        pass

class MatchingPlugin:

    def __init__(self):
        self._matching_hooks = {}

    @property
    def matching_hooks(self):
        pass

    def pytest_sessionstart(self, session):
        pass

    def pytest_addhooks(self, pluginmanager):
        pass

def pytest_configure(config):
    pass

@pytest.fixture(scope='session')
def operator_match(request, pytestconfig):
    pass

@pytest.fixture(scope='session')
def match_operator(operator_match):
    pass

def _make_keys_getter(keys):
    pass

def _make_key_getter(path):
    pass
