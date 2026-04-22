import json
from testsuite.utils import object_hook as object_hook_util

def loads(string, *args, **kwargs):
    """Helper function that wraps ``json.loads``.

    Automatically passes the object_hook for BSON type conversion.
    """
    pass

def substitute(json_obj, *, object_hook=None):
    """Create transformed json by making substitutions:

    {"$mockserver": "/path", "$schema": true} -> "http://localhost:9999/path"
    {"$dateDiff": 10} -> datetime.datetime.now(datetime.timezone.utc).replace(tzinfo=None) + timedelta(seconds=10)
    """
    pass

def dumps(obj, *args, **kwargs):
    """Helper function that wraps ``json.dumps``.

    This function does NOT support ``bson.binary.Binary`` and
    ``bson.code.Code`` types. It just passes ``default`` argument to
    ``json.dumps`` function.
    """
    pass
