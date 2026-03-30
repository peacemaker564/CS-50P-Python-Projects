import pytest
from twttr import shorten

def test_upper():
    assert shorten("AVI") == "V"
    assert shorten("MUMMA") == "MMM"

def test_lower():
    assert shorten("avi") == "v"
    assert shorten("mumma") == "mmm"

def test_intg():
    assert shorten("CS50") == "CS50"

def test_punctuation():
    assert shorten("Sup!?") == "Sp!?"
    





