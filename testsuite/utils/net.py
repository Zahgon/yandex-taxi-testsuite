import asyncio
import asyncio.events
import contextlib
import errno
import pathlib
import socket
DEFAULT_BACKLOG = 50

class MultipleSocketServer(asyncio.events.AbstractServer):

    def __init__(self, servers):
        self._servers = servers

    def get_loop(self):
        pass

    def start_serving(self):
        pass

    async def serve_forever(self):
        pass

    def is_serving(self):
        pass

    @property
    def sockets(self):
        pass

    def close(self):
        pass

    async def wait_closed(self):
        pass

def create_tcp_server(factory, *, loop=None, host='localhost', port=0, sock=None, **kwargs):
    pass

def create_unix_server(factory, path: pathlib.Path, *, loop=None, sock=None, **kwargs):
    pass

@contextlib.asynccontextmanager
async def create_server_multiple(factory, sockets, *, loop=None, **kwargs):
    pass

async def start_multiple_servers(client_connected_cb, sockets, *, loop=None, **kwargs) -> MultipleSocketServer:
    pass

def bind_socket_multiple(hostname='localhost', port=0, family=socket.AF_UNSPEC, type=socket.SOCK_STREAM, backlog=DEFAULT_BACKLOG, retries=15):
    """
    Bind multiple sockets for both IPv4 and IPv6 addresses.

    If `port` is zero tries to bind the same port for all addresses,
    `retries` times.
    """
    pass

def bind_socket(hostname='localhost', port=0, family=socket.AF_INET, type=socket.SOCK_STREAM, proto=-1, backlog=DEFAULT_BACKLOG):
    pass

def bind_unix_socket(socket_path, backlog=DEFAULT_BACKLOG):
    pass

@contextlib.contextmanager
def closing_sockets(sockets):
    pass

@contextlib.contextmanager
def _close_sockets_on_error(sockets):
    pass

@contextlib.asynccontextmanager
async def _create_server(factory, *, loop=None, **kwargs):
    pass

@contextlib.asynccontextmanager
async def _create_unix_server(factory, *, loop=None, **kwargs):
    pass

def _bind_socket_multiple(hostname, port, *, family, type, backlog):
    """
    Bind multiple sockets for both IPv4 and IPv6 addresses.
    """
    pass
