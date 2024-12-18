# Created by sarah-annnijman at 12/16/24
Feature: # Test Sign in
  # Enter feature description here

  Scenario: User can click sign in
    Given Open target main page
    When Click Sign in
    Then Verify Sign In form opened
