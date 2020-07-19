Feature: Window handling


  Scenario: Company's website is open in a new tab
    Given Open Yelp page
    Then Save current window handles
    When Click on a website link
    Then Switch to a new window
    Then The company's website is open
    And Close new window and switch back to original