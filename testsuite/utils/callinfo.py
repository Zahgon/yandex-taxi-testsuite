import asyncio
import inspect
import typing
from testsuite.utils import cached_property, traceback

class BaseError(Exception):
    """Base exception class for this module."""

class CallQueueError(BaseError):
    pass

class CallQueueEmptyError(CallQueueError):
    """Call queue is empty error."""

class CallQueueTimeoutError(CallQueueError):
    """Timed out while waiting for call."""
CheckerType = typing.Callable[[str], None]
__tracebackhide__ = traceback.hide(BaseError)

class AsyncCallQueue:
    """Function wrapper that puts information about function call into async
    queue.

    This class provides methods to wait/check function underlying function
    calls.
    """

    def __init__(self, func: typing.Callable, *, name=None, checker: CheckerType | None=None):
        self._func = func
        self._name = name or func.__name__
        self._checker = checker

    @property
    def func(self):
        """Returns underlying function."""
        return self._func

    @cached_property
    def _is_coro(self):
        pass

    @cached_property
    def _get_callinfo(self):
        pass

    @cached_property
    def _queue(self) -> asyncio.Queue:
        pass

    def __repr__(self):
        return f'<AsyncCallQueue: for {self._func!r}>'

    async def __call__(self, *args, **kwargs):
        """Call underlying function."""
        try:
            if self._is_coro:
                return await self._func(*args, **kwargs)
            return self._func(*args, **kwargs)
        finally:
            await self._queue.put((args, kwargs))

    def flush(self) -> None:
        """Clear call queue."""
        pass

    @property
    def has_calls(self) -> bool:
        """Returns ``True`` if call queue is not empty."""
        pass

    @property
    def times_called(self) -> int:
        """Returns call queue length."""
        pass

    def next_call(self) -> dict:
        """Pops call from queue and return its arguments dict.

        Raises ``CallQueueError`` if queue is empty
        """
        pass

    async def wait_call(self, timeout=10.0) -> dict:
        """Wait for fucntion to be called. Pops call from queue. Blocks if
        it's empty.

        :param timeout: timeout in seconds

        Raises ``CallQueueTimeoutError`` if queue is empty for ``timeout``
        seconds.
        """
        pass

    def _check_callqueue(self, caller):
        pass

def getfullargspec(func):
    pass

def callinfo(func):
    pass

def acallqueue(func: typing.Callable, *, checker: CheckerType | None=None) -> AsyncCallQueue:
    """Turn function into async call queue.

    :param func: async or sync callable, can be decorated with @staticmethod
    :param checker: optional function to check whether or not operation on
        callqueue is possible
    """
    pass
