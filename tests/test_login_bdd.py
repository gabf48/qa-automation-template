# tests/test_login_bdd.py
from pytest_bdd import scenario

@scenario('../features/login.feature', 'Login via UI with valid credentials')
def test_login_ui():
    pass

@scenario('../features/login.feature', 'Login via API with valid credentials')
def test_login_api():
    pass