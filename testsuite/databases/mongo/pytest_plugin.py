import contextlib
import dataclasses
import multiprocessing.pool
import pathlib
import pprint
import random
import re
import pymongo
import pymongo.collection
import pymongo.errors
import pytest
from bson import json_util
from testsuite import types, utils
from . import connection, ensure_db_indexes, mongo_schema, service
DB_FILE_RE_PATTERN = re.compile('^db_(?P<mongo_db_alias>\\w+)\\.json$')
JSON_OPTIONS = json_util.JSONOptions(tz_aware=False)
MONGO_OBJECT_HOOKS = ('$binary', '$code', '$date', '$dbPointer', '$maxKey', '$minKey', '$numberDecimal', '$numberDouble', '$numberInt', '$numberLong', '$oid', '$ref', '$regex', '$regularExpression', '$symbol', '$timestamp', '$undefined', '$uuid')

class BaseError(Exception):
    """Base testsuite error"""

class UnknownCollectionError(BaseError):
    pass

class CollectionWrapper:

    def __init__(self, collections):
        for alias, collection in collections.items():
            setattr(self, alias, collection)
        self._collections = collections.copy()
        self._aliases = tuple(collections.keys())

    def __getitem__(self, alias: str) -> pymongo.collection.Collection:
        return self._collections[alias]

    def __contains__(self, alias: str) -> bool:
        return alias in self._collections

    def get_aliases(self) -> tuple[str]:
        pass

class CollectionWrapperFactory:

    def __init__(self, connection_info: connection.ConnectionInfo):
        self._connection_info = connection_info

    @property
    def connection_string(self) -> str:
        pass

    @utils.cached_property
    def client(self) -> pymongo.MongoClient:
        pass

    def create_collection_wrapper(self, collection_names, mongodb_settings) -> CollectionWrapper:
        pass

def pytest_configure(config):
    pass

def pytest_addoption(parser):
    """
    :param parser: pytest's argument parser
    """
    pass

def pytest_report_header(config):
    pass

def pytest_service_register(register_service):
    pass

def pytest_register_object_hooks():
    pass

@pytest.fixture
def mongodb(mongodb_init, _mongodb_local: CollectionWrapper) -> CollectionWrapper:
    pass

@pytest.fixture
def mongo_connections(mongodb_settings, mongo_connection_info, mongo_extra_connections, _mongo_local_collections) -> dict[str, str]:
    pass

@pytest.fixture
def mongo_extra_connections() -> tuple[str, ...]:
    """
    Override this if you need to access mongo connections besides those
    defined in mongo_connections fixture
    """
    pass

@pytest.fixture(scope='session')
def mongo_connection_info(pytestconfig) -> connection.ConnectionInfo:
    pass

@pytest.fixture
def mongodb_settings(mongo_schema_directory, mongo_schema_extra_directories, _mongo_schema_cache) -> mongo_schema.MongoSchemas:
    pass

@pytest.fixture
def mongodb_collections(mongodb_settings) -> tuple[str, ...]:
    """
    Override this to enable access to named collections within test module

    Returns all available collections by default.
    """
    pass

@pytest.fixture(scope='session')
def mongo_schema_extra_directories() -> tuple[str, ...]:
    """
    Override to use collection schemas besides those defined by
    ``mongo_schema_directory`` fixture
    """
    pass

@pytest.fixture(scope='session')
def _mongo_indexes_ensured() -> set[str]:
    pass

@pytest.fixture
def _mongo_service(pytestconfig, ensure_service_started, _mongodb_local, _mongo_service_settings) -> None:
    pass

@pytest.fixture
def _mongo_create_indexes(_mongodb_local, mongodb_settings, pytestconfig, _mongo_indexes_ensured, _mongo_service) -> None:
    pass

@pytest.fixture(scope='session')
def _mongo_thread_pool() -> types.YieldFixture[multiprocessing.pool.ThreadPool,]:
    pass

@pytest.fixture
def _mongo_query_loader(load_json):
    pass

@pytest.fixture
def mongodb_init(request, verify_file_paths, static_dir: pathlib.Path, _mongodb_local, _mongo_thread_pool, _mongo_create_indexes, _mongo_query_loader) -> None:
    """Populate mongodb with fixture data."""
    pass

@pytest.fixture
def _mongodb_local(mongodb_settings, _mongo_local_collections, _mongo_collection_wrapper_factory: CollectionWrapperFactory) -> CollectionWrapper:
    pass

@pytest.fixture(scope='session')
def _mongo_collection_wrapper_factory(mongo_connection_info: connection.ConnectionInfo) -> CollectionWrapperFactory:
    pass

@pytest.fixture
def _mongo_local_collections(request, mongodb_collections) -> set[str]:
    pass

@pytest.fixture(scope='session')
def _mongo_schema_cache() -> mongo_schema.MongoSchemaCache:
    pass

@pytest.fixture(scope='session')
def _mongo_service_settings(pytestconfig) -> service.ServiceSettings | None:
    pass

def _is_relevant_file(request, static_dir: pathlib.Path, file_path: pathlib.Path) -> bool:
    pass

def _is_nested_path(parent: pathlib.Path, nested: pathlib.Path) -> bool:
    pass

def _mongo_object_hook(doc):
    pass

def _get_connection_info(config):
    pass
