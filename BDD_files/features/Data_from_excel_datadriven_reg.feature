Feature: Register Functionality data driven

  Scenario Outline: User Register functionality datadriven
    Given open the browser navigate to  url for datadriven
    And Click on reg link for datadriven
    And collection_data_from_excel "<location>" and "<sheet_name>"
    Then verify register results for data driven

    Examples:
      |location| sheet_name|
      | C:/Users/hp/PycharmProjects/nop_comm_project/TestData/TestData1.xlsx     |  reg           |