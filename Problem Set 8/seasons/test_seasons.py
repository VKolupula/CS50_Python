from datetime import date
from seasons import convert_age_minutes
import pytest

def main():
    test_valueerror()
    test_valid()

def test_valueerror():
    with pytest.raises(ValueError):
        convert_age_minutes(date.fromisoformat("1996-29-09"))

def test_valid():
    assert convert_age_minutes(date.fromisoformat("1996-09-20"))  == "Thirteen million, eight hundred eighty thousand, one hundred sixty minutes"

if __name__ == "__main__":
    main()
