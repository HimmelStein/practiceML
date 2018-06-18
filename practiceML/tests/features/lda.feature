
Feature: Latent Dirichlet Allocation

  Scenario: Retrieving content words
    Given the sentence "In einem Satz gibt es viele schöne Worte und einen schönen Punkt."
    When we extract the content words
    Then we get "Satz geben schöne Wort schön Punkt"
