# Created by sarah-annnijman at 12/25/24
Feature: Test Cart
  # Enter feature description here

  Scenario: User can add to cart
    Given Open target main page
     When Search for candy
    And Click on Add to Cart Button
    And Confirm Add to Cart from side Navigation
    Then Verify Cart has 1 item
   # Then Verify candy is added to cart

