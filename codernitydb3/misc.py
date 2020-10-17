import uuid
from random import getrandbits, randrange


class NONE:
    """
    It's inteded to be None but different,
    for internal use only!
    """


def random_hex_32():
    return uuid.UUID(int=getrandbits(128), version=4).hex.encode("utf8")


def random_hex_4(*args, **kwargs):
    s = "%04x" % randrange(256 ** 2)
    return s.encode("utf8")
