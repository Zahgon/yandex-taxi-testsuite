import asyncio
import contextlib
import socket
import pytest
from testsuite.utils import cached_property, net

class Mockserver:
    """TCP/IP mockserver."""

    def __init__(self, server):
        self._handler = None
        self._sockets = tuple(server.sockets)

    async def _client_connected_cb(self, reader, writer):
        pass

    @cached_property
    def sockets(self) -> tuple[socket.socket]:
        """Returns list of server sockets."""
        pass

    @cached_property
    def address(self) -> tuple[str, int]:
        """
        Returns service address (host, port)
        """
        pass

    @contextlib.asynccontextmanager
    async def open_connection(self, timeout=10.0):
        """Async context manager creates connection to the service.

        :param timeout: timeout to establish connection.

        Returns pair (read, writer).

        Connection is closed when context manager is done.

        Wrapper around :func:`asyncio.open_connection`


        .. code-block:: python

           async with server.open_connection() as (reader, writer):
               ...
        """
        pass

    @contextlib.contextmanager
    def client_handler(self, handler):
        """Context manager to install per-test client handler.

        .. code-block:: python

          async def handle_client(reader, writer):
              writer.write(b'hello\\r\\n')
              await writer.drain()
              writer.close()

          with _tcp_mockserver.client_handler(handle_client):
              ...
        """
        pass

class ProtocolFactory:

    def __init__(self):
        self.client_handler = None

    def __call__(self):
        if self.client_handler is None:
            pytest.fail('No client handler attached')
        reader = asyncio.StreamReader()
        protocol = asyncio.StreamReaderProtocol(reader, self.client_handler)
        return protocol

    @contextlib.contextmanager
    def attach_client_handler(self, handler):
        pass

@pytest.fixture(scope='session')
async def create_tcp_mockserver():
    pass
