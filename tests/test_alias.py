from mac_alias import Alias


def test_simple_alias():
    a = Alias.for_file("/Applications")

    assert a is not None
