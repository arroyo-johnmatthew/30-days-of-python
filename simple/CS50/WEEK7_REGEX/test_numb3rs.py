from numb3rs import validate

# These are the unit tests I did to test the number ranges (0-99, 100-199, 200-249, and 250-255)
# def test_0_to_99():
#     assert validate("0") == True
#     assert validate("98") == True
#     assert validate("99") == True

# def test_100_to_199():
#     assert validate("100") == True
#     assert validate("101") == True
#     assert validate("199") == True

# def test_200_to_249():
#     assert validate("200") == True
#     assert validate("201") == True
#     assert validate("248") == True
#     assert validate("249") == True

# def test_250_to_255():
#     assert validate("250") == True
#     assert validate("254") == True
#     assert validate("255") == True
#     assert validate("256") == False

# def zero_trailings():
#     assert validate("000") == False
#     assert validate("001") == False
#     assert validate("012") == False
#     assert validate("099") == False
#     assert validate("00") == False
#     assert validate("09") == False
#     assert validate("009") == False

def test_ip():
    assert validate("1.2.3.4") == True
    assert validate("127.0.0.1") == True
    assert validate("255.255.255.255") == True
    assert validate("512.512.512.512") == False
    assert validate("1.2.3.1000") == False
    assert validate("192.168.001.1") == False
    assert validate("cat") == False