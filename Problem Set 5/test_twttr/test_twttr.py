from twttr import shorten

def main():
    test_lower_shorten()
    test_upper_shorten()
    test_numbers_shorten()
    test_punctuation_shorten()

def test_lower_shorten():
    assert shorten("twitter") == "twttr"

def test_upper_shorten():
    assert shorten("TWITTER") == "TWTTR"

def test_numbers_shorten():
    assert shorten("12345") == "12345"

def test_punctuation_shorten():
    assert shorten("$%&*.") == "$%&*."


if __name__ == "__main__":
    main()