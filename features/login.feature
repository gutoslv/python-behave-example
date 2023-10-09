Feature: Login page

  Background: I am a user
    Given I am on the login page

  Scenario: Login with valid credentials
    When I enter valid credentials
    Then I should be logged in to the inventory page
    And I should see the inventory products in the page

  Scenario: Login with invalid credentials
    When I enter invalid credentials
    Then I should see the invalid credentials error message

  Scenario: Login with locked user
    When I enter locked out user credentials
    Then I should see the locked out user error message

  Scenario: Login with problem user
    When I enter problem user credentials
    Then I should be logged in to the inventory page
    And I should see the inventory page with all the item images loaded with the same image

  Scenario: Login with existing user and wrong password
    When I enter existing user and wrong password
    Then I should see the invalid credentials error message

  Scenario: Login with existing user and empty password
    When I enter existing user and empty password
    Then I should see the empty password error message

  Scenario: Login with empty user and existing password
    When I enter empty user and existing password
    Then I should see the empty user error message

  Scenario: Login with empty user and empty password
    When I enter empty user and empty password
    Then I should see the empty user error message only

  Scenario: Can't access inventory page without login
    When I try to access the inventory page without logging in
    Then I should see the login page
    And I should see the required login error message