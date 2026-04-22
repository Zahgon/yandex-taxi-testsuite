import contextlib
import inspect
import itertools
import signal
import subprocess
import typing
import warnings
from collections.abc import AsyncGenerator, Callable, Sequence
from typing import Any, AsyncContextManager
import aiohttp
import pytest
from testsuite import types
from testsuite._internal import fixture_types
from . import service_client, service_daemon
from .classes import DaemonInstance
from .spawn import __tracebackhide__
SHUTDOWN_SIGNALS = {'SIGINT': signal.SIGINT, 'SIGKILL': signal.SIGKILL, 'SIGQUIT': signal.SIGQUIT, 'SIGTERM': signal.SIGTERM}

class _DaemonScope:

    def __init__(self, name: str, spawn: Callable, *, multiple: bool=False) -> None:
        self.name = name
        self._spawn = spawn
        self.multiple = multiple

    async def spawn(self) -> 'DaemonInstance':
        pass

class _DaemonStore:
    _cells: dict[str, tuple[_DaemonScope, DaemonInstance]]

    def __init__(self) -> None:
        self._cells = {}

    async def aclose(self, skip_multiple=False) -> None:
        pass

    @contextlib.asynccontextmanager
    async def scope(self, name, spawn, *, multiple: bool=False) -> AsyncGenerator[_DaemonScope, None]:
        """
        Creates new scope evicting previous daemon.

        :param name: scope identifier.
        :param spawn: spawner instance.
        :param multiple: do not fail when this scope is requested with others.
        """
        pass

    async def request(self, scope: _DaemonScope) -> DaemonInstance:
        pass

    def has_running_daemons(self) -> bool:
        pass

    async def _cleanup_cell(self, name):
        pass

    async def _close_daemon(self, daemon: DaemonInstance):
        pass

class EnsureDaemonStartedFixture(typing.Protocol):
    """Fixture that starts requested service."""

    async def __call__(self, scope: _DaemonScope) -> DaemonInstance:
        ...

class ServiceSpawnerFactory(typing.Protocol):

    def __call__(self, args: Sequence[str], *, base_command: Sequence[str] | None=None, env: dict[str, str] | None=None, poll_retries: int=service_daemon.POLL_RETRIES, ping_url: str | None=None, ping_request_timeout: float=service_daemon.PING_REQUEST_TIMEOUT, ping_response_codes: tuple[int]=service_daemon.PING_RESPONSE_CODES, health_check: service_daemon.HealthCheckType | None=None, subprocess_spawner: Callable[..., subprocess.Popen] | None=None, subprocess_options: dict[str, Any] | None=None, setup_service: Callable[[subprocess.Popen], None] | None=None, shutdown_signal: int | None=None, stdout_handler=None, stderr_handler=None):
        """Creates service spawner asynccontextmanager factory.

        :param args: command arguments
        :param base_command: Arguments to be prepended to ``args``.
        :param env: Environment variables dictionary.
        :param poll_retries: Number of tries for service health check
        :param ping_url: service health check url, service is considered up
            when 200 received.
        :param ping_request_timeout: Timeout for ping_url request
        :param ping_response_codes: HTTP resopnse codes tuple meaning that
            service is up and running.
        :param health_check: Async function to check service is running.
        :param subprocess_spawner: callable with `subprocess.Popen` interface.
        :param subprocess_options: Custom subprocess options.
        :param setup_service: Function to be called right after service
            is started.
        :param shutdown_signal: Signal used to stop running services.
        :returns: Return asynccontextmanager factory that might be used
                  within ``register_daemon_scope`` fixture.
        """

