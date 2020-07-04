Feature: Test Scenarios for Orders functionality

  Scenario: Logged out user sees Sign in page when clicking Orders
    Given Open Amazon Page
    When Click on "Orders" button
    Then "Sign in" page opened