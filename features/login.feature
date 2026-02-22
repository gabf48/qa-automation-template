Feature: Login demo
  Demonstrate UI and API login

  @smoke @ui
  Scenario: Login via UI with valid credentials
    Given I open the SauceDemo login page
    When I login with username "standard_user" and password "secret_sauce"
    Then I should see the products page

  @smoke @api
  Scenario: Login via API with valid credentials
    When I login via API with email "eve.holt@reqres.in" and password "cityslicka"
    Then the response status should be 200