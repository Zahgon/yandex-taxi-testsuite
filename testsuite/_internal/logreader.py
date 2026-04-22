import pathlib
import sys
import threading
import typing

class LogFile:

    def __init__(self, path: pathlib.Path):
        self._path = path
        self._position = 0

    @property
    def path(self):
        pass

    @property
    def position(self):
        pass

    def filesize(self) -> int:
        pass

    def update_position(self):
        pass

    def readlines(self, eof_handler: typing.Callable[[], bool] | None=None, limit_position: bool=False):
        pass

class LiveLogHandler:

    def __init__(self, *, delay: float=0.05):
        self._threads = {}
        self._exiting = False
        self._delay = delay
        self._condition = threading.Condition()

    def register_logfile(self, path: pathlib.Path, *, formatter):
        pass

    def join(self, timeout: float=10):
        pass

    def _logreader_thread(self, path: pathlib.Path, formatter):
        pass

    def _write_logline(self, line: str):
        pass

    def _eof_handler(self) -> bool:
        pass

def _raw_line_reader(path: pathlib.Path, position: int=0, eof_handler: typing.Callable[[], bool] | None=None) -> typing.Iterator[tuple[bytes, int]]:
    pass
