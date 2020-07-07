Feature: Test Scenarios for Sign In functionality

  Scenario: Logged out user sees Sign in page when clicking Orders
    Given Open Amazon Page
    When Click on "Orders" button
    Then Verify Amazon Sign-In page opened