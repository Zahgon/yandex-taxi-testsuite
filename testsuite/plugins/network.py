import platform
import socket
import typing
import pytest

class BaseError(Exception):
    """Base class for errors from this module."""

class NoEnabledPorts(BaseError):
    """Raised if there are not free ports for worker"""

@pytest.fixture(scope='session')
def get_free_port(_get_free_port_sock_storing, _get_free_port_range_based) -> typing.Callable[[], int]:
    """
    Returns an ephemeral TCP port that is free for IPv4 and for IPv6.
    """
    pass

@pytest.fixture(scope='session')
def _get_free_port_sock_storing(_testsuite_default_af, _testsuite_socket_cleanup) -> typing.Callable[[], int]:
    pass

@pytest.fixture(scope='session')
def _get_free_port_range_based(_testsuite_default_af) -> typing.Callable[[], int]:
    pass

@pytest.fixture(scope='session')
def _testsuite_socket_cleanup():
    pass

@pytest.fixture(scope='session')
def _testsuite_default_af():
    pass

def _is_port_free(port_num: int, family: int, address: str) -> bool:
    pass

def _is_af_available(family: int, address: str):
    pass

def _get_inet_families():
    pass
