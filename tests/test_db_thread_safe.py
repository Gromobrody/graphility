import os
import random
import time
from threading import Thread

import pytest

from graphility.database_thread_safe import ThreadSafeDatabase

from .hash_tests import HashIndexTests
from .shared import DB_Tests, WithAIndex
from .tree_tests import TreeIndexTests


class Test_Database(DB_Tests):

    _db = ThreadSafeDatabase


class Test_HashIndex(HashIndexTests):

    _db = ThreadSafeDatabase


class Test_TreeIndex(TreeIndexTests):

    _db = ThreadSafeDatabase


class Test_Threads:

    _db = ThreadSafeDatabase

    def test_one(self, tmpdir):
        db = self._db(os.path.join(str(tmpdir), "db"))
        db.create()
        db.add_index(WithAIndex(db.path, "with_a"))
        ths = []
        for x in range(1, 101):
            ths.append(Thread(target=db.insert, args=(dict(a=x),)))
        for th in ths:
            th.start()
        for th in ths:
            th.join()
        assert db.count(db.all, "with_a") == 100
        l = list(range(1, 101))
        for curr in db.all("with_a", with_doc=True):
            print(curr)
            a = curr["doc"]["a"]
            l.remove(a)
        assert l == []

    @pytest.mark.parametrize(
        ("threads_num",), [(x,) for x in (3, 10, 20, 50, 100, 250)]
    )
    def test_conc_update(self, tmpdir, threads_num):
        db = self._db(os.path.join(str(tmpdir), "db"))
        db.create()
        db.add_index(WithAIndex(db.path, "with_a"))
        db.insert(dict(a=1))

        def updater():
            i = 0
            time.sleep(random.random() // 100)
            while True:
                rec = list(db.all("id", limit=1))
                doc = rec[0].copy()
                doc["a"] += 1
                try:
                    db.update(doc)
                except:
                    i += 1
                    if i > 100:
                        return False
                    time.sleep(random.random() // 100)
                else:
                    return True

        ths = []
        for x in range(threads_num):  # python threads... beware!!!
            ths.append(Thread(target=updater))
        for th in ths:
            th.start()
        for th in ths:
            th.join()

        assert db.count(db.all, "with_a", with_doc=True) == 1
        assert db.count(db.all, "id") == 1
