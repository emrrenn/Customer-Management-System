import project
from mainPage import mainPage

def test_check_username_password():
    assert project.check_username_password("admin","1234") == False
    assert project.check_username_password("adminn","123") == False
    assert project.check_username_password("admin","12345") == True

