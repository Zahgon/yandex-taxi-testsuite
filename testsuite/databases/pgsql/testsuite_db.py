from testsuite import utils
from . import connection, pool
CREATE_DATABASE_TEMPLATE = '\nCREATE DATABASE "{}" WITH TEMPLATE = template0\nENCODING=\'UTF8\' LC_COLLATE=\'C\' LC_CTYPE=\'C\'\n'
DATABASE_EXISTS_TEMPLATE = 'SELECT 1 FROM pg_database WHERE datname=%s'
CREATE_TABLE_SQL = '\nCREATE TABLE IF NOT EXISTS applied_schemas (\n    db_name TEXT PRIMARY KEY,\n    schema_hash TEXT\n);\n'
UPDATE_DB_HASH_TEMPLATE = '\nINSERT INTO applied_schemas (db_name, schema_hash)\nVALUES (%(dbname)s, %(hash)s)\nON CONFLICT (db_name) DO UPDATE SET\n    schema_hash = %(hash)s\nWHERE applied_schemas.db_name = %(dbname)s\n'
SELECT_DB_HASH_TEMPLATE = 'SELECT db_name, schema_hash FROM applied_schemas'
TESTSUITE_DB_NAME = 'testsuite'

class AppliedSchemaHashes:

    def __init__(self, pool: pool.AutocommitConnectionPool, base_conninfo: connection.PgConnectionInfo):
        self._pool = pool
        self._conninfo = base_conninfo.replace(dbname=TESTSUITE_DB_NAME)
        self._create_db()
        self._create_schema_table()

    def get_hash(self, dbname: str) -> str | None:
        """Get hash of schema applied to a database"""
        pass

    def set_hash(self, dbname: str, schema_hash: str):
        """Store in testsuite database and remember locally a hash of schema
        applied to a database
        """
        pass

    @utils.cached_property
    def _hash_by_dbname(self) -> dict[str, str]:
        pass

    def _create_schema_table(self) -> None:
        pass

    def _create_db(self) -> None:
        pass
