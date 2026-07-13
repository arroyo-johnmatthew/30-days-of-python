from response import validate

def test_emails():
    assert validate("johnmatthewarroyo2@gmail.com") == "Valid"
    assert validate("malan@harvard.edu") == "Valid"
    assert validate("malan@@@harvard.edu") == "Invalid"
    assert validate("johnmatthewarroyo2@gmail..com") == "Invalid"