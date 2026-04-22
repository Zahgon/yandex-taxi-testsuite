import pathlib
import typing
from testsuite.environment import service, utils
from . import connection
DEFAULT_CONFIG_SERVER_PORT = 27118
DEFAULT_MONGOS_PORT = 27217
DEFAULT_SHARD_PORT = 27119
DEFAULT_RS_INSTANCE_COUNT = 1
SERVICE_SCRIPT_PATH = pathlib.Path(__file__).parent.joinpath('scripts/service-mongo')

class ServiceSettings(typing.NamedTuple):
    config_server_port: int
    mongos_port: int
    shard_port: int
    rs_instance_count: int

    def get_connection_info(self) -> connection.ConnectionInfo:
        pass

def create_mongo_service(service_name, working_dir, settings: ServiceSettings | None=None, env: dict[str, str] | None=None):
    pass

def get_service_settings():
    pass
