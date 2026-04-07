import pytest
from fuel import gauge
from fuel import convert

def test_convert():
    assert convert("1/4") == 25
    assert convert("1/100") == 1
    assert convert("1/1") == 100
    # Test that it raises errors
    with pytest.raises(ZeroDivisionError):
        convert("1/0")
    with pytest.raises(ValueError):
        convert("three/four")
    with pytest.raises(ValueError):
        convert("-1/4")

def test_gauge():
    assert gauge(1) == "E"
    assert gauge(0) == "E"
    assert gauge(99) == "F"
    assert gauge(100) == "F"
    assert gauge(50) == "50%"
