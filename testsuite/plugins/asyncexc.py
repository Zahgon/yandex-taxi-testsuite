"""
Async exceptions handler.

Handle excpetions in background coroutines.
"""
import pytest
from testsuite.utils import traceback

class BaseError(Exception):
    pass

class BackgroundExceptionError(BaseError):
    pass
__tracebackhide__ = traceback.hide(BaseError)

@pytest.fixture
def _asyncexc():
    pass

@pytest.fixture
def asyncexc_append(_asyncexc):
    """Register background exception."""
    pass

@pytest.fixture
def asyncexc_check(_asyncexc):
    """Raise in case there are background exceptions."""
    pass

def _raise_if_any(errors):
    pass

def _clear_and_copy(errors):
    pass
