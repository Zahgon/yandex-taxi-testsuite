import contextlib
import typing
import psycopg2.extensions
import psycopg2.pool

class AutocommitConnectionPool:

    def __init__(self, minconn: int, maxconn: int, uri: str) -> None:
        self._pool = psycopg2.pool.ThreadedConnectionPool(minconn, maxconn, uri)

    @contextlib.contextmanager
    def get_connection(self) -> typing.Generator[psycopg2.extensions.connection, None, None]:
        pass

    def close(self) -> None:
        pass
