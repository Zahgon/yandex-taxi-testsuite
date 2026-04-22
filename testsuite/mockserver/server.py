import asyncio
import contextlib
import itertools
import logging
import pathlib
import re
import ssl
import time
import typing
import urllib.parse
import warnings
import aiohttp.web
import yarl
from testsuite import utils
from testsuite.tracing import TraceidManager
from testsuite.utils import cached_property, callinfo, http, url_util
from testsuite.utils import net as net_utils
from . import classes, exceptions, magicargs
from .exceptions import __tracebackhide__
DEFAULT_TRACE_ID_HEADER = 'X-YaTraceId'
DEFAULT_SPAN_ID_HEADER = 'X-YaSpanId'
REQUEST_FROM_ANOTHER_TEST_ERROR = 'Internal error: request is from other test'
_SUPPORTED_ERRORS_HEADER = 'X-Testsuite-Supported-Errors'
_ERROR_HEADER = 'X-Testsuite-Error'
_LOGGER_HEADERS = (('X-YaTraceId', 'trace_id'), ('X-YaSpanId', 'span_id'), ('X-YaRequestId', 'link'))
logger = logging.getLogger(__name__)
RouteParams = dict[str, str]

class MockserverRequest(aiohttp.web.BaseRequest):

    def __init__(self, message, *args, **kwargs):
        super().__init__(message, *args, **kwargs)
        self.original_path = _path_from_message(message)

class Handler:

    def __init__(self, func: typing.Callable, *, raw_request: bool=False, json_response: bool=False, strict: bool=False) -> None:
        self.raw_request = raw_request
        self.json_response = json_response
        self.orig_func = func
        self.strict = strict

    @cached_property
    def callqueue(self):
        pass

    @cached_property
    def handler_args(self):
        pass

    def __repr__(self):
        return f'{Handler.__module__}.{Handler.__name__}({self.orig_func!r}, raw_request={self.handler_args.raw_request}, json_response={self.json_response})'

    async def __call__(self, request: aiohttp.web.BaseRequest, **kwargs):
        args, kwargs = await self.handler_args.build_args(request, kwargs)
        response = await self.callqueue(*args, **kwargs)
        if not self.json_response:
            return response
        if isinstance(response, (http.Response, aiohttp.web.Response)):
            return response
        return http.make_response(json=response)

    def collect_calls(self) -> list[dict]:
        pass

class Session:
    handlers: dict[str, Handler]
    prefix_handlers: list[tuple[str, Handler]]
    regex_handlers: list[tuple[typing.Pattern, Handler]]

    def __init__(self, *, asyncexc_append, traceid_manager: TraceidManager, tracing_enabled=True, http_proxy_enabled=False, mockserver_host=None):
        self.traceid_manager = traceid_manager
        self.tracing_enabled = tracing_enabled
        self.handlers = {}
        self.prefix_handlers = []
        self.regex_handlers = []
        self.http_proxy_enabled = http_proxy_enabled
        self.mockserver_host = mockserver_host
        self._asyncexc_append = asyncexc_append

    def get_handler(self, path: str) -> tuple[Handler, RouteParams]:
        pass

    def _get_handler_not_found_message(self, path: str) -> str:
        pass

    async def handle_request(self, request: MockserverRequest, nofail_404: bool):
        pass

    def register_handler(self, path: str, func, *, prefix: bool=False, regex: bool=False):
        pass

    def _get_handler_for_request(self, request: MockserverRequest) -> tuple[Handler, RouteParams]:
        pass

    def collect_calls(self) -> list[dict]:
        pass

class Server:
    session = None

    def __init__(self, mockserver_info: classes.MockserverInfo, *, nofail=False, mockserver_debug=False, tracing_enabled=True, trace_id_header=DEFAULT_TRACE_ID_HEADER, span_id_header=DEFAULT_SPAN_ID_HEADER, http_proxy_enabled=False):
        self._info = mockserver_info
        self._nofail = nofail
        self._mockserver_debug = mockserver_debug
        self._tracing_enabled = tracing_enabled
        self._trace_id_header = trace_id_header
        self._span_id_header = span_id_header
        self._http_proxy_enabled = http_proxy_enabled

    @property
    def tracing_enabled(self) -> bool:
        pass

    @property
    def trace_id_header(self):
        pass

    @property
    def span_id_header(self):
        pass

    @property
    def http_proxy_enabled(self):
        pass

    @property
    def server_info(self) -> classes.MockserverInfo:
        pass

    def get_debug(self) -> bool:
        pass

    def set_debug(self, enabled: bool):
        pass

    @contextlib.contextmanager
    def new_session(self, *, asyncexc_append, traceid_manager: TraceidManager):
        pass

    async def handle_request(self, request):
        pass

    def _log_request(self, started, request, response=None, exc=None):
        pass

    async def _handle_request(self, request: MockserverRequest):
        pass

    def _report_other_test_request(self, request, trace_id):
        pass

