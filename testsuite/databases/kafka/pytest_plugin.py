import contextlib
import typing
import pytest
from . import classes, service

def pytest_addoption(parser):
    pass

def pytest_configure(config):
    pass

def pytest_service_register(register_service):
    pass

@pytest.fixture(scope='session')
async def _kafka_global_producer(_kafka_service, _bootstrap_servers) -> typing.AsyncGenerator[classes.KafkaProducer, None]:
    pass

@pytest.fixture
async def kafka_producer(_kafka_global_producer) -> typing.AsyncGenerator[classes.KafkaProducer, None]:
    """
    Per test Kafka producer instance.

    :returns: :py:class:`testsuite.databases.kafka.classes.KafkaProducer`
    """
    pass

@pytest.fixture(scope='session')
async def _kafka_global_consumer(_kafka_service, _bootstrap_servers) -> typing.AsyncGenerator[classes.KafkaConsumer, None]:
    pass

@pytest.fixture
async def kafka_consumer(_kafka_global_consumer) -> typing.AsyncGenerator[classes.KafkaConsumer, None]:
    """
    Per test Kafka consumer instance.

    :returns: :py:class:`testsuite.databases.kafka.classes.KafkaConsumer`
    """
    pass

@pytest.fixture(scope='session')
def kafka_custom_topics() -> dict[str, int]:
    """
    Redefine this fixture to pass your custom dictionary of topics' settings.
    """
    pass

@pytest.fixture(scope='session')
def kafka_local() -> classes.BootstrapServers:
    """
    Override to use custom local cluster bootstrap servers.
    If not empty, no service started.
    """
    pass

@pytest.fixture(scope='session')
def kafka_disabled(pytestconfig) -> bool:
    pass

@pytest.fixture(scope='session')
def _kafka_service_settings(kafka_custom_topics) -> classes.ServiceSettings:
    pass

@pytest.fixture(scope='session')
def _bootstrap_servers(kafka_local, _kafka_service_settings) -> str:
    pass

@pytest.fixture(scope='session')
def _kafka_service(ensure_service_started, kafka_local, kafka_disabled, pytestconfig, _kafka_service_settings) -> bool:
    pass
