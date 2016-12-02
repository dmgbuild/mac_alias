Mac Bookmark Format
===================

*Everything below is little-endian unless otherwise mentioned.*

The Bookmark format is a more modern alternative to the alias record.
Bookmarks consist of a set of dictionaries mapping keys to values; each
dictionary has its own Table of Contents (TOC) structure.

The record starts with a header:

====== ==== ========
Offset Size Contents
====== ==== ========
0      4    Magic number ('book')
4      4    Total size in bytes
8      4    Unknown (0x10040000) - might be a version?
12     4    Size of header (48)
16     32   Reserved
====== ==== ========

All offsets stored in the file are relative to the *end* of this header.

This is immediately followed at location 48 by a 4-byte offset to the first
TOC structure.  It seems odd that this is not part of the header, but for
some reason best known to the engineers at Apple, it isn't.

A TOC starts with its own header:

====== ==== ========
Offset Size Contents
====== ==== ========
0      4    Size of TOC in bytes, minus 8
4      4    Magic number (0xfffffffe)
8      4    Identifier (just a number)
12     4    Next TOC offset (or 0 if none)
16     4    Number of entries in this TOC
====== ==== ========

This is followed by an array of TOC entries.  There is code that does a
binary search of the TOC structure, so they *must* be stored in *key* order.
A TOC entry looks like this:

====== ==== ========
Offset Size Contents
====== ==== ========
0      4    Key
4      4    Offset to data record
8      4    Reserved (0)
====== ==== ========

If the key has its top bit set (0x80000000), then (key & 0x7fffffff) gives the
offset of a string record.

Each data record has the following fields:

====== ==== ========
Offset Size Contents
====== ==== ========
0      4    Length of data (n)
4      4    Type
8      n    Data bytes
====== ==== ========

Known data types are as follows:

====== ====================== ========
Code   Type                   Encoding
====== ====================== ========
0x0101 String                 UTF-8
0x0201 Data                   Raw bytes
0x0301 Number (signed 8-bit)  1-byte number
0x0302 Number (signed 16-bit) 2-byte number
0x0303 Number (signed 32-bit) 4-byte number
0x0304 Number (signed 64-bit) 8-byte number
0x0305 Number (32-bit float)  IEEE single precision
0x0306 Number (64-bit float)  IEEE double precision
0x0400 Date                   *Big-endian* IEEE double precision seconds since 2001-01-01 00:00:00 UTC
0x0500 Boolean (false)        No data
0x0501 Boolean (true)         No data
0x0601 Array                  Array of 4-byte offsets to data items
0x0701 Dictionary             Array of pairs of 4-byte (key, value) data item offsets
0x0801 UUID                   Raw bytes
0x0901 URL                    UTF-8 string
0x0902 URL (relative)         4-byte offset to base URL, 4-byte offset to UTF-8 string
====== ====================== ========

The first TOC in the file generally has its identifier set to 1.  As
mentioned, the keys in each TOC can be strings, in which case the key field
will contain the offset to the string, or they can be certain special values.
Currently known values are:

====== ======================= =====
Key    Meaning                 Value
====== ======================= =====
0x1003 Unknown                 Unknown
0x1004 Target path             Array of individual path components
0x1005 Target CNID path        Array of CNIDs
0x1010 Target flags            Data - see below
0x1020 Target filename         String
0x1030 Target CNID             4-byte integer
0x1040 Target creation date    Date
0x1054 Unknown                 Unknown
0x1055 Unknown                 Unknown
0x1056 Unknown                 Unknown
0x1101 Unknown                 Unknown
0x1102 Unknown                 Unknown
0x2000 TOC path                Array - see below
0x2002 Volume path             Array of individual path components
0x2005 Volume URL              URL of volume root
0x2010 Volume name             String
0x2011 Volume UUID             String (not a UUID!)
0x2012 Volume size             8-byte integer
0x2013 Volume creation date    Date
0x2020 Volume flags            Data - see below
0x2030 Volume is root          True if the volume was the filesystem root
0x2040 Volume bookmark         TOC identifier for disk image
0x2050 Volume mount point      URL
0x2070 Unknown                 Unknown
0xc001 Containing folder index Integer index of containing folder in target path array
0xc011 Creator username        Name of user that created bookmark
0xc012 Creator UID             UID of user that created bookmark
0xd001 File reference flag     True if creating URL was a file reference URL
0xd010 Creation options        Integer containing flags passed to CFURLCreateBookmarkData
0xe003 URL length array        Array of integers - see below
0xf017 Localized name?         String?
0xf022 Unknown                 Unknown
0xf080 Security extension      Unknown but looks like a hash with data and an access right
0xf081 Unknown                 Unknown
====== ======================= =====

The target flags (0x1010) are encoded as a Data object containing three 8-byte
integers.  The first contains flags describing the target; the second says
which flags are valid, and the third appears to always be zero.  Supported
flags can be found in CFURLPriv.h, which is part of CF-Lite; for the target
flags field, it's the "resource property flags" that are valid.

Similarly the volume flags (0x2020) are encoded in the same manner, but this
time it's the "volume property flags" that are interesting.

The TOC path (0x2000) is only used if there are multiple volumes between the
target and the filesystem root.  In that case, it contains an array, with
every other item holding a TOC ID for a dictionary describing a volume; the
values between TOC IDs appear to be zero.  The array starts from the
filesystem root.

The URL length array (0xe003) is used to indicate how the path components were
originally broken up; if the URL encoded by the bookmark has a base URL, each
entry in the length array gives the number of path elements that come from
that base URL.
