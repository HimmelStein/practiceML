Feature: Text cleaning
  In order to  have a well prepared basis for further analysis
         As a  text analyst
       I want  to be able to remove hyphenization from the text files. 

  
  Scenario: Text contains no hyphenated words
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
    Then the text contains "Eigentümer"
     But the text does not contain "Eigen-"


    Scenario: Text ist just one hyphenated long word
    Given the following lines of text
      """
      Bundes-
      aus-
      bil-
      dungs-
      förde-
      rungs-
      gesetz
      """
    When the system cleans this text
    Then the text consists of the following lines
      """
      Bundesausbildungsförderungsgesetz
      """