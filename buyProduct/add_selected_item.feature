Feature: Shopping cart

  Scenario: Verify the user is able to select and add product to the cart
    Given I add four different products to my wish list
    When I view my wishlist table
    Then I find total four selected items in my wish list
    When I search for the lowest price item to my cart
    Then I am able to verify the item in the cart
