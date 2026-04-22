import typing
import urllib.parse
import psycopg2.extensions

class _NotSet:
    pass

class PgConnectionInfo(typing.NamedTuple):
    """
    PostgreSQL connection parameters
    """
    host: str | None = None
    port: int | None = None
    user: str | None = None
    password: str | None = None
    options: str | None = None
    sslmode: str | None = None
    dbname: str | None = None

    def get_dsn(self) -> str:
        """PostgreSQL connection string in DSN format"""
        pass

    def get_uri(self) -> str:
        """PostgreSQL connection string in URI format"""
        pass

    def replace(self, **kwargs) -> 'PgConnectionInfo':
        """Return a new :py:class:`PgConnectionInfo` value replacing specified
        fields with new values
        """
        pass

def parse_connection_string(connstr: str) -> PgConnectionInfo:
    """Parse PostgreSQL connection string.
    :param connstr: connection string in DSN or URI format as specified in
    https://www.postgresql.org/docs/current/libpq-connect.html#LIBPQ-CONNSTRING
    """
    pass

def get_connection_uri(**kwargs):
    pass
