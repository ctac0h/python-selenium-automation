# Created by Svetlana at 4/4/19
Feature: Test Scenarios for Amazon Search functionality

  Scenario: User can search for a product
    Given Open Amazon page
    When Search for Rainbow Dash
    Then Product results for "Rainbow Dash" are shown
    And Verify number of elements is equal to 60



  Scenario: User can select Books department
    Given Open Amazon page
    When Select stripbooks department
    And Search for Faust
    Then Books department is selected



  Scenario: User can select Baby department
    Given Open Amazon page
    When  Select baby-products department
    And Search for pacifier
    Then Baby department is selected
