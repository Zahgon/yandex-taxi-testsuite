import hashlib
import pathlib
import typing
import urllib.parse

def scan_sql_directory(root: pathlib.Path) -> list[pathlib.Path]:
    pass

def connstr_replace_dbname(connstr: str, dbname: str) -> str:
    """Replace dbname in existing connection string."""
    pass

def get_files_hash(paths: typing.Iterable[pathlib.Path]) -> str:
    pass
