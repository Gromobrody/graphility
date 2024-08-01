from graphility.database import Database

from .hash_tests import HashIndexTests
from .shard_tests import ShardTests
from .shared import DB_Tests
from .tree_tests import TreeIndexTests


class Test_Database(DB_Tests):
    _db = Database


class Test_HashIndex(HashIndexTests):
    _db = Database


class Test_TreeIndex(TreeIndexTests):
    _db = Database


class Test_ShardIndex(ShardTests):
    _db = Database
