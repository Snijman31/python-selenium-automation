# Created by sarah-annnijman at 12/16/24
Feature:  Test cart icon


  Scenario:  user can click on cart icon
    Given Open target main page
    When Click Cart icon
    Then Verify Your Cart is empty message is shown
