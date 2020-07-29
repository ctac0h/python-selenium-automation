Feature: Tests for product page

  Scenario: Size tooltip is shown upon hovering over Add To Cart button
    Given Open Amazon Product B074TBCSC8 page
    When Hover over Add To Cart button
    Then Verify size selection tooltip is shown


  Scenario: New Arrivals tooltip is shown upon hovering over New Arrivals
    Given Open Amazon Product B074TBCSC8 page
    When Hover over 7 product top menu item
    Then Product top menu tooltip is shown
