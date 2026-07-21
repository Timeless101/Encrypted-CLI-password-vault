from src.validator import main_menu_validator

def test_menu_validator():
    assert main_menu_validator(selection="1") == 1
    assert main_menu_validator(selection=2) == 2
    assert main_menu_validator(selection="3") == 3
    assert main_menu_validator(selection="4") == 4
    assert main_menu_validator(selection="5") is False
    assert main_menu_validator(10) is False
    assert main_menu_validator("abc") is False
    assert main_menu_validator("") is False
    assert main_menu_validator("/") is False