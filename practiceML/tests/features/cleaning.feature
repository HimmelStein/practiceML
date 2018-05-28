Feature: Textfile cleaning
  In order to  have a well prepared basis for further analysis
         As a  text analyst
       I want  to be able to remove hyphenization from the text files. 

  
  Scenario: Text containes no hyphenated words
    Given the following lines of text 
      """
      § 959 Aufgabe des Eigentums
      Eine bewegliche Sache wird herrenlos, 
      wenn der Eigentümer in der Absicht, 
      auf das Eigentum zu verzichten, 
      den Besitz der Sache aufgibt.
      """
    When the system cleans this text
    Then the lines stay unchanged


  Scenario: Text contains one hyphenated word 
    Given the following lines of text 
      """
      § 959 Aufgabe des Eigentums
      Eine bewegliche Sache wird herrenlos, wenn der Eigen-
      tümer in der Absicht, auf das Eigentum zu verzichten, 
      den Besitz der Sache aufgibt.
      """
    When the system cleans this text
    Then the text consists of the following lines
      """
      § 959 Aufgabe des Eigentums
      Eine bewegliche Sache wird herrenlos, wenn der Eigentümer in der Absicht, auf das Eigentum zu verzichten, 
      den Besitz der Sache aufgibt.
      """

    Scenario: Text ist just one hyphenated long word
    Given the following lines of text
      """
      Run-
      time-
      test
      """
    When the system cleans this text
    Then the text consists of the following lines
      """
      Runtim
      etest
      """


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