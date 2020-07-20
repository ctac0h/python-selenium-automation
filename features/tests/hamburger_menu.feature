Feature: Hamburger menu


  Scenario: Verify Amazon Music sub menu has 6 items
    Given Open Amazon page
    When Open hamburger menu
    And Click on menu item with text Amazon Music
    Then Verify 6 items are present