class CreateDaemonScope(typing.Protocol):
    """Create daemon scope for daemon with command to start."""

    def __call__(self, *, args: Sequence[str], ping_url: str | None=None, name: str | None=None, base_command: Sequence | None=None, env: dict[str, str] | None=None, poll_retries: int=service_daemon.POLL_RETRIES, ping_request_timeout: float=service_daemon.PING_REQUEST_TIMEOUT, ping_response_codes: tuple[int]=service_daemon.PING_RESPONSE_CODES, health_check: service_daemon.HealthCheckType | None=None, subprocess_options: dict[str, Any] | None=None, setup_service: Callable[[subprocess.Popen], None] | None=None, shutdown_signal: int | None=None, stdout_handler=None, stderr_handler=None, multiple=True) -> AsyncContextManager[_DaemonScope]:
        """
        :param args: command arguments
        :param base_command: Arguments to be prepended to ``args``.
        :param env: Environment variables dictionary.
        :param poll_retries: Number of tries for service health check
        :param ping_url: service health check url, service is considered up
            when 200 received.
        :param ping_request_timeout: Timeout for ping_url request
        :param ping_response_codes: HTTP resopnse codes tuple meaning that
            service is up and running.
        :param health_check: Async function to check service is running.
        :param subprocess_options: Custom subprocess options.
        :param setup_service: Function to be called right after service
            is started.
        :param shutdown_signal: Signal used to stop running services.
        :param multiple: do not fail when this scope is requested with others.
        :returns: Returns internal daemon scope instance to be used with
            ``ensure_daemon_started`` fixture.
        """

class CreateServiceClientFixture(typing.Protocol):
    """Creates service client instance.

    Example:

    .. code-block:: python

        def my_client(create_service_client):
            return create_service_client('http://localhost:9999/')
    """

    def __call__(self, base_url: str, *, client_class=service_client.Client, **kwargs):
        """
        :param base_url: base url for http client
        :param client_class: client class to use
        :returns: ``client_class`` instance
        """

@pytest.fixture
def ensure_daemon_started(_global_daemon_store: _DaemonStore, _testsuite_suspend_capture, pytestconfig) -> EnsureDaemonStartedFixture:
    pass

@pytest.fixture(scope='session')
def service_spawner_factory(pytestconfig: Any, service_client_session_factory: Any, wait_service_started: Any) -> ServiceSpawnerFactory:
    pass

@pytest.fixture(scope='session')
def service_spawner(service_spawner_factory):
    pass

@pytest.fixture(scope='session')
def create_daemon_scope(_global_daemon_store: _DaemonStore, service_spawner_factory: ServiceSpawnerFactory) -> CreateDaemonScope:
    """Create daemon scope for daemon with command to start."""
    pass

@pytest.fixture
def create_service_client(service_client_default_headers: dict[str, str], service_client_options: dict[str, Any]) -> CreateServiceClientFixture:
    pass

@pytest.fixture(scope='session')
def wait_service_started(pytestconfig, service_client_session_factory):
    pass

def pytest_addoption(parser):
    pass

@pytest.fixture(scope='session')
def register_daemon_scope(_global_daemon_store: _DaemonStore):
    """Context manager that registers service process session.

    Yields daemon scope instance.

    :param name: service name
    :spawn spawn: asynccontextmanager service factory
    """
    pass

@pytest.fixture(scope='session')
def service_client_session_factory() -> service_daemon.ClientSessionFactory:
    pass

@pytest.fixture
async def service_client_session(service_client_session_factory) -> types.AsyncYieldFixture[aiohttp.ClientSession]:
    pass

@pytest.fixture
def service_client_default_headers() -> dict[str, str]:
    """Default service client headers.

    Fill free to override in your conftest.py
    """
    pass

@pytest.fixture
def service_client_options(pytestconfig, service_client_session: aiohttp.ClientSession, mockserver: fixture_types.MockserverFixture) -> types.YieldFixture[dict[str, Any]]:
    """Returns service client options dictionary."""
    pass

@pytest.fixture(scope='session')
async def _global_daemon_store():
    pass

@pytest.fixture(scope='session')
def _testsuite_suspend_capture(pytestconfig):
    pass

def _build_command_args(args: Sequence, base_command: Sequence | None) -> tuple[str, ...]:
    pass
