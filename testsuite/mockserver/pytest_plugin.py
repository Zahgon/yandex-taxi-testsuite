import asyncio
import contextlib
import logging
import warnings
import pytest
from testsuite import types
from testsuite.tracing import TraceidManager
from testsuite.utils import net
from . import classes, exceptions, server
MOCKSERVER_DEFAULT_PORT = 9999
MOCKSERVER_SSL_DEFAULT_PORT = 9998
_SSL_KEY_FILE_INI_KEY = 'mockserver-ssl-key-file'
_SSL_CERT_FILE_INI_KEY = 'mockserver-ssl-cert-file'
MOCKSERVER_PORT_HELP = '\n{proto} mockserver port for default worker.\nRandom port is used by default. If testsuite is started with\n--service-wait or --service-disabled default is forced to {default}.\n'
logger = logging.getLogger(__name__)

def pytest_addoption(parser):
    pass

def pytest_configure(config):
    pass

def pytest_register_object_hooks():
    pass

@pytest.fixture(name='mockserver_strict_default')
def fixture_mockserver_strict_default():
    pass

@pytest.fixture(name='mockserver_create_session')
def fixture_mockserver_create_session(request, asyncexc_append, testsuite_traceid_manager: TraceidManager, mockserver_strict_default: bool):
    pass

@pytest.fixture(name='_mockserver_create_session')
def legacy_fixture_mockserver_create_session(mockserver_create_session):
    pass

@pytest.fixture
def mockserver(_mockserver: server.Server, mockserver_create_session) -> types.YieldFixture[server.MockserverFixture]:
    pass

@pytest.fixture
def mockserver_ssl(_mockserver_ssl: server.Server | None, mockserver_create_session) -> types.AsyncYieldFixture[server.MockserverSslFixture]:
    pass

@pytest.fixture(scope='session')
def mockserver_info(_mockserver_socket: classes.MockserverSocket) -> classes.MockserverInfo:
    """Returns mockserver information object."""
    pass

@pytest.fixture(scope='session')
def mockserver_ssl_info(_mockserver_ssl_socket: classes.MockserverSocket | None) -> classes.MockserverInfo | None:
    pass

@pytest.fixture(scope='session')
def mockserver_ssl_cert(pytestconfig) -> classes.SslCertInfo | None:
    pass

@pytest.fixture(scope='session')
async def mockserver_create(_mockserver_config):
    pass

@pytest.fixture(scope='session')
async def _mockserver(pytestconfig, _mockserver_socket: classes.MockserverSocket, _mockserver_config: classes.MockserverConfig) -> types.AsyncYieldFixture[server.Server]:
    pass

@pytest.fixture(scope='session')
async def _mockserver_ssl(pytestconfig, _mockserver_ssl_socket: classes.MockserverSocket, _mockserver_config: classes.MockserverConfig, mockserver_ssl_cert) -> types.AsyncYieldFixture[server.Server]:
    pass

@pytest.fixture(scope='session')
def _mockserver_hook(mockserver_info):
    pass

@pytest.fixture(scope='session')
def _mockserver_https_hook(mockserver_ssl_info):
    pass

@pytest.fixture(scope='session')
def _mockserver_socket(pytestconfig, _mockserver_config) -> classes.MockserverSocket:
    pass

@pytest.fixture(scope='session')
def _mockserver_ssl_socket(pytestconfig) -> classes.MockserverSocket | None:
    pass

@pytest.fixture(scope='session')
async def mockserver_set_debug(_mockserver, _mockserver_ssl):
    pass

@pytest.fixture(scope='session')
def _mockserver_config(pytestconfig) -> classes.MockserverConfig:
    pass

def _mockserver_info_hook(doc: dict, key=None, mockserver_info: classes.MockserverInfo | None=None):
    pass

def _mockserver_getport(config, option_port, default_port):
    pass
