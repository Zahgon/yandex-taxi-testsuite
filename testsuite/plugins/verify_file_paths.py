import collections
import pytest

@pytest.fixture
def verify_file_paths(static_dir, _verified_static_dirs, get_all_static_file_paths):
    pass

@pytest.fixture(scope='session')
def _verified_static_dirs():
    pass
