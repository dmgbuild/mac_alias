
.. |pyversions| image:: https://img.shields.io/pypi/pyversions/mac_alias.svg
   :target: https://pypi.python.org/pypi/mac_alias
   :alt: Python Versions

.. |version| image:: https://img.shields.io/pypi/v/mac_alias.svg
   :target: https://pypi.python.org/pypi/mac_alias
   :alt: PyPI Version

.. |maturity| image:: https://img.shields.io/pypi/status/mac_alias.svg
   :target: https://pypi.python.org/pypi/mac_alias
   :alt: Maturity

.. |license| image:: https://img.shields.io/pypi/l/mac_alias.svg
   :target: https://github.com/dmgbuild/mac_alias/blob/main/LICENSE
   :alt: MIT License

.. |ci| image:: https://github.com/dmgbuild/mac_alias/workflows/CI/badge.svg?branch=main
   :target: https://github.com/dmgbuild/mac_alias/actions
   :alt: Build Status

=========
mac_alias
=========

|pyversions| |version| |maturity| |license| |ci|

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
