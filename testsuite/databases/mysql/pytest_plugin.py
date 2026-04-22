import collections
import pytest
from . import classes, control, service, utils

def pytest_addoption(parser):
    """
    :param parser: pytest's argument parser
    """
    pass

def pytest_configure(config):
    pass

def pytest_service_register(register_service):
    pass

@pytest.fixture
def mysql(_mysql, _mysql_apply) -> dict[str, control.ConnectionWrapper]:
    """MySQL fixture.

    Returns dictionary where key is database alias and value is
    :py:class:`control.ConnectionWrapper`
    """
    pass

@pytest.fixture(scope='session')
def mysql_disabled(pytestconfig) -> bool:
    pass

@pytest.fixture(scope='session')
def mysql_conninfo(pytestconfig, _mysql_service_settings):
    pass

@pytest.fixture(scope='session')
def mysql_local() -> classes.DatabasesDict:
    """Use to override databases configuration."""
    pass

@pytest.fixture
def _mysql(mysql_local, _mysql_service, _mysql_state):
    pass

@pytest.fixture
def _mysql_apply(mysql_local, _mysql_state, _mysql_query_loader, request):
    pass

@pytest.fixture
def _mysql_query_loader(get_file_path, get_directory_path):
    pass

@pytest.fixture(scope='session')
def _mysql_service_settings():
    pass

@pytest.fixture
def _mysql_service(ensure_service_started, mysql_local, mysql_disabled, pytestconfig, _mysql_service_settings):
    pass

@pytest.fixture(scope='session')
def _mysql_state(pytestconfig, mysql_conninfo):
    pass
