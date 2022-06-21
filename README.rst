=========
mac_alias
=========

.. image:: https://img.shields.io/pypi/pyversions/mac_alias.svg
   :target: https://pypi.python.org/pypi/mac_alias
   :alt: Python Versions

.. image:: https://img.shields.io/pypi/v/mac_alias.svg
   :target: https://pypi.python.org/pypi/mac_alias
   :alt: PyPI Version

.. image:: https://img.shields.io/pypi/status/mac_alias.svg
   :target: https://pypi.python.org/pypi/mac_alias
   :alt: Maturity

.. image:: https://img.shields.io/pypi/l/mac_alias.svg
   :target: https://github.com/dmgbuild/mac_alias/blob/main/LICENSE
   :alt: MIT License

.. image:: https://github.com/dmgbuild/mac_alias/workflows/CI/badge.svg?branch=main
   :target: https://github.com/dmgbuild/mac_alias/actions
   :alt: Build Status

.. image:: https://readthedocs.org/projects/mac_alias/badge/?version=latest
   :target: http://mac_alias.readthedocs.io/en/latest/?badge=latest
   :alt: Docs Build Status

What is this?
-------------

``mac_alias`` lets you generate or read binary Alias and Bookmark records
from Python code.

While it is written in pure Python, some OS X specific code is required to
generate a proper Alias or Bookmark record for a given file, so this module
currently is not portable to other platforms.

Credit is due to Wim Lewis <wiml@hhhh.org>, whose work on reverse engineering
the alias format was extremely useful in writing this code.  Alastair Houghton
<alastair@alastairs-place.net> was responsible for reverse engineering the
bookmark format.

See the documentation_ for more information.

.. _documentation: http://mac-alias.rtfd.org
