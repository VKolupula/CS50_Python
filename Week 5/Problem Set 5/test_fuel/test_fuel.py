from fuel import convert
from fuel import gauge
import pytest

def main():
    test_convert()
    test_gauge()
    test_ZeroDivisionError()

def test_convert():
    assert convert("2/4") == 50
    assert convert("4/4") == 100
    with pytest.raises(ValueError):
        convert("1/%")

def test_gauge():
    assert gauge(75) == "75%"
    assert gauge(0) == "E"
    assert gauge(1) == "E"
    assert gauge(99) == "F"
    assert gauge(100) == "F"

def test_ZeroDivisionError():
    with pytest.raises(ZeroDivisionError):
        convert("100/0")
        convert("4/0")

if __name__ == "__main__":
    main()

