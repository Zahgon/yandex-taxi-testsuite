import asyncio
import pytest

def pytest_configure(config):
    pass

@pytest.fixture(scope='session')
def event_loop():
    """
    Overrides pytest-asyncio internal `event_loop` fixture. Should not be
    used explicitly.

    Required for compatibility with pytest-asyncio 0.21.x
    """
    pass
