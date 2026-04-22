import collections
import dataclasses
import hashlib
import itertools
import logging
import pathlib
from collections.abc import Iterable
from typing import DefaultDict
from . import exceptions, utils
logger = logging.getLogger(__name__)
SINGLE_SHARD = -1
DB_NAME_MAX = 31

@dataclasses.dataclass(frozen=True)
class ShardName:
    db_name: str
    shard: int

@dataclasses.dataclass
class ShardFiles:
    name: ShardName
    files: list[pathlib.Path] | None = None
    pg_migrations: list[pathlib.Path] | None = None

@dataclasses.dataclass
class ShardFileInfo:
    files: list[pathlib.Path]
    pg_migrations: list[pathlib.Path]

    def extend(self, other: ShardFiles) -> None:
        pass
ShardPathesDict = dict[int, ShardFileInfo]

@dataclasses.dataclass(frozen=True)
class PgShard:
    shard_id: int
    pretty_name: str
    dbname: str
    files: list[pathlib.Path]
    migrations: list[pathlib.Path]

    def get_schema_hash(self) -> str:
        pass

@dataclasses.dataclass(frozen=True)
class PgShardedDatabase:
    service_name: str | None
    dbname: str
    shards: list[PgShard]

def find_schemas(service_name: str | None, schema_dirs: list[pathlib.Path]) -> dict[str, PgShardedDatabase]:
    """Read database schemas from directories ``schema_dirs``. ::

     |- schema_path/
       |- database1.sql
       |- database2.sql

    :param service_name: service name used as prefix for database name if not
           empty, e.g. "servicename_dbname".
    :param schema_dirs: list of pathes to scan for schemas
    :returns: :py:class:`Dict[str, PgShardedDatabase]` where key is
              database name as stored in :py:attr:`PgShard.dbname`
    """
    pass

def _find_databases_schemas(service_name: str | None, schema_path: pathlib.Path) -> dict[str, PgShardedDatabase]:
    pass

def _build_shard_files_map(root_path: pathlib.Path) -> DefaultDict[str, ShardPathesDict]:
    pass

def _find_shard_files(schema_path: pathlib.Path) -> Iterable[ShardFiles]:
    pass

def _get_shard_schema_files(path: pathlib.Path) -> ShardFiles | None:
    pass

def _raise_if_invalid_shards(dbname: str, shards: ShardPathesDict) -> None:
    pass

def _create_pgshard(dbname: str, service_name: str | None=None, shard_id: int=SINGLE_SHARD, files: list[pathlib.Path] | None=None, migrations: list[pathlib.Path] | None=None) -> PgShard:
    pass
_names_used = {}

def _database_name(service_name: str | None, dbname: str, shard_id: int):
    pass

def _shortened(name: str, suffix: str):
    pass

def _parse_shard_name(name) -> ShardName:
    pass

def _normalize_name(name):
    pass
