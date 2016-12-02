.. mac_alias documentation master file, created by
   sphinx-quickstart on Thu Feb 13 12:38:59 2014.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

mac_alias - Generate/parse Mac OS Alias records from Python
===========================================================

This document refers to version |release|

What is this?
=============

The Mac OS has a special data structure it calls an Alias, which allows
programs that make use of it to locate the file to which it refers more
reliably than they would be able to from e.g. a filename alone.

The format of this structure is not documented, so until recently you would
have used Mac OS X APIs to construct and process Alias records.  Sadly, Apple
has deprecated the APIs in question in favour of its new "Bookmark"
functionality; this is understandable, but it makes it tricky to construct an
Alias record reliably in future.

This module contains code to parse and generate Alias records from a Pythonic
equivalent data structure, and does not rely on the deprecated APIs.

It also contains code to parse and generate Bookmark records, again from a
Pythonic equivalent, and without relying on OS X APIs.

Usage
=====

To parse an Alias record given binary data::

  from mac_alias import Alias

  a = Alias.from_bytes(my_data)

To generate a binary Alias record::

  a.to_bytes()

Finally, to build an :class:`~mac_alias.Alias` for a file::

  Alias.for_file('/path/to/file.ext')

It's probably best to resist the temptation to mess with the Alias class too
much otherwise.

Similarly, to parse a Bookmark record given binary data::

  from mac_alias import Bookmark

  b = Bookmark.from_bytes(my_data)

To generate a binary Bookmark record::

  b.to_bytes()

And to build a :class:`~mac_alias.Bookmark` for a file::

  Bookmark.for_file('/path/to/file.ext')

Code Documentation
==================

Contents:

.. toctree::
   :maxdepth: 2

   mac_alias


Binary Formats
==============

.. toctree::
   :maxdepth: 2

   alias_fmt
   bookmark_fmt


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
