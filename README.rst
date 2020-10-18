Graphility - a fast pure-Python NoSQL database
==============================================

Graphility is based on CodernityDB by `Codernity Labs`_

Graphility is opensource, pure python (no 3rd party dependency), fast (really fast check Speed in documentation if you don't believe in words), multiplatform, schema-less, `NoSQL <http://en.wikipedia.org/wiki/NoSQL>`_ database. It has optional support for HTTP server version (Graphility-HTTP), and also Python client library (Graphility-PyClient) that aims to be 100% compatible with embeded version.

You can call it a more advanced key-value database. With multiple key-values indexes in the same engine. Also Graphility supports functions that are executed inside database.

Documentation in repo still refers to CodernityDB and will be updated at the end of reconstruction process.

Reconstruction
--------------

As of 2020 the original CodernityDB has been neglected for quite some time and the original repo has been lost.

`Nick M.`_ already started porting CodernityDB to Python 3. Go to his repo to see progress.
I'll try to backport any changes he makes but I cant' guarantee anything.

I decided to make my own port because I want to tear it down and rebuild it piece by piece using only Python 3.8+.
You know, to fully know the internals. I also want to add graph layer on top of it.
Also, Apache 2.0 License requires me to change the name of the project since "CodernityDB"
is a trademark/servicemark of Codernity_.


Key features
------------

* Native python database
* Multiple indexes
* Fast (more than 50 000 insert operations per second see Speed in documentation for details)
* Embeded mode (default). REST Server and client are planned.
* Easy way to implement custom Storage
* Sharding support

Planned features
----------------

* Graph db layer with pluggable language support (GQL, Gremlin, Cypher, SPARQL, etc.)
* Async support

Install
-------

Graphility is pure Python and does not need external dependencies.

   pip install graphility

or from sources::

   git clone ssh://git@github.com:Gromobrody/graphility.git
   cd graphility
   python setup.py install

Development
-----------

Poetry_ is used as project management tool. After downloading the project, activate the virtual env and install dev dependencies::

    poetry shell
    poetry install

Now you're ready to go.


License
-------

* Copyright 2020 Dominik Kozaczko (https://github.com/dekoza)
* Copyright 2020 Nick M. (https://github.com/nickmasster)
* Copyright 2011-2013 Codernity (http://codernity.com)

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

.. _Codernity Labs: http://labs.codernity.com/codernitydb
.. _Nick M.: https://github.com/nickmasster
.. _Poetry: https://python-poetry.org/docs/
.. _Codernity: https://codernity.com/
