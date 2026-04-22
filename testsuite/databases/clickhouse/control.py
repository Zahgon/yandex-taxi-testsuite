import dataclasses
import logging
import pathlib
import clickhouse_driver
from . import classes
logger = logging.getLogger(__name__)

@dataclasses.dataclass(frozen=True)
class ClickhouseQuery:
    body: str
    source: str
    path: str | None

class ConnectionCache:

    def __init__(self, conn_info: classes.ConnectionInfo):
        self._conn_info = conn_info
        self._cache: dict[str, clickhouse_driver.Client] = {}
        self._master_connection = None

    def get_master_connection(self):
        pass

    def get_connection(self, dbname: str) -> clickhouse_driver.Client:
        pass

    def get_connection_info(self, dbname: str) -> classes.ConnectionInfo:
        pass

    def _create_connection(self, dbname: str):
        pass

    def _connect(self, conn_info: classes.ConnectionInfo):
        pass

class DatabasesState:
    _migrations_run: set[tuple[str, pathlib.Path]]
    _initialized: set[str]

    def __init__(self, connections: ConnectionCache, verbose: bool=False):
        self._connections = connections
        self._verbose = verbose
        self._migrations_run = set()
        self._initialized = set()

    def get_connection(self, dbname: str, create_db: bool=True) -> clickhouse_driver.Client:
        pass

    def run_migration(self, dbname: str, path: pathlib.Path):
        pass

    def _init_db(self, dbname: str):
        pass

class Control:

    def __init__(self, databases: classes.DatabasesDict, state: DatabasesState):
        self._databases = databases
        self._state = state

    def get_connections(self):
        pass

    def run_migrations(self):
        pass

    def _run_database_migrations(self, dbconfig: classes.DatabaseConfig):
        pass

def _get_db_tables_list(connection: clickhouse_driver.Client):
    pass

def apply_queries(connection: clickhouse_driver.Client, queries: list[ClickhouseQuery]):
    pass
