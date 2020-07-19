Feature: Amazon bestsellers menu


  Scenario: Verify user can click each item in the menu and correct page is opened
    Given Open Amazon Best Sellers page with https://www.amazon.com/gp/bestsellers/?ref_=nav_cs_bestsellers
    Then Verify Best Sellers menu has 5 links
    And Click on each menu item and verify correct page is opened