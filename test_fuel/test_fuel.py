import pytest
from fuel import gauge
from fuel import convert

def test_one():
    assert convert("1/4") == 25
    assert convert("1/1") == 100
    assert convert("0/1") == 0

def test_two():
    assert gauge(25) == "25%"
    assert gauge(100) == "F"
    assert gauge(99) == "F"

    assert gauge(1) == "E"
    assert gauge(0) == "E"

def test_valueError():
    with pytest.raises("ValueError"):
        convert("three/four")


def test_ZeroDivisionError():
    with pytest.raises("ZeroDivError"):
        convert("1/0")
