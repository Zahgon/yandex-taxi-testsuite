import dataclasses
import getpass
import pathlib
import typing
from testsuite.utils import yaml_util
from . import service, utils
CONFIG_PATH = pathlib.Path('~/.config/yasuite/env.yaml')
DEFAULT_WORKER_ID = 'master'

class BaseError(Exception):
    """Base class for exceptions of this module."""

class AlreadyStarted(BaseError):
    pass

class ServiceUnknown(BaseError):
    pass

@dataclasses.dataclass(frozen=True)
class Config:
    env_dir: pathlib.Path
    worker_id: str
    reuse_services: bool
    verbose: int

class Environment:
    config: Config
    _services: dict[str, service.ScriptService]
    _services_start_order: list[str]
    _env: dict[str, str] | None
    _service_factories: dict[str, typing.Callable]

    def __init__(self, config: Config, env: dict[str, str] | None=None) -> None:
        self.config = config
        self._services = {}
        self._services_start_order = []
        self._env = env
        self._service_factories = {}

    def register_service(self, name: str, factory) -> None:
        pass

    def ensure_started(self, service_name: str, **kwargs) -> None:
        pass

    def start_service(self, service_name: str, **kwargs) -> None:
        pass

    def stop_service(self, service_name: str) -> None:
        pass

    def close(self) -> None:
        pass

    def _create_service(self, service_name: str, **kwargs) -> service.ScriptService:
        pass

    def _get_working_dir_for(self, service_name: str) -> pathlib.Path:
        pass

class TestsuiteEnvironment(Environment):

    def __init__(self, config: Config) -> None:
        if config.worker_id == DEFAULT_WORKER_ID:
            worker_suffix = '_' + config.worker_id
        else:
            worker_suffix = ''
        super().__init__(config=config, env={'WORKER_SUFFIX': worker_suffix})

def load_environment_config(*, env_dir: pathlib.Path | None=None, worker_id: str=DEFAULT_WORKER_ID, reuse_services: bool=False, verbose: int=0) -> Config:
    pass

def _load_config():
    pass
