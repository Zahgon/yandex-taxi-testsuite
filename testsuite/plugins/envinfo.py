import socket
import subprocess
import sys
from testsuite.utils import subprocess_helper
BASE_BRANCH = 'develop'
UPSTREAM_REMOTES = ('upstream', 'origin')

def pytest_addoption(parser):
    pass

def pytest_report_header(config):
    pass

def get_vcs_info() -> list[str]:
    pass

def git_is_clean() -> bool:
    pass

def git_merge_base() -> str | None:
    """Try to guess merge base for current commit."""
    pass
