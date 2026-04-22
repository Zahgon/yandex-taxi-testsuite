import dataclasses
import urllib.parse
_BOOL_TO_STR = {True: 'true', False: 'false'}
_STR_TO_BOOL = {value: key for key, value in _BOOL_TO_STR.items()}

@dataclasses.dataclass(frozen=True)
class ConnectionInfo:
    """Mongodb connection uri parameters"""
    host: str
    port: int
    dbname: str | None = None
    retry_writes: bool | None = None

    def get_uri(self, dbname: str | None=None, retry_writes: bool | None=None) -> str:
        """Get mongodb connection uri"""
        pass

def parse_connection_uri(uri: str) -> ConnectionInfo:
    pass

def _get_boolean_param(parsed_query: dict[str, list[str]], key: str) -> bool | None:
    pass
