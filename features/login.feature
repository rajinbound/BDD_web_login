Feature: User login

  Scenario: Successful Login with valid credentials
    Given The user is on login page of a website
    When User type the correct <Username> in the email field and <Password> in the password field
      | Username          | Password  |
      | test@qa-experience.com | Password1 |
    Then User press "Login" button
    Then User should see "Successfully logged in!" message


  Scenario: Successful Login with valid credentials
    Given User is on login page of a website
    When User type the incorrect <Username> in the email field and <Password> in the password field
      | Username          | Password  |
      | testqa-experience.com | Password1 |
    Then User pressed "Login" button
    Then User should see not see "Successfully logged in!" message