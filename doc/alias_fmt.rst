Mac Alias Format
================

*Everything below is big-endian.*

An Alias record starts as follows:

====== ==== ========
Offset Size Contents
====== ==== ========
0      4    Application specific four-character code
4      2    Record size (must be >= 150 bytes)
6      2    Version (we support version 2)
8      2    Alias kind (0 = file, 1 = folder)
10     28   Volume name (Pascal-style string; first octet gives length)
38     4    Volume date (seconds since 1904-01-01 00:00:00 UTC)
42     2    Filesystem type (typically 'H+' for HFS+)
44     2    Disk type (0 = fixed, 1 = network, 2 = 400Kb, 3 = 800kb, 4 = 1.44MB, 5 = ejectable)
46     4    CNID of containing folder
50     64   Target name (Pascal-style string)
114    4    Target CNID
118    4    Target creation date (seconds since 1904-01-01 00:00:00 UTC)
122    4    Target creator code (four-character code)
126    4    Target type code (four-character code)
130    2    Number of directory levels from alias to root (or -1)
132    2    Number of directory levels from root to target (or -1)
134    4    Volume attributes
138    2    Volume filesystem ID
140    10   Reserved (set to zero)
====== ==== ========

This record is optionally followed by tag-length-value data:

====== ====== ========
Offset Size   Contents
====== ====== ========
0      2      Tag
2      2      Length
4      Length Value
====== ====== ========

If the length is odd, a pad byte is added at the end.

Valid tags are:

====== ========
Tag    Contents
====== ========
-1     Signifies the end of the alias record
0      Carbon folder name (a string)
1      CNID path (an array of CNIDs, one per directory)
2      Carbon path (a string)
3      AppleShare zone (a string)
4      AppleShare server name (a string)
5      AppleShare username (a string)
6      Driver name (a string)
9      Network mount information
10     Dial-up connection information
14     Unicode filename of target (a UTF-16 big endian string)
15     Unicode volume name (a UTF-16 big endian string)
16     High resolution volume creation date (65536ths of a second since 1904-01-01 00:00:00 UTC)
17     High resolution creation date (65536ths of a second since 1904-01-01 00:00:00 UTC)
18     POSIX path (a string)
19     POSIX path to volume mountpoint (a string)
20     Recursive alias of disk image (an alias record)
21     User home length prefix (two-byte integer, says how many directory levels to the user's home folder)
====== ========

