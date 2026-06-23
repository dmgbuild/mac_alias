from mac_alias import Bookmark


def test_simple_bookmark():
    b = Bookmark.for_file("/Applications")

    assert b is not None


def test_read_bookmark():
    st = open("tests/56b_header", "rb")
    try:
        b = Bookmark.from_bytes(st.read())
    finally:
        st.close()
    assert b is not None
