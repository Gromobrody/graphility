.. _api_database:

API docs
========

Here you will find API docs. If you're python user you will probably
understand it. In other case you should visit:

- :ref:`database_operations_description`
- :ref:`design`
- :ref:`quick_tutorial`

And you probably want to use |GraphilityHTTP-link| instead this embedded version.

Database
--------

.. note::
    Please refer to :ref:`database_operations_description` for general description


Standard
^^^^^^^^

.. automodule:: graphility.database
    :members:
    :undoc-members:
    :show-inheritance:


Thread Safe Database
^^^^^^^^^^^^^^^^^^^^

.. autoclass:: graphility.database_thread_safe.ThreadSafeDatabase
    :members:
    :undoc-members:
    :show-inheritance:


Super Thread Safe Database
^^^^^^^^^^^^^^^^^^^^^^^^^^

.. automodule:: graphility.database_super_thread_safe
    :members:
    :undoc-members:
    :show-inheritance:


Gevent Database
^^^^^^^^^^^^^^^

.. automodule:: graphility.database_gevent
    :members:
    :undoc-members:
    :show-inheritance:


Indexes
-------

.. note::
   If you're **not interested in graphility development / extending** you don't need to read this section,
   please then refer to :ref:`database_indexes`, **otherwise** please remember that index methods are called from
   ``Database`` object.



General Index
^^^^^^^^^^^^^

.. automodule:: graphility.index
    :members:
    :undoc-members:
    :show-inheritance:


Hash Index specific
^^^^^^^^^^^^^^^^^^^

.. note::
    Please refer to :ref:`internal_hash_index` for description

.. automodule:: graphility.hash_index
    :members:
    :undoc-members:
    :show-inheritance:


B+Tree Index specific
^^^^^^^^^^^^^^^^^^^^^

.. note::
    Please refer to :ref:`internal_tree_index` for description

.. automodule:: graphility.tree_index
    :members:
    :undoc-members:
    :show-inheritance:



Storage
-------

.. automodule:: graphility.storage
    :members:
    :undoc-members:
    :show-inheritance:


Patches
-------

.. automodule:: graphility.patch
    :members:
    :show-inheritance:
    :undoc-members:
