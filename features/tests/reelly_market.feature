Feature: Test web app pages
  #@smoke
  Scenario: User can click market, add company and verify publish my company
    Given Open the main page
    When  Enter email
    Then Enter password
    Then CLick continue button
    Then Click on “Market” at the left side menu.
    #Then Verify the right page opens for market.
    Then Click on “Add Company” button.
    #Then Verify the right page opens.
    #Then Verify the button “Publish my company” is available.