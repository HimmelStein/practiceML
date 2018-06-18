
Feature: Text file cleaning
    In order to  have a well prepared basis for further analysis
           As a  text analyst
         I want  to be able to remove hyphenization from the text files.


Background: Tests work on BGB texts
    Given we are working on samples in the folder "bgb"



Scenario Outline: Text cleaning in files
    Given a text file named "<filename>"
      And a corresponding oracle file
     When we create a cleaned file
     Then the cleaned file exists
      And contains the same as the oracle file

Examples: BGB zu Bienen
    | filename                |
    | BGB_§691_zweizeilig.txt |
    | BGB_§691_mehrzeilig.txt |