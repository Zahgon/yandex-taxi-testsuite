import pathlib
import typing
from testsuite.environment import service, utils
from . import connection
DEFAULT_PORT = 15433
PLUGIN_DIR = pathlib.Path(__file__).parent
CONFIGS_DIR = PLUGIN_DIR.joinpath('configs')
SCRIPTS_DIR = PLUGIN_DIR.joinpath('scripts')

class ServiceSettings(typing.NamedTuple):
    port: int

    def get_conninfo(self) -> connection.PgConnectionInfo:
        pass

def get_service_settings():
    pass

def create_pgsql_service(service_name, working_dir, settings: ServiceSettings | None=None, env=None):
    pass
