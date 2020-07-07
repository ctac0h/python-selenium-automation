Feature: Tests for Help search functionality


  Scenario: Verify search for Cancel Order
    Given Open Amazon help page
    When Input cancel order to help search
    And Click help search button
    Then Help search results for Cancel Items or Orders shown