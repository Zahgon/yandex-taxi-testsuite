import json
import pathlib
import typing
import pytest
from testsuite import types
from testsuite.utils import cached_property, json_util, traceback, yaml_util

class BaseError(Exception):
    """Base class for errors from this module."""

class UnsupportedFileModeError(BaseError):
    """Unsupported file open mode passed."""

class LoadJsonError(BaseError):
    """Json file load or parse failure error."""

class LoadYamlError(BaseError):
    """Yaml file load or parse failure error."""
__tracebackhide__ = traceback.hide(BaseError, FileNotFoundError)

class GetSearchPathsFixture(typing.Protocol):
    """Generates sequence of paths for static files."""

    def __call__(self, filename: types.PathOrStr) -> typing.Iterator[pathlib.Path]:
        ...

class SearchPathFixture(typing.Protocol):

    def __call__(self, filename: types.PathOrStr, directory: bool=False) -> typing.Iterator[pathlib.Path]:
        ...

class GetFilePathFixture(typing.Protocol):
    """Returns path to static regular file."""

    def __call__(self, filename: types.PathOrStr, *, missing_ok=False) -> pathlib.Path | None:
        ...

class GetDirectoryPathFixture(typing.Protocol):
    """Returns path to static directory."""

    def __call__(self, filename: types.PathOrStr, *, missing_ok=False) -> pathlib.Path | None:
        ...

class OpenFileFixture(typing.Protocol):
    """Open static file by name.

    Only read-only open modes are supported.

    Example:

    .. code-block:: python

        def test_foo(open_file):
            with open_file('foo') as fp:
                ...
    """

    def __call__(self, filename: types.PathOrStr, mode='r', buffering=-1, encoding='utf-8', errors=None) -> typing.IO:
        ...

class LoadFixture(typing.Protocol):
    """Load file from static directory.

    Example:

    .. code-block:: python

        def test_something(load):
            data = load('filename')

    :return: :py:class:`LoadFixture` callable instance.
    """

    def __call__(self, filename: types.PathOrStr, encoding='utf-8', errors=None, *, missing_ok=False) -> bytes | str | None:
        ...

class LoadBinaryFixture(typing.Protocol):
    """Load binary data from static directory.

    Example:

    .. code-block:: python

        def test_something(load_binary):
            bytes_data = load_binary('data.bin')
    """

    def __call__(self, filename: types.PathOrStr) -> bytes:
        ...

class JsonLoadsFixture(typing.Protocol):
    """Load json doc from string.

    Json loader runs ``json_util.loads(data, ..., *args, **kwargs)`` hooks.
    It does:
    * bson.json_util.object_hook()
    * mockserver substitution

    Example:

    .. code-block:: python

        def test_something(json_loads):
            json_obj = json_loads('{"key": "value"}')
    """

    def __call__(self, content, *args, **kwargs) -> typing.Any:
        ...

class LoadJsonFixture(typing.Protocol):
    """Load json doc from static directory.

    Json loader runs ``json_util.loads(data, ..., *args, **kwargs)`` hooks.
    It does:
    * bson.json_util.object_hook()
    * mockserver substitution

    Example:

    .. code-block:: python

        def test_something(load_json):
            json_obj = load_json('filename.json')
    """

    def __call__(self, filename: types.PathOrStr, *args, missing_ok=False, missing=None, **kwargs) -> typing.Any:
        ...

class LoadYamlFixture(typing.Protocol):
    """Load yaml doc from static directory.

    .. code-block:: python

        def test_something(load_yaml):
            yaml_obj = load_yaml('filename.yaml')
    """

    def __call__(self, filename: types.PathOrStr, *args, **kwargs) -> typing.Any:
        ...
_MODES_WHITELIST = frozenset(['r', 'rt', 'rb'])

@pytest.fixture
def get_search_pathes(_search_directories_existing: tuple[pathlib.Path, ...], _path_entries_cache: typing.Callable) -> GetSearchPathsFixture:
    pass

@pytest.fixture
def get_search_paths(get_search_pathes):
    pass

@pytest.fixture
def search_path(get_search_paths: GetSearchPathsFixture) -> SearchPathFixture:
    pass

@pytest.fixture
def get_file_path(search_path: SearchPathFixture, _testsuite_file_not_found_error) -> GetFilePathFixture:
    pass

@pytest.fixture
def get_directory_path(search_path: SearchPathFixture, _testsuite_file_not_found_error) -> GetDirectoryPathFixture:
    pass

@pytest.fixture
def _testsuite_file_not_found_error(_search_directories_existing):
    pass

@pytest.fixture
def open_file(get_file_path: GetFilePathFixture) -> OpenFileFixture:
    pass

@pytest.fixture
def load(get_file_path: GetFilePathFixture) -> LoadFixture:
    pass

@pytest.fixture
def load_binary(get_file_path: GetFilePathFixture) -> LoadBinaryFixture:
    pass

@pytest.fixture
def json_loads(object_hook, load_json_defaults) -> JsonLoadsFixture:
    pass

@pytest.fixture
def load_json(load: LoadFixture, json_loads: JsonLoadsFixture) -> LoadJsonFixture:
    pass

@pytest.fixture
def load_yaml(load: LoadFixture) -> LoadYamlFixture:
    pass
FilePathsCache = dict[pathlib.Path, list[pathlib.Path]]

def pytest_configure(config):
    pass

@pytest.fixture
def static_dir(testsuite_request_directory) -> pathlib.Path:
    """Static directory related to test path.

    Returns static directory relative to test file, e.g.::

       |- tests/
          |- static/ <-- base static directory for test_foo.py
          |- test_foo.py

    """
    pass

@pytest.fixture
def initial_data_path() -> tuple[pathlib.Path, ...]:
    """Use this fixture to override base static search path.

    .. code-block:: python

     @pytest.fixture
     def initial_data_path():
         return (
             pathlib.Path(PROJECT_ROOT) / 'tests/static',
             pathlib.Path(PROJECT_ROOT) / 'static',
         )
    """
    pass

@pytest.fixture
def get_all_static_file_paths(static_dir: pathlib.Path, _file_paths_cache: FilePathsCache):
    pass

@pytest.fixture
def object_substitute(object_hook):
    """Perform object substitution as in load_json."""
    pass

@pytest.fixture(scope='session')
def testsuite_get_source_path():
    pass

@pytest.fixture(scope='session')
def testsuite_get_source_directory(testsuite_get_source_path):
    pass

@pytest.fixture
def testsuite_request_path(request, testsuite_get_source_path) -> pathlib.Path:
    pass

@pytest.fixture
def testsuite_request_directory(testsuite_request_path) -> pathlib.Path:
    pass

@pytest.fixture(scope='session')
def worker_id(request) -> str:
    pass

@pytest.fixture(scope='session')
def _file_paths_cache() -> FilePathsCache:
    pass

@pytest.fixture
def _search_directories(request, static_dir: pathlib.Path, initial_data_path: tuple[pathlib.Path, ...], testsuite_request_path, _path_entries_cache) -> tuple[pathlib.Path, ...]:
    pass

@pytest.fixture
def _search_directories_existing(_search_directories):
    pass

@pytest.fixture(scope='session')
def load_json_defaults():
    pass

@pytest.fixture(scope='session')
def _cached_stat_path():
    pass

@pytest.fixture(scope='session')
def _path_entries_cache(_cached_stat_path):
    pass
