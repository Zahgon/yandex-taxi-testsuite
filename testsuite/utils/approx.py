import json
import math

class Float(float):

    def __eq__(self, obj) -> bool:
        if isinstance(obj, (float, int)):
            return math.isclose(self, obj)
        return super().__eq__(obj)

    def __hash__(self):
        return super().__hash__()

def json_loads(data, **kwargs):
    pass

def wrap_json(data):
    pass
