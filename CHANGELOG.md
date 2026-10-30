# Release History

<!-- towncrier release notes start -->

## 2.2.3 (2025-12-04)

### Features

* Support for Python 3.13, 3.14 and 3.15 was added.

### Backward Incompatible Changes

* Support for Python 3.7, 3.8 and 3.9 was dropped.

### Misc

* [#204](https://github.com/dmgbuild/mac_alias/issues/204), [#24](https://github.com/dmgbuild/mac_alias/issues/24)

## 2.2.2 (2022-12-06)

### Bugfixes

* `kBookmarkVolumePath` and `kBookmarkVolumeURL` are now correctly exported from the top-level package. ([#20](https://github.com/dmgbuild/mac_alias/issues/20))

## 2.2.1 (2022-11-24)

### Features

* The project now uses a PEP 517 compliant build configuration, and declares Python 3.7 to 3.12 as supported versions. ([#19](https://github.com/dmgbuild/mac_alias/issues/19))

### Bugfixes

* A stray entry in Alias serialization was removed. ([#12](https://github.com/dmgbuild/mac_alias/issues/12))

### Backward Incompatible Changes

* Support for Python 2, and Python 3 versions prior to 3.7 was dropped.

### Misc

* [#13](https://github.com/dmgbuild/mac_alias/issues/13), [#14](https://github.com/dmgbuild/mac_alias/issues/14), [#16](https://github.com/dmgbuild/mac_alias/issues/16), [#17](https://github.com/dmgbuild/mac_alias/issues/17)

## 2.2.0 (2020-12-08)

### Features

* `osx.py` was updated with definitions from macOS 11 (Big Sur).

### Bugfixes

* `statfs` and `fstatfs` are now correctly located on ARM64 (Apple Silicon) machines. ([#11](https://github.com/dmgbuild/mac_alias/issues/11))

## 2.1.1 (2020-11-28)

### Bugfixes

* A `NameError` when reading an Alias from a file descriptor was corrected. ([#9](https://github.com/dmgbuild/mac_alias/issues/9))

## 2.1.0 (2020-10-11)

### Features

* Tentative support for the Alias v3 format was added.

### Bugfixes

* Volume paths are now normalized to NFC form before being compared, avoiding Unicode string comparison issues. ([#7](https://github.com/dmgbuild/mac_alias/issues/7))

## 2.0.7 (2018-02-13)

### Bugfixes

* A number of Python 3 compatibility problems were corrected. ([#3](https://github.com/dmgbuild/mac_alias/issues/3))

## 2.0.6 (2017-08-02)

### Features

* Bookmarks can now be parsed from `bytearray` data.

### Bugfixes

* Stray debugging `print` statements were removed from bookmark generation.

## 2.0.5 (2017-08-02)

### Bugfixes

* Byte strings are now used with `struct.pack`, correcting a Python 3 compatibility problem.

## 2.0.4 (2017-07-28)

### Bugfixes

* A number of Python 3 compatibility problems were corrected.

## 2.0.2 (2017-07-27)

### Features

* A basic test suite was added.

### Bugfixes

* A number of Python 3 compatibility problems were corrected.

## 2.0.1 (2017-04-28)

### Bugfixes

* Generated bookmarks now use generic ("nobody") user information, rather than details of the author.

## 2.0.0 (2016-12-02)

### Features

* Support for reading and generating Bookmark records was added.

## 1.1.0 (2015-10-19)

### Bugfixes

* Values provided to the `TargetInfo` initializer are now used, rather than being ignored.
* Floor division is now used explicitly where required, correcting Python 3 compatibility.
* The `TAG_APPLESHARE_SERVER_NAME` tag value was corrected.
* The full path to `libc` is now used, correcting a problem on OS X 10.11 (El Capitan).

## 1.0.0 (2014-02-13)

* Initial release.
