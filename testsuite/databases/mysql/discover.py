import collections
import pathlib
from typing import Any, DefaultDict
from . import classes, utils

def find_schemas(schema_dirs: list[pathlib.Path], dbprefix: str='testsuite-', extra_schema_args: dict[str, Any] | None=None) -> dict[str, classes.DatabaseConfig]:
    """Retrieve database schemas from filesystem.

    :param schema_dirs: list of schema paths
    :param dbprefix: database name internal prefix
    :param extra_schema_args: for each DB contains list
        of tables we don't have to truncate and flag for explicit creation
        example:

        .. code-block:: python

          {
              'database1': {
                  'create': False,
                  'truncate_non_empty': True,
                  'keep_tables': [
                      'table1', 'table2'
                  ]
              }
          }

    :returns: Dictionary where key is dbname and value is
        ``classes.DatabaseConfig`` instance.
    """
    pass

def _scan_path(schema_path: pathlib.Path) -> DefaultDict[str, list[pathlib.Path]]:
    pass
