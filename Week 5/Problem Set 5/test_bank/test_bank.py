from bank import value

def main():
    test_lower_value()
    test_upper_value()
    test_numbers_value()
    test_punctuation_value()

def test_lower_value():
    assert value("hello") == 0
    assert value("how you doing") == 20
    assert value("what happening") == 100

def test_upper_value():
    assert value("HELLO") == 0
    assert value("HOW YOU DOING") == 20
    assert value("WHAT HAPPENING") == 100

def test_numbers_value():
    assert value("hello 123456") == 0
    assert value("how you doing 12434") == 20
    assert value("what happening 1234") == 100


def test_punctuation_value():
    assert value("hello!") == 0
    assert value("how you doing?") == 20
    assert value("what's happening?") == 100

if __name__ == "__main__":
    main()