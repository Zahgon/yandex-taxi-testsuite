import email
import json
import typing
import urllib.parse
import aiohttp.web
CONTENT_IN_GET_REQUEST_ERROR = 'GET requests cannot have content, but Content-Length header was sent.'
CHUNKED_CONTENT_IN_GET_REQUEST_ERROR = "GET requests cannot have content, but 'Transfer-Encoding: chunked' header was sent."
MULTIPART_MIME_PATTERN = 'MIME-Version: 1.0\nContent-Type: %s\n\n%s'

class BaseError(Exception):
    pass

class MockedError(BaseError):
    """Base class for mockserver mocked errors."""
    error_code = 'unknown'

class TimeoutError(MockedError):
    """Exception used to mock HTTP client timeout errors.

    Requires service side support.

    Available as ``mockserver.TimeoutError`` alias
    or by full name ``testsuite.utils.http.TimeoutError``.
    """
    error_code = 'timeout'

class NetworkError(MockedError):
    """Exception used to mock HTTP client network errors.

    Requires service side support.

    Available as ``mockserver.NetworkError`` alias
    or by full name ``testsuite.utils.http.NetworkError``.
    """
    error_code = 'network'

class HttpResponseError(BaseError):

    def __init__(self, *, url: str, status: int):
        self.url = url
        self.status = status
        super().__init__(f"status={self.status}, url='{self.url}'")

class InvalidRequestError(BaseError):
    """Invalid request which cannot be wrapped"""

class Request:
    """Adapts aiohttp.web.BaseRequest to mimic a frequently used subset of
    werkzeug.Request interface. ``data`` property is not supported,
    use get_data() instead.
    """

    def __init__(self, request: aiohttp.web.BaseRequest, data: bytes):
        self._request = request
        self._data: bytes = data
        self._json: object = None
        self._form: dict[str, str] | None = None

    @property
    def method(self) -> str:
        pass

    @property
    def url(self) -> str:
        return str(self._request.url)

    @property
    def path(self) -> str:
        pass

    @property
    def path_qs(self) -> str:
        pass

    @property
    def query_string(self) -> bytes:
        pass

    @property
    def headers(self):
        pass

    @property
    def content_type(self):
        pass

    def get_data(self) -> bytes:
        pass

    @property
    def form(self):
        pass

    @property
    def json(self) -> typing.Any:
        pass

    @property
    def cookies(self) -> typing.Mapping[str, str]:
        pass

    @property
    def args(self):
        pass

    @property
    def query(self):
        pass

class _NoValue:
    pass

async def wrap_request(request: aiohttp.web.BaseRequest) -> Request:
    pass

class Response:

    def __init__(self, body: bytes | bytearray | None=None, text: str | None=None, status: int=200, headers: typing.Mapping[str, str] | None=None, content_type: str | None=None, charset: str | None=None):
        if body and text:
            raise RuntimeError('Response params "body" and "text" can not be used at the same time')
        self._body = body
        self._text = text
        self._status = status
        self._headers = headers
        self._content_type = content_type
        self._charset = charset

    def __repr__(self):
        return f'<{self.__class__.__name__} body={self._body!r} text={self._text} status={self._status} content_type={self._content_type} charset={self._charset}>'

    def to_aiohttp(self) -> aiohttp.web.Response:
        pass

class ClientResponse:

    def __init__(self, response: aiohttp.ClientResponse, content: bytes, *, json_loads):
        self._response = response
        self._content: bytes = content
        self._text: str | None = None
        self._form: dict[str, str] | None = None
        self._json_loads = json_loads

    def __repr__(self):
        return f'<{self.__class__.__name__} method={self._response.method} url={self._response.url} status={self.status} content={self.content!r}>'

    @property
    def status_code(self) -> int:
        pass

    @property
    def status(self) -> int:
        pass

    @property
    def reason(self) -> str | None:
        pass

    @property
    def content(self) -> bytes:
        pass

    @property
    def text(self) -> str:
        pass

    def json(self) -> typing.Any:
        pass

    @property
    def form(self):
        pass

    @property
    def headers(self):
        pass

    @property
    def content_type(self):
        pass

    @property
    def encoding(self):
        pass

    @property
    def cookies(self):
        pass

    def raise_for_status(self) -> None:
        pass

async def wrap_client_response(response: aiohttp.ClientResponse, *, json_loads=json.loads):
    pass

def make_response(response: str | bytes | bytearray | None=None, status: int=200, headers: typing.Mapping[str, str] | None=None, content_type: str | None=None, charset: str | None=None, *, json=_NoValue, form=_NoValue) -> Response:
    """
    Create HTTP response object. Returns ``Response`` instance.

    :param response: response content
    :param status: HTTP status code
    :param headers: HTTP headers dictionary
    :param content_type: HTTP Content-Type header
    :param charset: Response character set
    :param json: JSON response shortcut
    :param form: x-www-form-urlencoded response shortcut
    """
    pass

def _json_response(data: typing.Any) -> bytes:
    pass

def _form_response(data: typing.Any) -> bytes:
    pass
