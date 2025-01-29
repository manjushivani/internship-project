# Created by manju at 1/14/2025
Feature: Test web app pages
  #@smoke
  Scenario: User can open the Secondary deals page and go through the pagination
    Given Open the main page
    When  Enter email
    Then Enter password
    Then CLick continue button
    Then Click on Secondary option at the left side menu
    Then Verify the right page opens
    Then  Go to the final page using the pagination button
    Then Go back to the first page using the pagination button

