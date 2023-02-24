from um import count
def main():
    test_single()
    test_single_character()
    test_inside_word()
    test_multiple()
    test_case_insensitively()

def test_single():
    assert count("um") == 1
def test_single_character():
    assert count("um,") == 1
def test_inside_word():
    assert count("Um, thanks for the album.") == 1
def test_multiple():
    assert count("Um, thanks, um..., um um") == 4
def test_case_insensitively():
    assert count("UM") == 1
    assert count("UM um") == 2
    assert count("Um uM, um") == 3

if __name__ == "__main__":
    main()