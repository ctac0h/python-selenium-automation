Feature: Test scenarios for Cart feature

  Scenario: Verify Cart is empty
    Given Open Amazon page
    When Click on Cart icon
    Then Verify Amazon.com Shopping Cart page opened
    And Verify Cart is empty and Your Amazon Cart is empty displayed

  Scenario: Add product into the Cart
    Given Open Amazon page
    When Input Rainbow Dash into search field
    And Click on search icon
    And Click on first result
    And Click on Add to cart
    And Click on Cart icon
    Then Verify Amazon.com Shopping Cart page opened
    And Verify presence of Rainbow Dash in the cart


