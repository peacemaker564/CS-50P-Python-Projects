#Testing the vanity plate code.

from plates import is_valid
import pytest

def test_alpha():
    assert is_valid("Avineak") == False
    assert is_valid("Singh0") == False
    assert is_valid("AS2005") == True

def test_numbers():
    assert is_valid("Bro2005") == False
    assert is_valid("1982JoJo") == False

def test_check():
    assert is_valid("ASR205") == True
    assert is_valid("Jatt40") == True


