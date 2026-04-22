import pytest
from testsuite.utils import colors

class ColorsPlugin:

    def __init__(self, config):
        self._colors_enabled = colors.should_enable_color(config)

    @pytest.fixture(scope='session')
    def testsuite_colors_enabled(self) -> bool:
        pass

def pytest_configure(config):
    pass
