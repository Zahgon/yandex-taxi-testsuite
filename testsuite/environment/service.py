import logging
import os
import pathlib
import time
import typing
from testsuite import types
from testsuite.utils import traceback
from . import shell, utils
logger = logging.getLogger(__name__)
_TESTSUITE_LIB_UTILS = pathlib.Path(__file__).parent.joinpath('scripts/utils.sh')
COMMAND_START = 'start'
COMMAND_STOP = 'stop'

class BaseError(Exception):
    pass

class ServiceFailedToStartError(BaseError):
    pass
__tracebackhide__ = traceback.hide(BaseError)

class ScriptService:

    def __init__(self, *, service_name: str, script_path: str, working_dir: str, check_host: str='localhost', check_ports: list[int], environment: dict[str, str] | None=None, prestart_hook: typing.Callable | None=None, start_timeout: float=2.0) -> None:
        self._service_name = service_name
        self._script_path = script_path
        self._environment = environment
        self._check_host = check_host
        self._check_ports = check_ports
        self._prestart_hook = prestart_hook
        self._start_timeout = start_timeout
        self._started_mark = StartedMark(working_dir)

    def ensure_started(self, *, verbose: int) -> None:
        pass

    def stop(self, *, verbose: int) -> None:
        pass

    def is_running(self) -> bool:
        pass

    def _command(self, command: str, verbose: int) -> None:
        pass

    def _wait_for_ports(self) -> bool:
        pass

class StartedMark:

    def __init__(self, working_dir: types.PathOrStr) -> None:
        self._path = pathlib.Path(working_dir) / '.started'

    def create(self) -> None:
        pass

    def delete(self) -> None:
        pass

    def exists(self) -> bool:
        pass
