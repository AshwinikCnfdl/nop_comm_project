Feature: Register Functionality

  Scenario Outline: User Register functionality
    Given open the browser navigate to  url
    And Click on reg link
    And enter the "<fn>","<ln>","<email>","<pwd>",cpwd and click on the register
    Then verify register results

    Examples:
      |fn   |ln | email              | password  |
      | abc |k  | test1@example.com  | pass123   |
      |xyz  |m  |test2@example.com   | pass456   |
      |hyz  |h  | test3@example.com  | pass789   |
    # next file location