Feature: CSV reverse sorting
  The application process input CSV files into an output file with each line sorted in reverse order and an output file with all lines combined and sorted in reverse order.

  Scenario: General Case: The application should process an input <filename><.ext optional> into <filename>_sorted_lines.csv and <filename>_sorted_flat.csv reverse-sorted output files
    Given I have a terminal session open in the project's root directory
    And there exist CSV files in the input directory
    When I run `./execute.sh` in my terminal
    Then I should see each CSV file's reverse-sorted output files (by-line and flattened) represented in `data/outputs`

  Scenario: Special Case: The application should process an input called input<.ext optional> into output_lines.csv and output_flat.csv reverse-sorted output files
    Given I have a terminal session open in the project's root directory
    And there exists a CSV file called "input" with any or no extension in the input directory
    When I run `./execute.sh` in my terminal
    Then I should see the CSV file `input`<.ext optional>'s reverse-sorted output files (by-line and flattened) represented in `data/outputs` as `output_flat.csv` and `output_lines.csv`.

  Scenario: General Case: The application should skip an input starting with `.git`
    Given I have a terminal session open in the project's root directory
    And there exist files starting with `.git` in the input directory
    When I run `./execute.sh` in my terminal
    Then I should not see any output CSV files for inputs starting with `.git`.

  Scenario: General Case: The application should result in only `.git`-prefix files and output CSV files in the output directory
    Given I have a terminal session open in the project's root directory
    When I run `./execute.sh` in my terminal
    Then I should only see unprocessed `.git`-prefixed files and processed CSV outputs for any input files present at execution time