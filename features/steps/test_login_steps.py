from pytest_bdd import given, when, then
from pages.sauce_login_page import SauceLoginPage
import pytest
import requests

# UI Steps
@given("I open the SauceDemo login page")
def open_login_page(page):
    page.goto("https://www.saucedemo.com/")
    return page

@when('I login with username "standard_user" and password "secret_sauce"')
def ui_login(page):
    login_page = SauceLoginPage(page)
    login_page.login("standard_user", "secret_sauce")

@then("I should see the products page")
def verify_products(page):
    assert "inventory.html" in page.url

# API Steps
@when('I login via API with email "eve.holt@reqres.in" and password "cityslicka"')
def api_login_step():
    response = requests.post("https://reqres.in/api/login",
                             json={"email": "eve.holt@reqres.in", "password": "cityslicka"})
    pytest.api_response = response

@then("the response status should be 200")
def api_status_check():
    assert pytest.api_response.status_code == 200