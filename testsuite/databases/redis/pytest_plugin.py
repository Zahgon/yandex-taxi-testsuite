import json
import pytest
import redis as redisdb
from . import service

def pytest_addoption(parser):
    pass

def pytest_configure(config):
    pass

def pytest_service_register(register_service):
    pass

@pytest.fixture(scope='session')
def redis_service(pytestconfig, ensure_service_started, _redis_service_settings):
    pass

@pytest.fixture(scope='session')
def redis_cluster_service(pytestconfig, ensure_service_started, _redis_cluster_service_settings):
    pass

@pytest.fixture(scope='session')
async def redis_standalone_service(pytestconfig, ensure_service_started, _redis_standalone_service_settings):
    pass

@pytest.fixture
def redis_store(pytestconfig, _redis_store, _redis_execute_commands_from_file):
    pass

@pytest.fixture
def redis_sentinel(pytestconfig, request, load_json, redis_service, redis_sentinels):
    pass

@pytest.fixture
def redis_cluster_store(pytestconfig, _redis_cluster_store, _redis_execute_commands_from_file):
    pass

@pytest.fixture(scope='session')
def _redis_masters(pytestconfig, _redis_service_settings):
    pass

@pytest.fixture(scope='session')
def redis_sentinels(pytestconfig, _redis_service_settings):
    pass

@pytest.fixture(scope='session')
def redis_cluster_nodes(_redis_cluster_service_settings):
    pass

@pytest.fixture(scope='session')
def redis_standalone_node(_redis_standalone_service_settings):
    pass

@pytest.fixture(scope='session')
def redis_cluster_replicas(_redis_cluster_service_settings):
    pass

@pytest.fixture(scope='session')
def _redis_service_settings():
    pass

@pytest.fixture(scope='session')
def _redis_cluster_service_settings():
    pass

@pytest.fixture(scope='session')
def _redis_standalone_service_settings():
    pass

def _json_object_hook(dct):
    pass

@pytest.fixture(scope='session')
def _redis_store(pytestconfig, redis_service, _redis_masters):
    pass

@pytest.fixture(scope='session')
def _redis_cluster_store(pytestconfig, redis_cluster_service, redis_cluster_nodes):
    pass

@pytest.fixture
def redis_standalone_store(pytestconfig, redis_standalone_service, redis_standalone_node, _redis_execute_commands_from_file):
    pass

@pytest.fixture
def _redis_execute_commands_from_file(request, load_json):
    pass
