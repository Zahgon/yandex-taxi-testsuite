import json
import ssl
import typing
import uuid
import aiohttp
import yarl
from testsuite import types
from testsuite.utils import http, url_util
DEFAULT_HOST = 'localhost'
DEFAULT_TIMEOUT = 120.0
TResponse = typing.TypeVar('TResponse', aiohttp.ClientResponse, http.ClientResponse)

class BaseAiohttpClient:

    def __init__(self, base_url: str, *, session: aiohttp.ClientSession, ssl_context: ssl.SSLContext | None=None, span_id_header: str | None=None, headers: dict[str, str] | None=None, timeout: float=DEFAULT_TIMEOUT):
        """
        :param base_url: Base client url
        :param session: ``aiohttp.ClientSession`` instance
        :param headers: default request headers dictionary
        :param timeout: http client default timeout
        """
        self._base_url = url_util.ensure_trailing_separator(base_url)
        self._headers = headers or {}
        self._timeout = timeout
        self._session = session
        self._ssl_context = ssl_context
        self._span_id_header = span_id_header

    def url(self, path: str | yarl.URL):
        pass

    async def _aiohttp_request(self, http_method: str, path: str | yarl.URL, headers: dict[str, str] | None=None, bearer: str | None=None, x_real_ip: str | None=None, **kwargs) -> aiohttp.ClientResponse:
        pass

    def _build_headers(self, user_headers: dict[str, str] | None=None, bearer: str | None=None, x_real_ip: str | None=None) -> dict[str, str]:
        pass

class GenericClient(BaseAiohttpClient, typing.Generic[TResponse]):
    """Basic asyncio HTTP service client."""

    async def post(self, path: str, json: types.JsonAnyOptional=None, data: typing.Any=None, params: dict[str, str] | None=None, bearer: str | None=None, x_real_ip: str | None=None, headers: dict[str, str] | None=None, **kwargs) -> TResponse:
        """Perform HTTP POST request."""
        pass

    async def put(self, path, json: types.JsonAnyOptional=None, data: typing.Any=None, params: dict[str, str] | None=None, bearer: str | None=None, x_real_ip: str | None=None, headers: dict[str, str] | None=None, **kwargs) -> TResponse:
        """Perform HTTP PUT request."""
        pass

    async def patch(self, path, json: types.JsonAnyOptional=None, data: typing.Any=None, params: dict[str, str] | None=None, bearer: str | None=None, x_real_ip: str | None=None, headers: dict[str, str] | None=None, **kwargs) -> TResponse:
        """Perform HTTP PATCH request."""
        pass

    async def get(self, path: str, headers: dict[str, str] | None=None, bearer: str | None=None, x_real_ip: str | None=None, **kwargs) -> TResponse:
        """Perform HTTP GET request."""
        pass

    async def delete(self, path: str, headers: dict[str, str] | None=None, bearer: str | None=None, x_real_ip: str | None=None, **kwargs) -> TResponse:
        """Perform HTTP DELETE request."""
        pass

    async def options(self, path: str, headers: dict[str, str] | None=None, bearer: str | None=None, x_real_ip: str | None=None, **kwargs) -> TResponse:
        """Perform HTTP OPTIONS request."""
        pass

    async def request(self, http_method: str, path: str, **kwargs) -> TResponse:
        """Perform HTTP ``http_method`` request."""
        pass

    async def _request(self, http_method: str, path: str | yarl.URL, headers: dict[str, str] | None=None, bearer: str | None=None, x_real_ip: str | None=None, **kwargs) -> TResponse:
        pass

class AiohttpClient(GenericClient[aiohttp.ClientResponse]):

    async def _request(self, http_method: str, path: str | yarl.URL, headers: dict[str, str] | None=None, bearer: str | None=None, x_real_ip: str | None=None, **kwargs) -> aiohttp.ClientResponse:
        pass

class Client(GenericClient[http.ClientResponse]):

    async def _request(self, http_method: str, path: str | yarl.URL, headers: dict[str, str] | None=None, bearer: str | None=None, x_real_ip: str | None=None, **kwargs) -> http.ClientResponse:
        pass

    def _wrap_client_response(self, response) -> typing.Awaitable[http.ClientResponse]:
        pass

def _flatten(query_params):
    pass
