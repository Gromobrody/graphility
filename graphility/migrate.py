import os
import shutil

from graphility.database import Database


def migrate(source, destination):
    """
    Very basic for now
    """
    dbs = Database(source)
    dbt = Database(destination)
    dbs.open()
    dbt.create()
    dbt.close()
    for curr in os.listdir(os.path.join(dbs.path, "_indexes")):
        if curr != "00id.py":
            shutil.copyfile(
                os.path.join(dbs.path, "_indexes", curr),
                os.path.join(dbt.path, "_indexes", curr),
            )
    dbt.open()
    for c in dbs.all("id"):
        del c["_rev"]
        dbt.insert(c)
    return True


if __name__ == "__main__":
    import sys

    migrate(sys.argv[1], sys.argv[2])
