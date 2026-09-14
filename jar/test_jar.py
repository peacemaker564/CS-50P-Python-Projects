from jar import Jar
import pytest


def test_init():
    jar = Jar() #SHould have default cap = 12
    assert jar.capacity == 12

    jar2 = Jar(15)
    assert jar2.capacity == 15


    ...


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar(15)
    jar.deposit(12) #Non property method
    assert jar.size == 12 #Property method

    with pytest.raises(ValueError):
        jar.deposit(-1)


def test_withdraw():
    jar = Jar(5)
    jar.deposit(2)
    assert jar.size == 2

    jar.withdraw(2)
    assert jar.size == 0

    with pytest.raises(ValueError):
        jar.withdraw(1)

    with pytest.raises(ValueError):
        jar.withdraw(-1)

