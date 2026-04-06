#Testing the vanity plate code.

from plates import is_valid
import pytest

def test_alpha():
    assert is_valid("Avineak") == False
    assert is_valid("Singh0") == False
    assert is_valid("AS") == True


def test_numbers():
    assert is_valid("Bro2005") == False
    assert is_valid("1982JoJo") == False
    assert is_valid("AAA22A") == False
    assert is_valid("AA2A2") == False

   
    assert is_valid("AAA222") == True
    assert is_valid("AA10") == True

def test_check():
    assert is_valid("ASR205") == True
    assert is_valid("Jatt40") == True
    assert is_valid("AB!") == False
    assert is_valid("A1") == False
    assert is_valid("12") == False
    assert is_valid("1AA") == False
    assert is_valid("A") == False
    assert is_valid("OUTATIME") == False


