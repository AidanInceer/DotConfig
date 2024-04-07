from pytest import fixture

from dotcon import DotConfig


@fixture
def test_dict() -> dict:
    return {"A": [1, 2, 3, 4], "B": {"C": 5}, "D": "E", "F": None}


def test_dot_dict_00(test_dict: dict):
    ddict = DotConfig(test_dict)
    expected = test_dict["A"]
    actual = ddict.A

    assert actual == expected


def test_dot_dict_01(test_dict: dict):
    ddict = DotConfig(test_dict)
    expected = test_dict["B"]
    actual = ddict.B

    assert actual != expected


def test_dot_dict_02(test_dict: dict):
    ddict = DotConfig(test_dict)
    expected = test_dict["F"]
    actual = ddict.F

    assert actual == expected


def test_dot_dict_03(test_dict: dict):
    ddict = DotConfig(test_dict)
    ddict.F = "Hello World"

    assert ddict.F == "Hello World"


def test_dot_dict_04():
    ddict = DotConfig({"A": 1})
    actual = repr(ddict)

    assert actual == "DotConfig: {A: 1}"


def test_dot_dict_05():
    ddict = DotConfig({"A": [1, 2, 3]})

    actual = ddict.to_dict()

    assert {"A": [1, 2, 3]} == actual


def test_dot_dict_06():
    ddict = DotConfig({".A": [1, 2, 3]})

    actual = ddict[".A"]

    assert [1, 2, 3] == actual


def test_dot_dict_07():
    ddict = DotConfig({"A": [1, 2, 3], "B": [4, 5, 6]})

    ddict.pop("A")

    actual = ddict.to_dict()

    assert {"B": [4, 5, 6]} == actual


def test_dot_dict_08():
    ddict = DotConfig({"A": [1, 2, 3], "B": [4, 5, 6]})

    actual = ddict.keys()

    assert ["A", "B"] == actual
