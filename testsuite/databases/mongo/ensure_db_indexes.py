import typing
import pymongo
import pytest
SORT_STR_TO_PYMONGO = {'ascending': pymongo.ASCENDING, 'descending': pymongo.DESCENDING, '2d': pymongo.GEO2D, '2dsphere': pymongo.GEOSPHERE, 'hashed': pymongo.HASHED, 'text': pymongo.TEXT}

def create_collection(collection):
    pass

def shard_collection(collection, sharding):
    pass

def ensure_db_indexes(dbase, db_settings, sharding_enabled=True):
    pass

def _ensure_index(index, collection):
    pass

def _get_args_for_ensure_func(index):
    pass

def _get_kwargs_for_shard_func(sharding):
    pass

def _is_collection_sharded(collection):
    pass
