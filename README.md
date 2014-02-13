`mac_alias` lets you generate or read binary Alias records from Python code.
While it is written in pure Python, some OS X specific code is required to
generate a proper Alias record for a given file, so this module currently
is not portable to other platforms.

Credit is due to Wim Lewis, whose work on reverse engineering the alias
format was extremely useful in writing this code.
