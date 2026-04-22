import collections
import contextlib
import enum
import typing
import py.io
SetTypes = (set, frozenset)

class TransformMode(enum.Enum):
    DEFAULT = 'default'
    EXPERIMENTAL = 'experimental'

class CompareTransform:
    path: list[str]
    errors: typing.DefaultDict[str, list[str]]

    def __init__(self, transform_mode: TransformMode=TransformMode.DEFAULT):
        self.path = ['left']
        self.errors = collections.defaultdict(list)
        self.transform_mode = transform_mode

    def report_error(self, msg: str, *, path=None) -> None:
        pass

    def visit(self, left: typing.Any, right: typing.Any) -> tuple[typing.Any, typing.Any]:
        pass

    def visit_list(self, left: list | tuple, right: typing.Any) -> tuple:
        pass

    def visit_dict(self, left: dict, right: typing.Any) -> tuple:
        pass

    def visit_set(self, left: set | frozenset, right: typing.Any) -> tuple:
        pass

    @contextlib.contextmanager
    def push(self, path: str):
        pass

def _resolve_values_default(left, right, reporter):
    pass

def _resolve_values_experimental(left, right, reporter):
    pass

def _format_keys(keys):
    pass

def _build_path(path, extra_path=None):
    pass
