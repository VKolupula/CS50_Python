from jar import Jar
import pytest

def main():
    test_init()
    test_str()

def test_init():
    jar = Jar(2)
    assert jar.capacity == 2
    assert jar.size == 0
    with pytest.raises(ValueError):
        jar = Jar(-1)
    jar= Jar()
    assert jar.capacity == 12

def test_str():
    jar = Jar(4)
    assert str(jar) == ""
    jar.deposit(4)
    assert str(jar) == "🍪🍪🍪🍪"
    jar = Jar()
    jar.deposit(12)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"

def test_withdraw():
    jar = Jar()
    jar.deposit(8)
    assert jar.size == 8
    jar.withdraw(4)
    assert jar.size == 4
    assert str(jar) == "🍪🍪🍪🍪"

def test_valueerror():
    jar =Jar()
    with pytest.raises(ValueError):
        jar.deposit(13)
    jar.deposit(4)
    assert jar.size == 4
    with pytest.raises(ValueError):
        jar.withdraw(5)

if __name__ == "__main__":
    main()