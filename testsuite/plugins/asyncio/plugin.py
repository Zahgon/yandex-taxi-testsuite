import pytest

@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    pass

def pytest_collection_modifyitems(items):
    """Force tests to use session asyncio loop."""
    pass
