import concurrent.futures
import contextlib
import dataclasses
import logging
import pathlib
import time
import typing
import warnings
import psycopg2
import psycopg2.extensions
import psycopg2.extras
from testsuite.environment import shell
from . import connection, discover, exceptions, pool, service, testsuite_db
from .exceptions import __tracebackhide__
logger = logging.getLogger(__name__)
CREATE_DATABASE_TEMPLATE = '\nCREATE DATABASE "{}" WITH TEMPLATE = template0\nENCODING=\'UTF8\' LC_COLLATE=\'C\' LC_CTYPE=\'C\'\n'
DROP_DATABASE_TEMPLATE = 'DROP DATABASE IF EXISTS "{}"'
LIST_TABLES_SQL = "\nSELECT CONCAT(table_schema, '.', table_name)\nFROM information_schema.tables\nWHERE table_schema != 'information_schema' AND\ntable_schema != 'pg_catalog' AND table_type = 'BASE TABLE'\nORDER BY table_schema,table_name\n"
TRUNCATE_SQL_TEMPLATE = 'TRUNCATE TABLE {tables} RESTART IDENTITY'
TRUNCATE_RETRIES = 5
TRUNCATE_RETRY_DELAY = 0.005

class BaseError(Exception):
    pass

class UninitializedUsageError(BaseError):
    pass

@dataclasses.dataclass(frozen=True)
class PgQuery:
    body: str
    source: str
    path: str | None

class ConnectionWrapper:

    def __init__(self, conninfo: connection.PgConnectionInfo):
        self._initialized = False
        self._conninfo = conninfo
        self._conn: psycopg2.extensions.connection | None = None
        self._tables: list[str] | None = None
        self._truncate_thread: None | concurrent.futures.Future[None] = None
        self._executer = concurrent.futures.ThreadPoolExecutor(max_workers=1)

    def initialize(self, cleanup_exclude_tables: frozenset[str]):
        pass

    @property
    def conninfo(self) -> connection.PgConnectionInfo:
        """returns
        :py:class:`testsuite.databases.pgsql.connection.PgConnectionInfo`
        """
        pass

    @property
    def conn(self) -> psycopg2.extensions.connection:
        """:returns: :py:class:`psycopg2.extensions.connection`"""
        pass

    def cursor(self, **kwargs) -> psycopg2.extensions.cursor:
        """:returns: :py:class:`psycopg2.extensions.cursor`"""
        pass

    def dict_cursor(self, **kwargs) -> psycopg2.extensions.cursor:
        """Returns dictionary cursor, see psycopg2.extras.DictCursor

        :returns: :py:class:`psycopg2.extensions.cursor`
        """
        pass

    def apply_queries(self, queries: typing.Iterable[PgQuery]) -> None:
        """Apply queries to database"""
        pass

    def close(self):
        pass

    def schedule_truncation(self):
        pass

    def _try_truncate_tables(self, cursor) -> None:
        pass

    def _truncate_tables(self, cursor) -> None:
        pass

    @staticmethod
    def _apply_query(cursor, query: PgQuery) -> None:
        pass

class PgDatabaseWrapper:

    def __init__(self, connection: ConnectionWrapper):
        self._connection = connection

    @property
    def conninfo(self) -> connection.PgConnectionInfo:
        """returns
        :py:class:`testsuite.databases.pgsql.connection.PgConnectionInfo`
        """
        pass

    @property
    def conn(self) -> psycopg2.extensions.connection:
        """:returns: :py:class:`psycopg2.extensions.connection`"""
        pass

    def cursor(self, **kwargs) -> psycopg2.extensions.cursor:
        """:returns: :py:class:`psycopg2.extensions.cursor`"""
        pass

    def dict_cursor(self, **kwargs) -> psycopg2.extensions.cursor:
        """Returns dictionary cursor, see psycopg2.extras.DictCursor

        :returns: :py:class:`psycopg2.extensions.cursor`
        """
        pass

    def apply_queries(self, queries: typing.Iterable[str]) -> None:
        """Apply queries to database"""
        pass

class PgControl:
    _applied_schemas: dict[str, set[pathlib.Path]]
    _connections: dict[str, ConnectionWrapper]
    _connection_pool: pool.AutocommitConnectionPool | None
    _applied_schema_hashes: testsuite_db.AppliedSchemaHashes | None

    def __init__(self, pgsql_conninfo: connection.PgConnectionInfo, *, verbose: int, skip_applied_schemas: bool) -> None:
        self._connection_pool = None
        self._conninfo = pgsql_conninfo
        self._connections = {}
        self._psql_helper = _get_psql_helper()
        self._pgmigrate = _get_pgmigrate()
        self._verbose = verbose
        self._applied_schemas = {}
        self._skip_applied_schemas = skip_applied_schemas
        self._applied_schema_hashes = None

    def initialize(self) -> None:
        pass

    def get_connection_cached(self, dbname) -> ConnectionWrapper:
        pass

    def initialize_sharded_db(self, database: discover.PgShardedDatabase) -> None:
        pass

    def _initialize_shard(self, shard: discover.PgShard) -> None:
        pass

    def _create_database(self, dbname: str) -> None:
        pass

    def _apply_schema(self, shard: discover.PgShard) -> None:
        pass

    def _run_script(self, dbname, path) -> None:
        pass

    def _run_pgmigrate(self, dbname, path) -> None:
        pass

    def close(self):
        pass

    def _get_connection_uri(self, dbname: str) -> str:
        pass

    def _get_connection_dsn(self, dbname: str) -> str:
        pass

def _get_psql_helper() -> pathlib.Path:
    pass

def _get_pgmigrate() -> pathlib.Path:
    pass
