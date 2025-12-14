Feature: Web calculator
  As a user
  I want to calculate results in the browser
  So that I can verify basic operations

  Scenario: Add two numbers
    Given numbers 2 and 3
    When I submit "add"
    Then the result should be "5.0"

  Scenario: Divide by zero shows an error
    Given numbers 1 and 0
    When I submit "divide"
    Then I should see an error message "Cannot divide by zero."
