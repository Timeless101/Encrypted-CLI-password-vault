from src.validator import email_checker

def test_email_checker_wrong():
    assert email_checker("@@@") is False

def test_email_cheker_good():
    assert email_checker("fake@fake.com") is True