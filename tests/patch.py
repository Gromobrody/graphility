from codernitydb3.patch import patch_cache_lfu


class TestPatches:
    def test_lfu(self):

        from codernitydb3 import lfu_cache

        assert lfu_cache.__name__ == "lfu_cache"
        del lfu_cache

        from threading import RLock

        patch_cache_lfu(RLock)
        from codernitydb3 import lfu_cache

        assert lfu_cache.__name__ != "lfu_cache"
