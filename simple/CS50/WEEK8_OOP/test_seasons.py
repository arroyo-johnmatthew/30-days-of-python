import pytest
from datetime import date
from seasons import num_to_words, validate_bday, get_age_in_min

def test_num_to_words():
    assert num_to_words(525600) == "Five hundred twenty-five thousand, six hundred minutes"
    assert num_to_words(527040) == "Five hundred twenty-seven thousand forty minutes"
    assert num_to_words(1051200) == "One million, fifty-one thousand, two hundred minutes"
    assert num_to_words(11327040) == "Eleven million, three hundred twenty-seven thousand forty minutes"

def test_mins():
    assert get_age_in_min(date(2026, 1, 1), date(2025, 1, 1)) == 525600
    assert get_age_in_min(date(2025, 1, 1), date(2024, 1, 1)) == 527040
    assert get_age_in_min(date(2026, 7, 16), date(2026, 7, 15)) == 1440
    assert get_age_in_min(date(2026, 7, 16), date(2005, 1, 1)) == 11327040

def test_validation():
    format = r"^([1-9][0-9]{3})-((?:0[1-9]|1[0-2]))-((?:0[1-9]|[12][0-9]|3[01]))$"

    with pytest.raises(SystemExit):
        validate_bday("2026/07/16", format)
    with pytest.raises(SystemExit):
        validate_bday("07-16-2026", format)
    with pytest.raises(SystemExit):
        validate_bday("July 16, 2026", format)

