#Testing the vanity plate code.

from plates import is_valid
import pytest

def test_alpha():
    assert is_valid("Avineak") == True
    assert is_valid("Singh0") == False
    assert is_valid("AS") == True


def test_numbers():
    assert is_valid("Bro2005") == True
    assert is_valid("1982JoJo") == False

def test_check():
    assert is_valid("ASR205") == True
    assert is_valid("Jatt40") == True
    assert is_valid("AB!") == False
    assert is_valid("A1") == False
    assert is_valid("12") == False
    assert is_valid("1AA") == False
    assert is_valid("A") == False
    assert is_valid("OUTATIME") == True


