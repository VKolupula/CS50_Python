from working import convert
import pytest

def main():
    test_valueerror()
    test_non_num()
    test_valid()

def test_valueerror():
    with pytest.raises(ValueError):
        convert("9 AM to 5 P")
    with pytest.raises(ValueError):
        convert("0 AM to 0 PM")
    with pytest.raises(ValueError):
        convert("10:10  to 12:30 ")
    with pytest.raises(ValueError):
        convert("9 AM - 5 PM")
    with pytest.raises(ValueError):
        convert("09:00 AM - 17:00 PM")

def test_non_num():
    with pytest.raises(ValueError):
        convert("cat to dog")

def test_valid():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("12 AM to 12 PM") == "00:00 to 12:00"

if __name__ == "__main__":
    main()

