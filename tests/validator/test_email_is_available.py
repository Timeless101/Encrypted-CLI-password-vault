from src.validator import email_is_available

def test_email_isnot_available():
    assert email_is_available("fake@fake.com", "fake@fake.com") is False

def test_email_is_available_none():
    assert email_is_available(None, "fake@fake.com") is True

def test_email_is_available():
    assert email_is_available("fakefake@fake.com", "fake@fake.com") is True