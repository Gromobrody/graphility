import os
import uuid
from hashlib import md5

from py.test import raises
from pytest import fixture

from graphility.database import Database, RecordNotFound
from graphility.hash_index import HashIndex, MultiHashIndex
from graphility.indexcreator import (
    IndexCreatorFunctionException,
    IndexCreatorValueException,
    Parser,
)
from graphility.tree_index import MultiTreeBasedIndex, TreeBasedIndex

# class db_set():
# def __init__(self,t):
# self.t = t
# def __enter__(self):
# self.db = Database(os.path.join(str(self.t), 'db'))
# self.db.create()
# return self.db
# def __exit__(self,type,value,traceback):
# self.db.destroy()


@fixture
def db(request):
    db = Database(os.path.join(str(request.getfixturevalue("tmpdir")), "db"))
    db.create()
    return db


def compare_for_multi_index(db, name, s, key_name, data, keys):
    db.add_index(s)

    for i in data:
        db.insert({key_name: i})

    # for i in db.all(name):
    # print i

    for i, k in keys:
        if k is None:
            with raises(RecordNotFound):
                db.get(name, i, with_doc=True)
        else:
            assert db.get(name, i, with_doc=True)["doc"][key_name] == k


class TestIndexCreatorWithDatabase:
    def test_output_check(self, db, tmpdir):
        s = """
        type = HashIndex
        name = s
        key_format =     32s
        hash_lim = 1
        make_key_value:
        0,None
        make_key:
        0
        """
        db.add_index(s)
        assert s.encode("utf8") == db.get_index_code("s", code_switch="S")

        s1 = """
        type = TreeBasedIndex
        name = s1
        key_format =     32s
        make_key_value:
        0,None
        make_key:
        0
        """
        db.add_index(s1)
        assert s1.encode("utf8") == db.get_index_code("s1", code_switch="S")


class TestMultiIndexCreatorWithInternalImports:
    def test_infix(self, db):
        s = """
        name = s
        type = MultiTreeBasedIndex
        key_format: 3s
        make_key_value:
        infix(a,2,3,3),null
        make_key:
        fix_r(key,3)
        """
        compare_for_multi_index(
            db,
            "s",
            s,
            "a",
            ["abcd"],
            [
                ("a", None),
                ("ab", "abcd"),
                ("abc", "abcd"),
                ("b", None),
                ("abcd", "abcd"),  # fix_r will trim it to 3 letters!
                ("bcd", "abcd"),
                ("abdc", None),
            ],
        )

        s2 = """
        name = s2
        type = MultiTreeBasedIndex
        key_format: 5s
        make_key_value:
        infix(a,0,20,5),None
        make_key:
        fix_r(key,5)
        """
        compare_for_multi_index(
            db,
            "s2",
            s2,
            "a",
            ["abcd"],
            [
                ("a", "abcd"),
                ("ab", "abcd"),
                ("abc", "abcd"),
                ("b", "abcd"),
                ("abcd", "abcd"),
                ("bcd", "abcd"),
                ("abdc", None),
            ],
        )

    def test_more_than_one_func(self, db):
        s = """
        name = s
        type = MultiTreeBasedIndex
        key_format: 3s
        make_key_value:
        len(a)>3:infix(a,2,3,3),null
        prefix(a,2,3,3),none
        make_key:
        fix_r(key,3)
        """
        compare_for_multi_index(
            db,
            "s",
            s,
            "a",
            ["abcd"],
            [
                ("a", None),
                ("ab", "abcd"),
                ("abc", "abcd"),
                ("b", None),
                ("abcd", "abcd"),  # fix_r will trim it to 3 letters!
                ("bcd", "abcd"),
                ("abdc", None),
            ],
        )
