from threading import RLock

from graphility.database_safe_shared import SafeDatabase
from graphility.env import cdb_environment

cdb_environment["mode"] = "threads"
cdb_environment["rlock_obj"] = RLock


class ThreadSafeDatabase(SafeDatabase):
    """
    Thread safe version of graphility that uses several lock objects,
    on different methods / different indexes etc. It's completely different
    implementation of locking than SuperThreadSafe one.
    """
