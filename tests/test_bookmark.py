from mac_alias import Bookmark


def test_simple_bookmark():
    b = Bookmark.for_file("/Applications")

    assert b is not None
