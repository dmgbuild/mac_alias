# mac_alias package

## Classes

::: mac_alias.Alias

::: mac_alias.AppleShareInfo

::: mac_alias.VolumeInfo

::: mac_alias.TargetInfo

::: mac_alias.Bookmark

::: mac_alias.Data

::: mac_alias.URL

## Constants

`ALIAS_KIND_FILE`
`ALIAS_KIND_FOLDER`
:   Values for the [`TargetInfo.kind`][mac_alias.TargetInfo.kind] attribute.

`ALIAS_HFS_VOLUME_SIGNATURE`
:   The volume signature for HFS+.

`ALIAS_FILESYSTEM_UDF`
`ALIAS_FILESYSTEM_FAT32`
`ALIAS_FILESYSTEM_EXFAT`
`ALIAS_FILESYSTEM_HFSX`
`ALIAS_FILESYSTEM_HFSPLUS`
`ALIAS_FILESYSTEM_FTP`
`ALIAS_FILESYSTEM_NTFS`
`ALIAS_FILESYSTEM_UNKNOWN`
:   Values returned by the
    [`VolumeInfo.fs_type`][mac_alias.VolumeInfo.fs_type]
    attribute.

`ALIAS_FIXED_DISK`
`ALIAS_NETWORK_DISK`
`ALIAS_400KB_FLOPPY_DISK`
`ALIAS_800KB_FLOPPY_DISK`
`ALIAS_1_44MB_FLOPPY_DISK`
`ALIAS_EJECTABLE_DISK`
:   Disk type constants.

`ALIAS_NO_CNID`
:   A constant used where no CNID is present.

`kBookmarkURL`
`kBookmarkPath`
`kBookmarkCNIDPath`
`kBookmarkFileProperties`
`kBookmarkFileName`
`kBookmarkFileID`
`kBookmarkFileCreationDate`
`kBookmarkTOCPath`
`kBookmarkVolumePath`
`kBookmarkVolumeURL`
`kBookmarkVolumeName`
`kBookmarkVolumeUUID`
`kBookmarkVolumeSize`
`kBookmarkVolumeCreationDate`
`kBookmarkVolumeProperties`
`kBookmarkContainingFolder`
`kBookmarkUserName`
`kBookmarkUID`
`kBookmarkWasFileReference`
`kBookmarkCreationOptions`
`kBookmarkURLLengths`
`kBookmarkDisplayName`
`kBookmarkIconData`
`kBookmarkIconRef`
`kBookmarkTypeBindingData`
`kBookmarkCreationTime`
`kBookmarkSandboxRwExtension`
`kBookmarkSandboxRoExtension`
`kBookmarkAliasData`
`kBookmarkSecurityExtension`
:   Bookmark data keys. A Bookmark holds a set of TOCs (Tables of Contents), each of which maps a set of keys to a set of values. The keys are either numeric, like the ones represented by the above constants, or strings.

    Bookmarks can hold strings, byte data, numbers, dates, booleans, arrays, dicts, UUIDs, URLs and NULLs (represented by Python `None`). If you store data in a bookmark using the string key functionality, the documentation for CF/NSURL recommends using reverse DNS for the keys to avoid clashes.
