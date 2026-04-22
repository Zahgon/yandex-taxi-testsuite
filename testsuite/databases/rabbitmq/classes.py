import asyncio
import dataclasses
import aio_pika

class BaseError(Exception):
    pass

class RabbitMqDisabledError(BaseError):
    pass

@dataclasses.dataclass(frozen=True)
class ConnectionInfo:
    """RabbitMQ connection parameters"""
    host: str
    tcp_port: int

class Channel:

    def __init__(self, channel: aio_pika.Channel):
        self._channel = channel

    async def __aenter__(self) -> 'Channel':
        if not self._channel.is_initialized:
            await self._channel.initialize()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb) -> None:
        await self._channel.close(exc_val)

    async def declare_exchange(self, exchange: str, exchange_type: aio_pika.ExchangeType, timeout: float=1.0) -> None:
        pass

    async def declare_queue(self, queue: str, timeout: float=1.0) -> None:
        pass

    async def bind_queue(self, exchange: str, queue: str, routing_key: str, timeout: float=1.0):
        pass

    async def publish(self, exchange: str, routing_key: str, body: bytes, timeout: float=1.0):
        pass

    async def consume(self, queue: str, count: int, timeout: float=2.0):
        pass

class Client:

    def __init__(self, connection_future):
        self._connection_future = connection_future
        self._connection = None

    async def teardown(self):
        pass

    async def get_channel(self) -> Channel:
        pass

class Control:

    def __init__(self, enabled: bool, conn_info: ConnectionInfo):
        self._enabled = enabled
        if self._enabled:
            self._client = Client(connection_future=aio_pika.connect_robust(host=conn_info.host, port=conn_info.tcp_port, timeout=2.0))

    async def teardown(self):
        pass

    async def get_channel(self) -> Channel:
        pass
