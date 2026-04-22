import asyncio
import select
import socket
import sys
DEFAULT_TIMEOUT = 10.0
_DefaultTimeout = object()
_ASYNCIO_HAS_SENDTO = sys.version_info >= (3, 11)

class AsyncioSocket:

    def __init__(self, sock: socket.socket, loop: asyncio.AbstractEventLoop | None=None, timeout=DEFAULT_TIMEOUT):
        if loop is None:
            loop = asyncio.get_running_loop()
        self._loop: asyncio.AbstractEventLoop = loop
        self._sock: socket.socket = sock
        self._default_timeout = timeout
        sock.setblocking(False)

    def __repr__(self):
        return f'<AsyncioSocket for {self._sock}>'

    def __enter__(self):
        return self

    def __exit__(self, *args):
        self.close()

    @property
    def type(self):
        pass

    @property
    def socket(self) -> socket.socket:
        return self._sock

    def fileno(self) -> int:
        pass

    async def connect(self, address, *, timeout=_DefaultTimeout):
        pass

    async def sendto(self, *args, timeout=_DefaultTimeout):
        pass

    async def sendall(self, data, *, timeout=_DefaultTimeout):
        pass

    async def recv(self, size, *, timeout=_DefaultTimeout):
        pass

    async def recvfrom(self, *args, timeout=_DefaultTimeout):
        pass

    async def accept(self, *, timeout=_DefaultTimeout):
        pass

    def bind(self, address):
        pass

    def listen(self, *args):
        pass

    def getsockname(self):
        pass

    def setsockopt(self, *args, **kwargs):
        pass

    def close(self):
        pass

    def has_data(self) -> bool:
        pass

    def can_write(self) -> bool:
        pass

    async def wait_for_data(self, timeout=_DefaultTimeout):
        pass

    async def _with_timeout(self, awaitable, timeout):
        pass

    async def _sendto_legacy(self, *args, timeout):
        pass

    async def _recvfrom_legacy(self, *args, timeout):
        pass

class AsyncioSocketsFactory:

    def __init__(self, loop=None):
        if loop is None:
            loop = asyncio.get_running_loop()
        self._loop = loop

    def from_socket(self, sock, timeout=DEFAULT_TIMEOUT):
        pass

    def socket(self, *args, timeout=DEFAULT_TIMEOUT):
        pass

    async def getaddrinfo(self, *args, timeout=DEFAULT_TIMEOUT, **kwargs):
        pass

    def tcp(self, *, timeout=DEFAULT_TIMEOUT):
        pass

    def udp(self, *, timeout=DEFAULT_TIMEOUT):
        pass

    def socketpair(self, *args, timeout=DEFAULT_TIMEOUT, **kwargs):
        pass

def from_socket(sock: socket.socket | AsyncioSocket, *, loop=None, timeout=DEFAULT_TIMEOUT) -> AsyncioSocket:
    pass

def create_socket(*args, timeout=DEFAULT_TIMEOUT):
    pass

def create_tcp_socket(*args, timeout=DEFAULT_TIMEOUT):
    pass

def create_udp_socket(timeout=DEFAULT_TIMEOUT):
    pass

def create_socketpair(*args, timeout=DEFAULT_TIMEOUT, **kwargs):
    pass

async def getaddrinfo(*args, **kwargs):
    pass

def _legacy_io_handler(fut, sock_handler, *args):
    pass

async def _wait_for_data(loop, sock):
    pass
