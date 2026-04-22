"""
Logcapture allows to intercepts service logs on demand with context manager.

It starts tcp server and read logs sent by server.
"""
import asyncio
import collections
import contextlib
import enum
import logging
import typing
from testsuite.utils import callinfo, net, traceback
logger = logging.getLogger(__name__)

class BaseError(Exception):
    pass

class IncorrectUsageError(BaseError):
    """Incorrect usage error."""

class ClientConnectTimeoutError(BaseError):
    pass

class TimeoutError(BaseError):
    pass

class LogLevel(enum.IntEnum):
    """
    Represents log level as IntEnum, which supports comparison.

    Available levels are: TRACE, DEBUG, INFO, WARNING, ERROR, CRITICAL, NONE
    """
    TRACE = 0
    DEBUG = 1
    INFO = 2
    WARNING = 3
    ERROR = 4
    CRITICAL = 5
    NONE = 6

    @classmethod
    def from_string(cls, level: str) -> 'LogLevel':
        """Parse log level from the string."""
        pass

class CapturedLogs:

    def __init__(self, *, log_level: LogLevel) -> None:
        self._log_level = log_level
        self._logs: list[dict] = []
        self._subscribers = []
        self._closed = False

    @property
    def log_level(self):
        pass

    def is_closed(self):
        pass

    def close(self):
        pass

    async def publish(self, row: dict) -> None:
        pass

    def subscribe(self, query: dict, decorated):
        pass

    def __iter__(self) -> typing.Iterator[dict]:
        return iter(self._logs)

class Capture:

    def __init__(self, logs: CapturedLogs):
        self._logs = logs

    def select(self, **query) -> list[dict]:
        """Select logs matching query.

        Could only be used after capture contextmanager block.

        .. code-block:: python

           async with logcapture_server.capture() as capture:
               ...
           records = capture.select(text='Message to capture')
        """
        pass

    def subscribe(self, **query):
        """Subscribe to records matching `query`. Returns decorator function.
        `subscribe()` may only be used within `capture()` block. Callqueue is returned.

        .. code-block:: python

           async with logcapture_server.capture() as capture:
               @capture.subscribe(text='Message to capture')
               def log_event(link, **other):
                   ...
               ...
               assert log_event.wait_call()
        """
        pass

class CaptureServer:
    _capture: CapturedLogs | None

    def __init__(self, *, log_level: LogLevel, parse_line: collections.abc.Callable[[bytes], dict]):
        """Capture server."""
        self._log_level = log_level
        self._client_cond = asyncio.Condition()
        self._capture = None
        self._tasks = []
        self._parse_line = parse_line
        self._started = False
        self._socknames = []

    @property
    def default_log_level(self) -> LogLevel:
        """Returns default log level specified on object creation."""
        pass

    def getsocknames(self) -> list[tuple]:
        """Return list of server socket names."""
        pass

    @contextlib.asynccontextmanager
    async def start(self, host='localhost', port=0, **kwargs) -> typing.AsyncIterator['CaptureServer']:
        """Starts capture logs asyncio server.

        Arguments are directly passed to `asyncio.start_server`. Server could be started
        only once. Capture server is returned. Server is closed when contextmanager
        is finished.
        """
        pass

    async def wait_for_client(self, timeout: float=10.0):
        """Waits for logserver client to connect."""
        pass

    async def _handle_client(self, reader, writer):
        pass

    @contextlib.asynccontextmanager
    async def capture(self, *, log_level: LogLevel | None=None, timeout: float=10.0) -> typing.AsyncIterator[Capture]:
        """
        Starts logs capture. Returns `Capture` object.
        """
        pass

def _match_entry(row: dict, query: dict) -> bool:
    pass
__tracebackhide__ = traceback.hide(BaseError, FileNotFoundError)
