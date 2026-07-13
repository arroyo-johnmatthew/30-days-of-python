import pytest
from working import convert, get_format

def test_conversion():
    assert convert("9 AM to 5 PM") == ("09:00 to 17:00")
    assert convert("9:00 AM to 5:00 PM") == ("09:00 to 17:00")
    assert convert("10 AM to 8:50 PM") == ("10:00 to 20:50")
    assert convert("10:30 PM to 8 AM") == ("22:30 to 08:00")

def test_error():
    with pytest.raises(ValueError):
        convert("9:60 AM to 5:60 PM")
    with pytest.raises(ValueError):
        convert("9 AM - 5 PM")
    with pytest.raises(ValueError):
        convert("09:00 AM - 17:00 PM")

def test_format():
    assert get_format("1", "PM") == "13"
    assert get_format("1", "AM") == "01"
    assert get_format("12", "PM") == "12"
    assert get_format("12", "AM") == "00"
    assert get_format("7", "PM") == "19"
    assert get_format("7", "AM") == "07"
    assert get_format("1", "am") == "incorrect time or type"
    assert get_format("1", "pm") == "incorrect time or type"
    assert get_format("1", "ampm") == "incorrect time or type"
    