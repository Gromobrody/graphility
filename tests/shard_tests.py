import pytest

from graphility.database import Database
from graphility.index import IndexPreconditionsException
from graphility.sharded_hash import ShardedUniqueHashIndex


class ShardedUniqueHashIndex5(ShardedUniqueHashIndex):
    custom_header = "from codernitydb3.sharded_hash import ShardedUniqueHashIndex"

    def __init__(self, *args, **kwargs):
        kwargs["sh_nums"] = 5
        super(ShardedUniqueHashIndex5, self).__init__(*args, **kwargs)


class ShardedUniqueHashIndex10(ShardedUniqueHashIndex):
    custom_header = "from codernitydb3.sharded_hash import ShardedUniqueHashIndex"

    def __init__(self, *args, **kwargs):
        kwargs["sh_nums"] = 10
        super(ShardedUniqueHashIndex10, self).__init__(*args, **kwargs)


class ShardedUniqueHashIndex50(ShardedUniqueHashIndex):
    custom_header = "from codernitydb3.sharded_hash import ShardedUniqueHashIndex"

    def __init__(self, *args, **kwargs):
        kwargs["sh_nums"] = 50
        super(ShardedUniqueHashIndex50, self).__init__(*args, **kwargs)


class ShardTests:
    def test_create(self, tmpdir):
        db = Database(str(tmpdir) + "/db")
        db.create(with_id_index=False)
        db.add_index(ShardedUniqueHashIndex(db.path, "id", sh_nums=3))

    @pytest.mark.parametrize(("sh_nums",), [(x,) for x in (5, 10, 50)])
    def test_num_shards(self, tmpdir, sh_nums):
        db = Database(str(tmpdir) + "/db")
        db.create(with_id_index=False)
        n = globals()["ShardedUniqueHashIndex%d" % sh_nums]
        db.add_index(n(db.path, "id"))
        assert db.id_ind.sh_nums == sh_nums

    @pytest.mark.parametrize(("sh_nums",), [(x,) for x in (5, 10, 50)])
    def test_insert_get(self, tmpdir, sh_nums):
        db = Database(str(tmpdir) + "/db")
        db.create(with_id_index=False)
        n = globals()["ShardedUniqueHashIndex%d" % sh_nums]
        db.add_index(n(db.path, "id"))
        l = []
        for x in range(10000):
            l.append(db.insert(dict(x=x))["_id"])

        for curr in l:
            assert db.get("id", curr)["_id"] == curr

    @pytest.mark.parametrize(("sh_nums",), [(x,) for x in (5, 10, 50)])
    def test_all(self, tmpdir, sh_nums):
        db = Database(str(tmpdir) + "/db")
        db.create(with_id_index=False)
        n = globals()["ShardedUniqueHashIndex%d" % sh_nums]
        db.add_index(n(db.path, "id"))
        l = []
        for x in range(10000):
            l.append(db.insert(dict(x=x))["_id"])

        for curr in db.all("id"):
            l.remove(curr["_id"])

        assert l == []

    def test_to_many_shards(self, tmpdir):
        db = Database(str(tmpdir) + "/db")
        db.create(with_id_index=False)
        # it's ok to use sharded directly there
        with pytest.raises(IndexPreconditionsException):
            db.add_index(ShardedUniqueHashIndex(db.path, "id", sh_nums=300))
        with pytest.raises(IndexPreconditionsException):
            db.add_index(ShardedUniqueHashIndex(db.path, "id", sh_nums=256))

    def test_compact_shards(self, tmpdir):
        db = Database(str(tmpdir) + "/db")
        db.create(with_id_index=False)
        db.add_index(ShardedUniqueHashIndex5(db.path, "id"))

        for x in range(100):
            db.insert({"x": x})

        db.compact()
        assert db.count(db.all, "id") == 100
