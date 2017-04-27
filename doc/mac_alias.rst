mac_alias package
=================

.. currentmodule:: mac_alias

Classes
-------

.. autoclass:: Alias
   :members:
   :undoc-members:

.. autoclass:: AppleShareInfo
   :members:
   :undoc-members:

.. autoclass:: TargetInfo
   :members:
   :undoc-members:

.. autoclass:: Bookmark
   :members:
   :undoc-members:

.. autoclass:: Data
   :members:
   :undoc-members:

.. autoclass:: URL
   :members:
   :undoc-members:

Constants
---------

.. py:data:: ALIAS_KIND_FILE
             ALIAS_KIND_FOLDER

   Values for the :attr:`~mac_alias.Alias.kind` attribute.

.. py:data:: ALIAS_HFS_VOLUME_SIGNATURE

   The volume signature for HFS+.

.. py:data:: ALIAS_FIXED_DISK
             ALIAS_NETWORK_DISK
             ALIAS_400KB_FLOPPY_DISK
             ALIAS_800KB_FLOPPY_DISK
             ALIAS_1_44MB_FLOPPY_DISK
             ALIAS_EJECTABLE_DISK

   Disk type constants.

.. py:data:: ALIAS_NO_CNID

   A constant used where no CNID is present.

.. py:data:: kBookmarkPath
             kBookmarkCNIDPath
             kBookmarkFileProperties
             kBookmarkFileName
             kBookmarkFileID
             kBookmarkFileCreationDate
             kBookmarkTOCPath
             kBookmarkVolumePath
             kBookmarkVolumeURL
             kBookmarkVolumeName
             kBookmarkVolumeUUID
             kBookmarkVolumeSize
             kBookmarkVolumeCreationDate
             kBookmarkVolumeProperties
             kBookmarkContainingFolder
             kBookmarkUserName
             kBookmarkUID
             kBookmarkWasFileReference
             kBookmarkCreationOptions
             kBookmarkURLLengths
             kBookmarkSecurityExtension

   Bookmark data keys.  A Bookmark holds a set of TOCs (Tables of Contents),
   each of which maps a set of keys to a set of values.  The keys are either
   numeric, like the ones represented by the above constants, or strings.

   Bookmarks can hold strings, byte data, numbers, dates, booleans, arrays,
   dicts, UUIDs, URLs and NULLs (represented by Python None).  If you store
   data in a bookmark using the string key functionality, the documentation
   for CF/NSURL recommends using reverse DNS for the keys to avoid clashes.
