import collections
import collections.abc
import concurrent.futures
import contextlib
import re
import typing
import pytest
from . import connection, control, discover, exceptions, service, utils
DB_FILE_RE_PATTERN = re.compile('/pg_(?P<pg_db_alias>\\w+)(/?\\w*)\\.sql$')

class ServiceLocalConfig(collections.abc.Mapping):

    def __init__(self, databases: list[discover.PgShardedDatabase], pgsql_control: control.PgControl, cleanup_exclude_tables: frozenset[str]):
        self._initialized = False
        self._pgsql_control = pgsql_control
        self._databases = databases
        self._shard_connections = {shard.pretty_name: pgsql_control.get_connection_cached(shard.dbname) for db in self._databases for shard in db.shards}
        self._cleanup_exclude_tables = cleanup_exclude_tables

    def __len__(self) -> int:
        return len(self._shard_connections)

    def __iter__(self) -> typing.Iterator[str]:
        return iter(self._shard_connections)

    def __getitem__(self, dbname: str) -> connection.PgConnectionInfo:
        """Get
        :py:class:`testsuite.databases.pgsql.connection.PgConnectionInfo`
        instance by database name
        """
        return self._shard_connections[dbname].conninfo

    def initialize(self, parallel_init: bool) -> dict[str, control.ConnectionWrapper]:
        pass

def pytest_addoption(parser):
    """
    :param parser: pytest's argument parser
    """
    pass

def pytest_report_header(config):
    pass

def pytest_configure(config):
    pass

def pytest_service_register(register_service):
    pass

@pytest.fixture(scope='session')
def pgsql_cleanup_exclude_tables() -> frozenset[str]:
    pass

@pytest.fixture
def pgsql(_pgsql, pgsql_apply) -> dict[str, control.PgDatabaseWrapper]:
    """
    Returns str to
    :py:class:`testsuite.databases.pgsql.control.PgDatabaseWrapper` dictionary

    Example usage:

    .. code-block:: python

      def test_pg(pgsql):
          cursor = pgsql['example_db'].cursor()
          cursor.execute('SELECT ... FROM ...WHERE ...')
          assert list(cusror) == [...]
    """
    pass

@pytest.fixture(scope='session')
def pgsql_local_create(_pgsql_control, pgsql_cleanup_exclude_tables) -> typing.Callable[[list[discover.PgShardedDatabase]], ServiceLocalConfig]:
    """Creates pgsql configuration.

    :param databases: List of databases.
    :returns: :py:class:`ServiceLocalConfig` instance.
    """
    pass

@pytest.fixture(scope='session')
def pgsql_disabled(pytestconfig) -> bool:
    pass

@pytest.fixture
def pgsql_local(pgsql_local_create) -> ServiceLocalConfig:
    """Configures local pgsql instance.

    :returns: :py:class:`ServiceLocalConfig` instance.

    In order to use pgsql fixture you have to override pgsql_local()
    in your local conftest.py file, example:

    .. code-block:: python

        @pytest.fixture(scope='session')
        def pgsql_local(pgsql_local_create):
            databases = discover.find_schemas(
                'service_name', [PG_SCHEMAS_PATH])
            return pgsql_local_create(list(databases.values()))

    Sometimes it is desirable to have tests-only database, maybe used in one
    particular test or tests group. This can be achieved by by overriding
    ``pgsql_local`` fixture in your test file:

    .. code-block:: python

        @pytest.fixture
        def pgsql_local(pgsql_local_create):
            databases = discover.find_schemas(
                'testsuite', [pathlib.Path('custom/pgsql/schema/path')])
            return pgsql_local_create(list(databases.values()))

    ``pgsql_local`` provides access to PostgreSQL connection parameters:

    .. code-block:: python

        def get_custom_connection_string(pgsql_local):
            conninfo = pgsql_local['database_name']
            custom_dsn: str = conninfo.replace(options='-c opt=val').get_dsn()
            return custom_dsn
    """
    pass

@pytest.fixture(scope='session')
def pgsql_parallelization_enabled():
    pass

@pytest.fixture
def _pgsql(_pgsql_service, _pgsql_control, pgsql_local, pgsql_cleanup_exclude_tables, pgsql_disabled: bool, pgsql_parallelization_enabled: bool) -> dict[str, control.ConnectionWrapper]:
    pass

@pytest.fixture(scope='session')
def pgsql_background_truncate_enabled():
    pass

@pytest.fixture
def _pgsql_apply_queries(request, _pgsql: ServiceLocalConfig, _pgsql_query_loader) -> dict[str, list[control.PgQuery]]:
    pass

@pytest.fixture
def pgsql_apply(_pgsql: ServiceLocalConfig, load, pgsql_background_truncate_enabled: bool, pgsql_parallelization_enabled: bool, _pgsql_apply_queries) -> None:
    """Initialize PostgreSQL database with data.

    By default pg_${DBNAME}.sql and pg_${DBNAME}/*.sql files are used
    to fill PostgreSQL databases.

    Use pytest.mark.pgsql to change this behaviour:

    @pytest.mark.pgsql(
        'foo@0',
        files=[
            'pg_foo@0_alternative.sql'
        ],
        directories=[
            'pg_foo@0_alternative_dir'
        ],
        queries=[
          'INSERT INTO foo VALUES (1, 2, 3, 4)',
        ]
    )
    """
    pass

@pytest.fixture
def _pgsql_query_loader(get_file_path, get_directory_path, mockserver_info):
    pass

@pytest.fixture
def _pgsql_service(pytestconfig, pgsql_disabled: bool, ensure_service_started, pgsql_local: ServiceLocalConfig, _pgsql_service_settings) -> None:
    pass

@pytest.fixture(scope='session')
def _pgsql_control(pytestconfig, pgsql_disabled: bool):
    pass

@pytest.fixture(scope='session')
def _pgsql_service_settings() -> service.ServiceSettings:
    pass

@pytest.fixture(scope='session')
def _pgsql_conninfo(request, _pgsql_service_settings) -> connection.PgConnectionInfo:
    pass

def _get_connection_info(config):
    pass
