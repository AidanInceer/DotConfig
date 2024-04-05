from pytest import fixture

from dotdict import DotDict


@fixture
def test_dict() -> dict:
    return {"A": [1, 2, 3, 4], "B": {"C": 5}, "D": "E", "F": None}


def test_dot_dict_00(test_dict: dict):
    ddict = DotDict(test_dict)
    expected = test_dict["A"]
    actual = ddict.A

    assert actual == expected


def test_dot_dict_01(test_dict: dict):
    ddict = DotDict(test_dict)
    expected = test_dict["B"]
    actual = ddict.B

    assert actual != expected


def test_dot_dict_02(test_dict: dict):
    ddict = DotDict(test_dict)
    expected = test_dict["F"]
    actual = ddict.F

    assert actual == expected


def test_dot_dict_03(test_dict: dict):
    ddict = DotDict(test_dict)
    ddict.F = "Hello World"

    assert ddict.F == "Hello World"


def test_dot_dict_04():
    ddict = DotDict({"A": 1})
    actual = repr(ddict)

    assert actual == "DotDict: {A: 1}"
