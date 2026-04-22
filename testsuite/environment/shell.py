import contextlib
import logging
import subprocess
import threading
from testsuite.utils import traceback
logger = logging.getLogger(__name__)

class BaseError(Exception):
    pass

class SubprocessFailed(BaseError):
    pass
__tracebackhide__ = traceback.hide(BaseError)

def execute(args, *, env=None, verbose: int, command_alias: str) -> None:
    pass
