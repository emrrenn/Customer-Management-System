import project

def test_check_username_password():
    assert project.check_username_password("admin","1234") == False
    assert project.check_username_password("adminn","123") == False
    assert project.check_username_password("admin","12345") == True

def test_check_database():
    assert project.check_database("customers.db") == True
    assert project.check_database("customer.db") == False

def test_check_database_elements():
    assert project.check_database_elements() == project.total