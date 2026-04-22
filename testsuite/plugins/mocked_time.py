import datetime
import dateutil.parser
import pytest
from testsuite import utils
from testsuite.utils import traceback
MOCK_TIME_DISABLED_MESSAGE = 'Mock time is disabled. Use @pytest.mark.now to enable mock time for a particular test'
UTC = datetime.timezone.utc

class BaseError(Exception):
    """Base class for errors in this module"""

class DisabledUsageError(BaseError):
    """Raised when attempting to use a disabled feature"""
__tracebackhide__ = traceback.hide(BaseError)

class MockedTime:

    def __init__(self, time: datetime.datetime, *, is_enabled: bool):
        self._now: datetime.datetime = time
        self._is_enabled = is_enabled

    def sleep(self, delta: float) -> None:
        """Increase mock time value

        :param delta: increase value in seconds
        """
        pass

    def now(self, tz: datetime.tzinfo | None=None) -> datetime.datetime:
        """:returns: current value of mock time"""
        pass

    def set(self, time: datetime.datetime):
        """Set mock time value"""
        pass

    @property
    def is_enabled(self) -> bool:
        pass

def pytest_addoption(parser):
    pass

def pytest_configure(config):
    pass

def pytest_register_object_hooks():
    pass

def pytest_servicetest_modifyitem(session, item):
    pass

@pytest.fixture
def mocked_time(_mocked_time_enabled: bool, now: datetime.datetime) -> MockedTime:
    """:returns: :py:class:`MockedTime`"""
    pass

@pytest.fixture
def now(request) -> datetime.datetime:
    pass

@pytest.fixture
def _mocked_time_enabled(request, pytestconfig) -> bool:
    pass

@pytest.fixture
def _date_diff_hook(now: datetime.datetime):
    pass

def _time_delta_hook(doc: dict):
    pass
