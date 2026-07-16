import pytest
from jar import Jar

@pytest.fixture
def default_jar():
    return Jar()

def test_str(default_jar):
    assert str(default_jar) == ""
    default_jar.deposit(5) 
    assert str(default_jar) == "🍪🍪🍪🍪🍪"
    default_jar.deposit(2) 
    assert str(default_jar) == "🍪🍪🍪🍪🍪🍪🍪"

def test_deposit(default_jar):
    # Deposit 10 so size = 10
    default_jar.deposit(10)
    assert default_jar.size == 10

    # Deposit 3 so size = 13, which should throw an error
    with pytest.raises(ValueError, match="Cant fit it all those cookies!"):
        default_jar.deposit(3)

def test_withdraw(default_jar):
    default_jar.deposit(12)
    default_jar.withdraw(2)

    # Now, cookie jar size is now 10
    assert default_jar.size == 10
    default_jar.withdraw(10)

    # Now it is 0
    assert default_jar.size == 0

    # Now get a cookie from the empty jar, it should display an error
    with pytest.raises(ValueError, match="Not enough cookies to take!"):
        default_jar.withdraw(1)

    # Refill the jar then take cookies more than the size of the current
    default_jar.deposit(10)
    with pytest.raises(ValueError, match="Not enough cookies to take!"):
        default_jar.withdraw(11)




