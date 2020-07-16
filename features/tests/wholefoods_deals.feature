Feature: Whole foods deals


  Scenario: Products on Wholefoods deals page should have Regular price and Product name
    Given Open Amazon Wholefoods deals page https://www.amazon.com/wholefoodsdeals
    Then Verify all products have name and regular price