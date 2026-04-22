import argparse
import pathlib
import string
MASTER_TPL_FILENAME = 'redis_master.conf.tpl'
SENTINEL_TPL_FILENAME = 'redis_sentinel.conf.tpl'
SLAVE_TPL_FILENAME = 'redis_slave.conf.tpl'
CLUSTER_TPL_FILENAME = 'redis_cluster_node.conf.tpl'
SENTINEL_PARAMS = [{'down_after_milliseconds': 60000, 'failover_timeout': 180000, 'parallel_syncs': 1}, {'down_after_milliseconds': 10000, 'failover_timeout': 180000, 'parallel_syncs': 5}]

def _parse_args():
    pass

def _generate_redis_config(input_file: pathlib.Path, output_file: pathlib.Path, host: str, port: int, master_port: int | None=None) -> None:
    pass

def _generate_master(host: str, port: int, output_path: pathlib.Path, index: int) -> None:
    pass

def _generate_slave(host: str, port: int, master_port: int, output_path: pathlib.Path, index: int) -> None:
    pass

def _generate_sentinel(host: str, sentinel_port: int, ports: list[int], output_path: pathlib.Path, params: list) -> None:
    pass

def _generate_cluster_node(host: str, port: int, output_path: pathlib.Path, index: int) -> None:
    pass

def _construct_output_filename(output_path: pathlib.Path, tpl_filename: str, number: int) -> pathlib.Path:
    pass

def _redis_config_directory() -> pathlib.Path:
    pass

def generate_cluster_redis_configs(output_path: pathlib.Path, host: str, cluster_ports: tuple[int, ...]) -> None:
    pass

def generate_standalone_redis_config(output_path: pathlib.Path, host: str, port: int) -> None:
    pass

def generate_redis_configs(output_path: pathlib.Path, host: str, master0_port: int, master1_port: int, slave0_port: int, slave1_port: int, slave2_port: int, sentinel_port: int) -> None:
    pass

def main():
    pass
if __name__ == '__main__':
    main()
