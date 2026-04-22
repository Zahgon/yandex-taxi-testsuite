import pathlib
import urllib.parse
from testsuite.environment import service, utils
from . import classes
DEFAULT_HOSTNAME = 'localhost'
DEFAULT_PORT = 13307
PLUGIN_DIR = pathlib.Path(__file__).parent
SCRIPTS_DIR = PLUGIN_DIR.joinpath('scripts')

def create_service(service_name: str, working_dir: str, settings: classes.ServiceSettings | None=None, env: dict[str, str] | None=None):
    pass

def get_service_settings():
    pass

def parse_connection_url(url: str):
    pass
