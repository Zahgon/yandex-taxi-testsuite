import pathlib
import typing
from testsuite.environment import service, utils
from . import classes
DEFAULT_CLICKHOUSE_TCP_PORT = 17123
DEFAULT_CLICKHOUSE_HTTP_PORT = 17124
SERVICE_SCRIPT_PATH = pathlib.Path(__file__).parent.joinpath('scripts/service-clickhouse')

class ServiceSettings(typing.NamedTuple):
    tcp_port: int
    http_port: int

    def get_connection_info(self) -> classes.ConnectionInfo:
        pass

def create_clickhouse_service(service_name, working_dir, settings: ServiceSettings | None=None, env: dict[str, str] | None=None):
    pass

def get_service_settings():
    pass
