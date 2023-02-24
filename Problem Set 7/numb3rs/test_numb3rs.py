from numb3rs import validate

def main():
    test_Non_numb()
    test_valid_IP()
    test_Invalid_IP()

def test_Non_numb():
    assert validate("cat") == False
    assert validate("dog.1.1.1") == False
    assert validate("dog.1.%.1") == False
    assert validate("1") == False


def test_valid_IP():
    assert validate("127.0.0.1") == True
    assert validate("255.255.255.255") == True
    assert validate("1.2.3.4") == True

def test_Invalid_IP():
    assert validate("512.512.512.512") == False
    assert validate("256.0.25.25") == False
    assert validate("255.255.500.500") == False
    assert validate("0.0.500.500") == False


if __name__ == "__main__":
    main()

