import asyncio
import dataclasses
import logging
import typing
import aiokafka
logger = logging.getLogger(__name__)

@dataclasses.dataclass(frozen=True)
class ServiceSettings:
    """Kafka service start settings"""
    server_host: str
    server_port: int
    controller_port: int
    custom_start_topics: dict[str, int]
'Kafka bootstrap servers URLs list'
BootstrapServers = list[str]
'Kafka message header'
Header = tuple[str, bytes]
'\n    Kafka headers sequence.\n    The order is taken into account.\n    Duplicate keys are allowed.\n'
Headers = typing.Sequence[Header]

class KafkaDisabledError(Exception):
    pass

class KafkaProducer:
    """
    Kafka producer wrapper.
    """

    def __init__(self, enabled: bool, bootstrap_servers: str):
        self._enabled = enabled
        self._bootstrap_servers = bootstrap_servers

    async def start(self):
        pass

    async def send(self, topic: str, key: str | bytes, value: str | bytes, partition: int | None=None, headers: Headers | None=None):
        """
        Sends the message (``value``) to ``topic`` by ``key`` and,
        optionally, to a given ``partition`` and waits until it is delivered.
        If the call is successfully awaited,
        message is guaranteed to be delivered.

        :param topic: topic name.
        :param key: key. Needed to determine message's partition.
        :param value: message payload. Must be valid UTF-8.
        :param partition: Optional message partition.
            If not passed, determined by internal partitioner
            depends on key's hash.
        """
        pass

    async def send_async(self, topic: str, key: str | bytes, value: str | bytes, partition: int | None=None, headers: Headers | None=None):
        """
        Sends the message (``value``) to ``topic`` by ``key`` and,
        optionally, to a given ``partition`` and
        returns the future for message delivery awaiting.

        :param topic: topic name.
        :param key: key. Needed to determine message's partition.
        :param value: message payload. Must be valid UTF-8.
        :param partition: Optional message partition.
            If not passed, determined by internal partitioner
            depends on key's hash.
        """
        pass

    async def _flush(self):
        pass

    async def aclose(self):
        pass

class ConsumedMessage:
    """Wrapper for consumed record."""
    topic: str
    key_raw: bytes
    value_raw: bytes
    partition: int
    offset: int
    headers_raw: Headers

    def __init__(self, record: aiokafka.ConsumerRecord):
        self.topic = record.topic
        self.key_raw = record.key
        self.value_raw = record.value
        self.partition = record.partition
        self.offset = record.offset
        self.headers_raw = record.headers

    @property
    def key(self) -> str:
        pass

    @property
    def value(self) -> str:
        pass

    @property
    def headers(self) -> list[Header]:
        pass

class KafkaConsumer:
    """
    Kafka balanced consumer wrapper.
    All consumers are created with the same group.id,
    after each test consumer commits offsets for all consumed messages.
    This is needed to make tests independent.
    """

    def __init__(self, enabled: bool, bootstrap_servers):
        self._enabled = enabled
        self._bootstrap_servers = bootstrap_servers
        self._subscribed_topics: list[str] = []

    async def start(self):
        pass

    def _subscribe(self, topics: list[str]):
        pass

    async def _commit(self):
        pass

    async def _unsubscribe(self):
        pass

    async def receive_one(self, topics: list[str], timeout: float=20.0) -> ConsumedMessage:
        """
        Waits until one message are consumed.

        :param topics: list of topics to read messages from.
        :param timeout: timeout to stop waiting. Default is 20 seconds.

        :returns: :py:class:`ConsumedMessage`
        """
        pass

    async def receive_batch(self, topics: list[str], max_batch_size: int | None, timeout: float=3.0) -> list[ConsumedMessage]:
        """
        Waits until either ``max_batch_size`` messages are consumed or
        ``timeout`` expired.

        :param topics: list of topics to read messages from.
        :max_batch_size: maximum number of consumed messages.
        :param timeout: timeout to stop waiting. Default is 3 seconds.

        :returns: :py:class:`List[ConsumedMessage]`
        """
        pass

    async def aclose(self):
        pass
