Feature: Window handling


  Scenario: Company's website is open in a new tab
    Given Open Yelp page
    When Click on a website link
    And Switch to a new window
    Then The company's website is open
    And a user can close the new window and go to the original