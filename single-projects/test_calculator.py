from calculator import count_vowels

def test_vowels():
    assert count_vowels("Hello") == 2
    assert count_vowels("He l lo") == 2
    assert count_vowels("John Matthew Arroyo") == 6

def test_consonants():
    assert count_vowels("BGC") == 0
    assert count_vowels("LRT") == 0

def test_uppercase():
    assert count_vowels("HELLO") == 2
    assert count_vowels("HE L LO") == 2
    assert count_vowels("JOHN MATTHEW ARROYO") == 6

def test_lowercase():
    assert count_vowels("hello") == 2
    assert count_vowels("he l lo") == 2
    assert count_vowels("john matthew arroyo") == 6