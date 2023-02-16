import main

def test_check_username_password():
    assert main.check_username_password("admin","1234") == False
    assert main.check_username_password("adminn","123") == False
    assert main.check_username_password("admin","12345") == True

def test_check_database():
    assert main.check_database("customers.db") == True
    assert main.check_database("customer.db") == False

def test_check_database_elements():
    assert main.check_database_elements() == main.total