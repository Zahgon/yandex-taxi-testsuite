import os
import pathlib
from testsuite.environment import service, utils
from . import classes
DEFAULT_SERVER_HOST = 'localhost'
DEFAULT_SERVER_PORT = 9099
DEFAULT_CONTROLLER_PORT = 9100
PLUGIN_DIR = pathlib.Path(__file__).parent
SERVICE_SCRIPT_DIR = PLUGIN_DIR.joinpath('scripts/service-kafka')

def _stringify_start_topics(start_topics: dict[str, int]) -> str:
    pass

def _parse_custom_topics(custom_topics: str) -> dict[str, int]:
    pass

def try_get_custom_topics() -> dict[str, int]:
    pass

def create_kafka_service(service_name: str, working_dir: str, settings: classes.ServiceSettings | None=None, env: dict[str, str] | None=None):
    pass

def get_service_settings(custom_start_topics: dict[str, int]={}) -> classes.ServiceSettings:
    pass
