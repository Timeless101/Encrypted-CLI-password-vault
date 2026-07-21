from src.validator import password_match_checker

def test_password_match():
    assert password_match_checker("password", "password") is True

def test_password_match_false():
    assert password_match_checker("password", "fake") is False