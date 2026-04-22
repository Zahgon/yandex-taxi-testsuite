import os
import socket
import time
DOCKERTEST_WORKER = os.getenv('DOCKERTEST_WORKER', '')

class BaseError(Exception):
    pass

class RootUserForbiddenError(BaseError):
    pass

class EnvironmentVariableError(BaseError):
    pass

def test_tcp_connection(host: str, port: int, timeout: float=1.0) -> bool:
    pass

def wait_tcp_connection(host: str, port: int, timeout: float=1.0) -> bool:
    pass

def ensure_non_root_user() -> None:
    pass

def getenv_str(key: str, default: str) -> str:
    pass

def getenv_int(key: str, default: int) -> int:
    pass

def getenv_float(key: str, default: float) -> float:
    pass

def getenv_ints(key: str, default: tuple[int, ...]) -> tuple[int, ...]:
    pass
