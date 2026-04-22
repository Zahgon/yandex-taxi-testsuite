import typing
import aiohttp.web
from testsuite.utils import callinfo, http

def magic_arg(func):
    pass

def magic_arg_wrapped(func):
    pass

@magic_arg_wrapped
def arg_body_json(request: http.Request):
    pass

@magic_arg_wrapped
def arg_body_binary(request: http.Request):
    pass

@magic_arg_wrapped
def arg_form(request: http.Request):
    pass

@magic_arg
def arg_cookies(request: aiohttp.web.BaseRequest):
    pass

@magic_arg
def arg_method(request: aiohttp.web.BaseRequest):
    pass

@magic_arg
def arg_path(request: aiohttp.web.BaseRequest):
    pass

@magic_arg
def arg_headers(request: aiohttp.web.BaseRequest):
    pass

@magic_arg
def arg_query(request: aiohttp.web.BaseRequest):
    pass

@magic_arg
def arg_content_type(request: aiohttp.web.BaseRequest):
    pass

class MagicArgsHandler:
    magic_args_handlers = {'body_binary': arg_body_binary, 'body_json': arg_body_json, 'content_type': arg_content_type, 'cookies': arg_cookies, 'form': arg_form, 'headers': arg_headers, 'method': arg_method, 'path': arg_path, 'query': arg_query}
    has_request = False

    def __init__(self, func: typing.Callable, *, raw_request: bool) -> None:
        signature = callinfo.getfullargspec(func)
        self.magic_args: list = []
        self.raw_request = raw_request
        if signature.args:
            self.has_request = True
            request_arg = signature.args[0]
            if request_arg in signature.annotations:
                self._infer_request_type(signature.annotations[request_arg])
            for arg in signature.args[1:]:
                self._handle_arg(arg)
        elif signature.varargs:
            self.has_request = True
        if signature.kwonlyargs:
            for arg in signature.kwonlyargs:
                self._handle_arg(arg)

    def _infer_request_type(self, request_type: type) -> None:
        pass

    def _handle_arg(self, arg: str) -> None:
        pass

    async def build_args(self, request: aiohttp.web.BaseRequest, orig_kwargs: dict[str, object]) -> tuple:
        pass
