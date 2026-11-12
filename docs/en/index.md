# mac_alias {{ release }}

## What is this?

macOS has a special data structure it calls an Alias, which allows programs that make use of it to locate the file to which it refers more reliably than they would be able to from e.g. a filename alone.

The format of this structure is not documented, so until recently you would have used macOS APIs to construct and process Alias records. Sadly, Apple has deprecated the APIs in question in favor of its new "Bookmark" functionality; this is understandable, but it makes it tricky to construct an Alias record reliably in future.

This module contains code to parse and generate Alias records from a Pythonic equivalent data structure, and does not rely on the deprecated APIs.

It also contains code to parse and generate Bookmark records, again from a Pythonic equivalent, and without relying on OS X APIs.

## Usage

To parse an Alias record given binary data:

```python
from mac_alias import Alias

a = Alias.from_bytes(my_data)
```

To generate a binary Alias record:

```python
a.to_bytes()
```

Finally, to build an [`Alias`][mac_alias.Alias] for a file:

```python
Alias.for_file("/path/to/file.ext")
```

It's probably best to resist the temptation to mess with the Alias class too much otherwise.

Similarly, to parse a Bookmark record given binary data:

```python
from mac_alias import Bookmark

b = Bookmark.from_bytes(my_data)
```

To generate a binary Bookmark record:

```python
b.to_bytes()
```

And to build a [`Bookmark`][mac_alias.Bookmark] for a file:

```python
Bookmark.for_file("/path/to/file.ext")
```

## Code Documentation

- [mac_alias package](mac_alias.md)

## Binary Formats

- [Mac Alias Format](alias_fmt.md)
- [Mac Bookmark Format](bookmark_fmt.md)