class MockserverFixture:
    """Mockserver handler installer fixture."""

    def __init__(self, mockserver: Server, session: Session, base_prefix: str='', *, strict_default: bool=False) -> None:
        self._server = mockserver
        self._session = session
        self._base_prefix = base_prefix
        self._base_prefix_re = re.escape(base_prefix)
        self._strict_default = strict_default

    def new(self, prefix: str) -> 'MockserverFixture':
        """Create mockserver installer with given base prefix."""
        pass

    @property
    def base_url(self) -> str:
        """Mockserver base url."""
        pass

    @property
    def host(self) -> str | None:
        """Mockserver hostname."""
        pass

    @property
    def port(self) -> int | None:
        """Mockserver port."""
        pass

    @property
    def trace_id_header(self) -> str:
        pass

    @property
    def span_id_header(self) -> str:
        pass

    @property
    def trace_id(self) -> str:
        pass

    def handler(self, path: str, *, prefix: bool=False, raw_request: bool=False, json_response: bool=False, regex: bool=False, strict: typing.Optional[bool]=None) -> classes.GenericRequestDecorator:
        """Register basic http handler for ``path``.

        Returns decorator that registers handler ``path``. Original function is
        wrapped with :ref:`AsyncCallQueue`.

        :param path: match url by prefix if ``True`` exact match otherwise
        :param raw_request: pass ``aiohttp.web.Response`` to handler instead of
            ``testsuite.utils.http.Request``
        :param regex: set True to match path as regex pattern
        :param prefix: set True to match path prefix instead of whole path
        :param json_response: set True to let handler return json object
               instead of full response object

        .. code-block:: python

           @mockserver.handler('/service/path')
           def handler(request: testsuite.utils.http.Request):
               return mockserver.make_response('Hello, world!')
        """
        pass

    def json_handler(self, path: str, *, prefix: bool=False, raw_request: bool=False, regex: bool=False, strict: typing.Optional[bool]=None) -> classes.JsonRequestDecorator:
        """Register json http handler for ``path``.

        Returns decorator that registers handler ``path``. Original function is
        wrapped with :ref:`AsyncCallQueue`.

        :param path: match url by prefix if ``True`` exact match otherwise
        :param raw_request: pass ``aiohttp.web.Response`` to handler instead of
            ``testsuite.utils.http.Request``
        :param prefix: set True to match path prefix instead of whole path
        :param regex: set True to match path as regex pattern

        .. code-block:: python

           @mockserver.json_handler('/service/path')
           def handler(request: testsuite.utils.http.Request):
               # Return JSON document
               return {...}
               # or call to mockserver.make_response()
               return mockserver.make_response(...)
        """
        pass

    def aiohttp_handler(self, path: str, *, prefix: bool=False, regex: bool=False, strict: typing.Optional[bool]=None) -> classes.GenericRequestDecorator:
        pass

    def aiohttp_json_handler(self, path: str, *, prefix: bool=False, regex: bool=False, strict: typing.Optional[bool]=None) -> classes.JsonRequestDecorator:
        pass

    def url(self, path: str) -> str:
        """Builds mockserver url for ``path``"""
        pass

    def url_encoded(self, path: str) -> yarl.URL:
        """Builds mockserver url for ``path``"""
        pass

    def ws_url(self, path: str) -> str:
        pass

    def ignore_trace_id(self) -> typing.ContextManager[None]:
        pass

    @contextlib.contextmanager
    def tracing(self, value: bool=True):
        pass

    def get_callqueue_for(self, path) -> callinfo.AsyncCallQueue:
        pass
    make_response = staticmethod(http.make_response)
    TimeoutError = http.TimeoutError
    NetworkError = http.NetworkError

    def _handler_installer(self, path: str, *, strict: typing.Optional[bool], prefix: bool=False, raw_request: bool=False, json_response: bool=False, regex: bool=False) -> typing.Callable:
        pass

    def _build_fullpath(self, path, regex: bool=False) -> str:
        pass
MockserverSslFixture = MockserverFixture

def create_server(*, host: str, port: int, pytestconfig, ssl_info=None, loop=None):
    pass

def _create_ssl_context(ssl_cert: classes.SslCertInfo) -> ssl.SSLContext:
    pass

def _internal_error(message: str='Internal error') -> aiohttp.web.Response:
    pass

def _mocked_error_response(request, error_code) -> aiohttp.web.Response:
    pass

def _create_server_obj(mockserver_info: classes.MockserverInfo, mockserver_config: classes.MockserverConfig) -> Server:
    pass

def _create_web_server(server: Server, loop) -> aiohttp.web.Server:
    pass

def _create_mockserver_socket(socket_path=None, host='localhost', port=0, https=False):
    pass

@contextlib.asynccontextmanager
async def _create_server_from_socket(mockserver_socket: classes.MockserverSocket, mockserver_config: classes.MockserverConfig, ssl_cert: classes.SslCertInfo | None=None, loop=None) -> typing.AsyncGenerator[Server, None]:
    pass

def _create_mockserver_info(sock, socket_path, host: str, https: bool=False) -> classes.MockserverInfo:
    pass

def _create_unix_mockserver_info(socket_path: pathlib.Path) -> classes.MockserverInfo:
    pass

def _path_from_message(message):
    """Returns original HTTP path without query."""
    pass
