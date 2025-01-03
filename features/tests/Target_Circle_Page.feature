# Created by sarah-annnijman at 12/25/24
Feature:  Target Circle page
  # Enter feature description here

  Scenario: User can open Target Circle page
    Given Open target circle page
    When Locate benefit cells
    Then Verify benefit cells are displayed
    