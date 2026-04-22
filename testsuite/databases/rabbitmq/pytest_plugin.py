import asyncio
import pytest
from . import classes, service

def pytest_addoption(parser):
    pass

def pytest_configure(config):
    pass

def pytest_service_register(register_service):
    pass

@pytest.fixture
def rabbitmq(_rabbitmq_connection) -> classes.Control:
    pass

@pytest.fixture(scope='session')
async def _rabbitmq_connection(_rabbitmq_service, _rabbitmq_service_settings) -> classes.Control:
    pass

@pytest.fixture(scope='session')
def rabbitmq_disabled(pytestconfig) -> bool:
    pass

@pytest.fixture(scope='session')
def _rabbitmq_service_settings() -> service.ServiceSettings:
    pass

@pytest.fixture(scope='session')
def _rabbitmq_service(ensure_service_started, rabbitmq_disabled, pytestconfig, _rabbitmq_service_settings):
    pass
