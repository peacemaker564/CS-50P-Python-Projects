import pytest
from bank import value

def test_hello():
    assert value("Hello, Avi.") == 0
    assert value("hello, brah!56") == 0

def test_h():
    assert value("Hi, Avi.") == 20
    assert value("hi, brah!56") == 20
    assert value("How are you? , Avi.") == 20
    assert value("Hohooho, brah!56") == 20

def test_non():
    assert value("Sup ? Avi.") == 100
    assert value("Yoo, mate.!") == 100





