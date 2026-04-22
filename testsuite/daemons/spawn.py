import asyncio
import contextlib
import ctypes
import inspect
import logging
import signal
import subprocess
import sys
import time
from collections.abc import AsyncGenerator, Sequence
from testsuite.utils import traceback
SIGNAL_ERRORS: dict[int, str] = {signal.SIGSEGV: 'Service crashed with {signal_name} signal (segmentation fault)', signal.SIGABRT: 'Service aborted by {signal_name} signal'}
DEFAULT_SIGNAL_ERROR = 'Service terminated by {signal_name} signal'
_KNOWN_SIGNALS: dict[int, str] = {signal.SIGABRT: 'SIGABRT', signal.SIGBUS: 'SIGBUS', signal.SIGFPE: 'SIGFPE', signal.SIGHUP: 'SIGHUP', signal.SIGINT: 'SIGINT', signal.SIGKILL: 'SIGKILL', signal.SIGPIPE: 'SIGPIPE', signal.SIGSEGV: 'SIGSEGV', signal.SIGTERM: 'SIGTERM'}
_POLL_TIMEOUT = 0.1
logger = logging.getLogger(__name__)

class BaseError(Exception):
    pass

class HealthCheckError(BaseError):
    pass

class ExitCodeError(BaseError):

    def __init__(self, message: str, exit_code: int) -> None:
        super().__init__(message)
        self.exit_code = exit_code

class AioReaders:

    def __init__(self, loop=None):
        self._tasks = []
        self._loop = loop

    async def aclose(self):
        pass

    async def add(self, pipe, handler):
        pass

@contextlib.asynccontextmanager
async def spawned(args: Sequence[str], *, shutdown_signal: int=signal.SIGINT, shutdown_timeout: float=120, subprocess_spawner=None, stdout_handler=None, stderr_handler=None, **kwargs) -> AsyncGenerator[subprocess.Popen, None]:
    pass

def exit_code_error(process: subprocess.Popen) -> ExitCodeError:
    pass

def _exit_code_text(retcode: int):
    pass

@contextlib.asynccontextmanager
async def _shutdown_service(*args, **kwargs):
    pass

async def _do_service_shutdown(process, *, shutdown_signal, shutdown_timeout):
    pass

def _pretty_signal(signum: int) -> str:
    pass

async def _create_pipe_reader(pipe, loop=None):
    pass
_PR_SET_PDEATHSIG = 1
if sys.platform == 'linux':
    _LIBC = ctypes.CDLL('libc.so.6')
else:
    _LIBC = None

def _setup_process() -> None:
    pass
__tracebackhide__ = traceback.hide(BaseError)
