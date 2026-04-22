import asyncio
import contextlib
import os
import signal
import subprocess
import time
from collections.abc import AsyncGenerator, Awaitable, Callable, Sequence
from typing import AsyncGenerator, Awaitable, Callable
import aiohttp
from testsuite.daemons import spawn
from testsuite.daemons.spawn import __tracebackhide__
POLL_RETRIES = 2000
PING_REQUEST_TIMEOUT = 1.0
PING_RESPONSE_CODES = (200,)
HealthCheckType = Callable[..., Awaitable[bool]]
ClientSessionFactory = Callable[..., aiohttp.ClientSession]

@contextlib.asynccontextmanager
async def start(args: Sequence[str], *, health_check: HealthCheckType, session_factory: ClientSessionFactory=aiohttp.ClientSession, env: dict[str, str] | None=None, shutdown_signal: int=signal.SIGINT, shutdown_timeout: float=120, poll_retries: int=POLL_RETRIES, subprocess_options=None, setup_service=None, subprocess_spawner=None, stdout_handler=None, stderr_handler=None) -> AsyncGenerator[subprocess.Popen | None, None]:
    pass

async def service_wait(args: Sequence[str], *, health_check: HealthCheckType, session_factory: ClientSessionFactory=aiohttp.ClientSession, reporter):
    pass

@contextlib.asynccontextmanager
async def start_dummy_process():
    pass

def make_health_check(*, health_check: HealthCheckType | None=None, ping_url: str | None, ping_request_timeout: float=PING_REQUEST_TIMEOUT, ping_response_codes: tuple[int]=PING_RESPONSE_CODES) -> HealthCheckType:
    pass

async def _run_health_check(health_check: HealthCheckType, *, session: aiohttp.ClientSession, process: subprocess.Popen | None, sleep: float=0.05):
    pass

def _make_ping_health_check(*, ping_url: str, ping_request_timeout: float, ping_response_codes: tuple[int]) -> HealthCheckType:
    pass

async def _service_wait(process: subprocess.Popen | None, *, poll_retries: int, health_check: HealthCheckType, session: aiohttp.ClientSession) -> bool:
    pass

def _prepare_env(*envs: dict[str, str] | None) -> dict[str, str]:
    pass

@contextlib.asynccontextmanager
async def _service_daemon(args: Sequence[str], *, env: dict[str, str] | None, shutdown_signal: int, shutdown_timeout: float, poll_retries: int, subprocess_options=None, setup_service=None, subprocess_spawner=None, health_check, session: aiohttp.ClientSession, stdout_handler=None, stderr_handler=None) -> AsyncGenerator[subprocess.Popen, None]:
    pass
