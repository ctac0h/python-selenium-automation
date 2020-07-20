# Created by Svetlana at 4/4/19
Feature: Test Scenarios for Amazon Search functionality

  Scenario: User can search for a product
    Given Open Amazon page
    When Search for Rainbow Dash
    Then Product results for "Rainbow Dash" are shown
    And Verify number of elements is equal to 60