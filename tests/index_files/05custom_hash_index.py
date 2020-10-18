# custom_hash_index
# CustomHashIndex

# inserted automatically
import os
import pickle
import shutil
import struct
from hashlib import md5

# custom index code start
from graphility import rr_cache

# custom db code start


# source of classes in index.classes_code
# index code start


class CustomHashIndex(HashIndex):
    def __init__(self, *args, **kwargs):
        kwargs["entry_line_format"] = "32sIIIcI"
        kwargs["hash_lim"] = 1
        super(CustomHashIndex, self).__init__(*args, **kwargs)

    def make_key_value(self, data):
        d = data.get("test")
        print(d)
        if d is None:
            return None
        if d > 5:
            k = 1
        else:
            k = 0
        return k, dict(test=d)

    def make_key(self, key):
        if not isinstance(key, str):
            key = str(key)
        return key.encode("utf8")
