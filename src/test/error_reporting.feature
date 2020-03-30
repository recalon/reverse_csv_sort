Feature: Error reporting
  The application should give informative errors when an exception occurs or usage directions are not followed.

  Scenario: The input directory is empty
    Given I have a terminal session open to the project's root directory
    And the only files in the `data/inputs` directory are hidden files
    When I run `./execute.sh` in my terminal
    Then I should not find output files in `data/inputs`
    And I should see a message printed to the console informing me the application requires input CSV files.

  Scenario: An input file gets deleted before processing
    Given I have a terminal session open to the project's root directory
    And I have placed input files into the input directory
    When I run `./execute.sh` in my terminal
    And I delete an input file before the application can process it
    Then I should not find output files for the deleted input in `data/outputs`
    And I should see a message printed to the console informing me that the file could not be found and was skipped.