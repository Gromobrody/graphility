from graphility.database_super_thread_safe import SuperThreadSafeDatabase

from .hash_tests import HashIndexTests
from .shared import DB_Tests
from .test_db_thread_safe import Test_Threads as Test_ThreadsSafe
from .tree_tests import TreeIndexTests


class Test_Database(DB_Tests):
    _db = SuperThreadSafeDatabase


class Test_HashIndex(HashIndexTests):
    _db = SuperThreadSafeDatabase


class Test_TreeIndex(TreeIndexTests):
    _db = SuperThreadSafeDatabase


class Test_Threads(Test_ThreadsSafe):
    _db = SuperThreadSafeDatabase
