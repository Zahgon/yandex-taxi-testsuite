import os
import pathlib
import socket
import typing
import warnings
from testsuite.environment import service, utils
from . import genredis
DEFAULT_MASTER_PORTS = (16379, 16389)
DEFAULT_SENTINEL_PORT = 26379
DEFAULT_SLAVE_PORTS = (16380, 16390, 16381)
DEFAULT_CLUSTER_PORTS = (17380, 17381, 17382, 17383, 17384, 17385)
DEFAULT_CLUSTER_REPLICAS = 1
DEFAULT_STANDALONE_PORT = 7000
SERVICE_SCRIPT_PATH = pathlib.Path(__file__).parent.joinpath('scripts/service-redis')
CLUSTER_SERVICE_SCRIPT_PATH = pathlib.Path(__file__).parent.joinpath('scripts/service-cluster-redis')
STANDALONE_SERVICE_SCRIPT_PATH = pathlib.Path(__file__).parent.joinpath('scripts/service-standalone-redis')

class BaseError(Exception):
    pass

class NotEnoughPorts(BaseError):
    pass

class ServiceSettings(typing.NamedTuple):
    host: str
    master_ports: tuple[int, ...]
    sentinel_port: int
    slave_ports: tuple[int, ...]

    def validate(self):
        pass

class ClusterServiceSettings(typing.NamedTuple):
    host: str
    cluster_ports: tuple[int, ...]
    cluster_replicas: int

    def validate(self):
        pass

class StandaloneServiceSettings(typing.NamedTuple):
    host: str
    port: int

def get_service_settings():
    pass

def get_cluster_service_settings():
    pass

def get_standalone_service_settings():
    pass

def create_redis_service(service_name, working_dir, settings: ServiceSettings | None=None, env=None):
    pass

def create_cluster_redis_service(service_name, working_dir, settings: ClusterServiceSettings | None=None, env=None):
    pass

def create_standalone_redis_service(service_name, working_dir, settings: StandaloneServiceSettings | None=None, env=None):
    pass

def _get_hostname():
    pass

def _resolve_hostname(hostname: str) -> str:
    pass
