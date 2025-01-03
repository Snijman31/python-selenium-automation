# Created by sarah-annnijman at 12/21/24
Feature: Test For Search
  # Enter feature description here

  Scenario: User can search for juice
    Given Open target main page
    When Search for juice
   Then Verify search results shown juice
