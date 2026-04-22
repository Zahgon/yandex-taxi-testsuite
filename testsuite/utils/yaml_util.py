import yaml
import yaml.parser
from testsuite.utils import object_hook as object_hook_util

class BaseError(Exception):
    pass

class ParserError(BaseError):
    pass
if hasattr(yaml, 'CLoader'):
    _Loader = yaml.CLoader
else:
    _Loader = yaml.Loader

def load_file(path, encoding='utf-8', object_hook=None):
    pass

def load(string_or_stream, object_hook=None):
    pass
