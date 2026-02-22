# features/steps/login_steps.py
from pytest_bdd import given, when, then
from pages.login_page import LoginPage

@given('I open the SauceDemo login page')
def open_login_page(page):
    login_page = LoginPage(page)
    login_page.navigate("https://www.saucedemo.com")  # sau din .env

@when('I login with username "standard_user" and password "secret_sauce"')
def login_ui(page):
    login_page = LoginPage(page)
    login_page.login("standard_user", "secret_sauce")

@then('I should see the products page')
def products_page_visible(page):
    assert page.url.endswith("inventory.html")


# features/steps/login_steps.py (continuare)
import pytest
import requests

@when('I login via API with email "eve.holt@reqres.in" and password "cityslicka"')
def login_api():
    response = requests.post(
        "https://reqres.in/api/login",
        json={"email": "eve.holt@reqres.in", "password": "cityslicka"}
    )
    pytest.response = response

@then('the response status should be 200')
def response_ok():
    assert pytest.response.status_code == 200