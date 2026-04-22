import collections
import clickhouse_driver
import pytest
from . import classes, control, service, utils

def pytest_addoption(parser):
    pass

def pytest_configure(config):
    pass

def pytest_service_register(register_service):
    pass

@pytest.fixture
def clickhouse(_clickhouse, _clickhouse_apply) -> dict[str, clickhouse_driver.Client]:
    pass

@pytest.fixture
def _clickhouse(clickhouse_local, _clickhouse_service, _clickhouse_state):
    pass

@pytest.fixture
def _clickhouse_apply(clickhouse_local, _clickhouse_state, _clickhouse_query_loader, request):
    pass

@pytest.fixture
def _clickhouse_query_loader(get_file_path, get_directory_path):
    pass

@pytest.fixture(scope='session')
def clickhouse_disabled(pytestconfig) -> bool:
    pass

@pytest.fixture(scope='session')
def clickhouse_local() -> classes.DatabasesDict:
    """Use to override databases configuration."""
    pass

@pytest.fixture(scope='session')
def _clickhouse_service_settings() -> service.ServiceSettings:
    pass

@pytest.fixture(scope='session')
def clickhouse_conn_info(_clickhouse_service_settings):
    pass

@pytest.fixture
def _clickhouse_service(ensure_service_started, clickhouse_local, clickhouse_disabled, pytestconfig, _clickhouse_service_settings):
    pass

@pytest.fixture(scope='session')
def _clickhouse_state(pytestconfig, clickhouse_conn_info):
    pass
