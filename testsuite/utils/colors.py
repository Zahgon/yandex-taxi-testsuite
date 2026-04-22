import sys

class Colors:
    BLACK = '\x1b[30m'
    RED = '\x1b[31m'
    GREEN = '\x1b[32m'
    YELLOW = '\x1b[33m'
    BLUE = '\x1b[34m'
    GRAY = '\x1b[37m'
    DARK_GRAY = '\x1b[37m'
    BRIGHT_RED = '\x1b[91m'
    BRIGHT_GREEN = '\x1b[92m'
    BRIGHT_YELLOW = '\x1b[93m'
    DEFAULT = '\x1b[0m'
    DEFAULT_BG = '\x1b[49m'
    BG_BLACK = '\x1b[40m'

def should_enable_color(pytestconfig) -> bool:
    pass
