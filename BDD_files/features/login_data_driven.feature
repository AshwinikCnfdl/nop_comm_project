Feature: Login Functionality with csv file data

  Scenario Outline: User login functionality with datadriven
    Given open the Chrome browser with url
    When the user navigates to the login_page
    When the user enters email "<email>" and password "<password>" and clicks on login
    Then verify login with set of data results

    Examples:
      | email              | password  |
      | test1@example.com  | pass123   |
      | test2@example.com  | pass456   |