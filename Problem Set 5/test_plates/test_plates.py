from plates import is_valid

def main():
    test_isvalid_at_least_2()
    test_isvalid_range()
    test_isvalid_num_middle()
    test_isvalid_punctuation()
    test_isvalid_without_beg_alph()
    test_isvalid_zero_plac()

def test_isvalid_at_least_2():
    assert is_valid("N") == False
    assert is_valid("Hel") == True
    assert is_valid("NRVOUS") == True

def test_isvalid_range():
    assert is_valid("CS50") == True
    assert is_valid("ECTO88") == True
    assert is_valid("OUTATIME") == False

def test_isvalid_num_middle():
    assert is_valid("AAA22A") == False
    assert is_valid("AAA222") == True
    assert is_valid("CS50P2") == False

def test_isvalid_punctuation():
    assert is_valid("PI3.14") == False
    assert is_valid("PI*.14") == False

def test_isvalid_without_beg_alph():
    assert is_valid("14cs50") == False
    assert is_valid("14cs") == False
    assert is_valid("14") == False

def test_isvalid_zero_plac():
    assert is_valid("AAA050") == False
    assert is_valid("ECT088") == False
    assert is_valid("CS50") == True


if __name__ == "__main__":
    main()