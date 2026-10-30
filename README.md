# mac_alias

[![Python Versions](https://img.shields.io/pypi/pyversions/mac_alias.svg)](https://pypi.python.org/pypi/mac_alias) [![PyPI Version](https://img.shields.io/pypi/v/mac_alias.svg)](https://pypi.python.org/pypi/mac_alias) [![Maturity](https://img.shields.io/pypi/status/mac_alias.svg)](https://pypi.python.org/pypi/mac_alias) [![MIT License](https://img.shields.io/pypi/l/mac_alias.svg)](https://github.com/dmgbuild/mac_alias/blob/main/LICENSE) [![Build status](https://github.com/dmgbuild/mac_alias/workflows/CI/badge.svg?branch=main)](https://github.com/dmgbuild/mac_alias/actions)

`mac_alias` lets you generate or read binary Alias and Bookmark records from Python code.

While it is written in pure Python, some macOS specific code is required to generate a proper Alias or Bookmark record for a given file, so this module currently is not portable to other platforms.

Credit is due to Wim Lewis <wiml@hhhh.org>, whose work on reverse engineering the alias format was extremely useful in writing this code.  Alastair Houghton <alastair@alastairs-place.net> was responsible for reverse engineering the bookmark format.

See the [documentation](https://mac-alias.readthedocs.io) for more information.
