import collections
import pathlib
import typing
from . import classes, utils

def find_schemas(schema_dirs: list[pathlib.Path], dbprefix: str='testsuite-') -> dict[str, classes.DatabaseConfig]:
    pass

def _scan_path(schema_path: pathlib.Path) -> typing.DefaultDict[str, list[pathlib.Path]]:
    pass
