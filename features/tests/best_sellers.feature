Feature: Tests scenarios for Amazon Best Sellers page


  Scenario: Check Best Sellers menu
    Given Open Amazon Best Sellers page with https://www.amazon.com/gp/bestsellers/?ref_=nav_cs_bestsellers
    Then Verify Best Sellers menu has 5 links