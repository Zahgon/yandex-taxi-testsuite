import pathlib
import typing
from testsuite.environment import service, utils
from . import classes
DEFAULT_RABBITMQ_TCP_PORT = 8672
DEFAULT_RABBITMQ_EPMD_PORT = 8673
SERVICE_SCRIPT_PATH = pathlib.Path(__file__).parent.joinpath('scripts/service-rabbitmq')

class ServiceSettings(typing.NamedTuple):
    tcp_port: int
    epmd_port: int

    def get_connection_info(self) -> classes.ConnectionInfo:
        pass

def create_rabbitmq_service(service_name, working_dir, settings: ServiceSettings | None=None, env: dict[str, str] | None=None):
    pass

def get_service_settings() -> ServiceSettings:
    pass
