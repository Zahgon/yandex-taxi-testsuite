import contextlib
import dataclasses
import logging
import pathlib
import pymysql
import pymysql.constants
from testsuite.environment import shell
from testsuite.utils import cached_property
from . import classes, exceptions
logger = logging.getLogger(__name__)
MYSQL_HELPER = pathlib.Path(__file__).parent.joinpath('scripts/mysql-helper')

@dataclasses.dataclass(frozen=True)
class MysqlQuery:
    body: str
    source: str
    path: str | None

class ConnectionWrapper:
    """MySQL database connection wrapper."""

    def __init__(self, connection, conninfo, tables):
        self._connection = connection
        self._conninfo = conninfo
        self._tables: list[str] = tables

    @property
    def conninfo(self) -> classes.ConnectionInfo:
        """:py:class:`classes.ConnectionInfo` instance."""
        pass

    def cursor(self, **kwargs) -> pymysql.cursors.Cursor:
        """Returns cursor instance."""
        pass

    def dict_cursor(self, **kwargs) -> pymysql.cursors.Cursor:
        """Return dictionary cursor, pymysql.cursors.DictCursor."""
        pass

    def commit(self) -> None:
        pass

    def _truncate_non_empty_tables(self) -> list[str] | None:
        pass

    def apply_queries(self, queries: list[MysqlQuery], keep_tables: list[str] | None=None, truncate_non_empty: bool=False) -> None:
        pass

class ConnectionCache:

    def __init__(self, conninfo, verbose: bool=False):
        self._conninfo = conninfo
        self._cache: dict = {}
        self._master_connection = None

    def get_master_connection(self):
        pass

    def get_conninfo(self, dbname: str) -> classes.ConnectionInfo:
        pass

    def get_connection(self, dbname):
        pass

    def _create_connection(self, dbname):
        pass

    def _connect(self, conninfo: classes.ConnectionInfo):
        pass

class DatabasesState:
    _migrations_run: set[tuple[str, str]]
    _initialized: set[str]

    def __init__(self, connections: ConnectionCache, verbose: bool=False):
        self._need_save_tables = True
        self._connections = connections
        self._verbose = verbose
        self._migrations_run = set()
        self._initialized = set()
        self._tables: dict[str, list[str]] = dict()

    def get_connection(self, dbname: str, create_db: bool=True):
        pass

    def wrapper_for(self, dbname: str):
        pass

    def run_migration(self, dbname: str, path: str):
        pass

    @cached_property
    def known_databases(self):
        pass

    def _initdb(self, dbname: str):
        pass

    def save_tables(self, dbname: str) -> None:
        pass

class Control:

    def __init__(self, databases: classes.DatabasesDict, state: DatabasesState):
        self._databases = databases
        self._state = state

    def get_wrappers(self):
        pass

    def run_migrations(self):
        pass

    def _run_database_migrations(self, dbconfig):
        pass

def _build_mysql_args(conninfo: classes.ConnectionInfo) -> list[str]:
    pass

def _run_script(conninfo: classes.ConnectionInfo, args: list[str], verbose: bool):
    pass
