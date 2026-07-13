from working import convert

def test_validity():
    assert convert("9:00 AM to 5:00 PM") == True
    assert convert("9 AM to 5 PM") == True
    assert convert("9:00 AM to 5 PM") == True
    assert convert("9 AM to 5:00 PM") == True
