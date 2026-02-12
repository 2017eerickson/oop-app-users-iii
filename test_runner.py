from runner import user_menu

def test_user_menu():
    assert isinstance(user_menu(), dict)