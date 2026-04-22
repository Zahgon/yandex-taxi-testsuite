import contextlib
import enum
import io
import logging
import typing
import pytest
from testsuite._internal import compare_transform

class AssertMode(enum.Enum):
    DEFAULT = 'default'
    COMBINE = 'combine'
    ANALYZE = 'analyze'

class AssertionPlugin:

    def __init__(self, assert_mode, transform_mode):
        self._disabled = False
        self._assert_mode = assert_mode
        self._transform_mode = transform_mode

    @contextlib.contextmanager
    def disabled(self):
        pass

    def pytest_assertrepr_compare(self, config: pytest.Config, op: str, left: typing.Any, right: typing.Any):
        pass

def pytest_configure(config: pytest.Config):
    pass

def pytest_addoption(parser: pytest.Parser):
    """
    :param parser: pytest's argument parser
    """
    pass
