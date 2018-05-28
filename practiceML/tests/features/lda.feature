# Created by dongt at 28.05.18
Feature: Latent Dirichlet Allocation

  Scenario: Retrieving content words
    Given the sentence "In einem Satz sind viele schöne Worte."
    When we extract the content words
    Then we get "Satz sind viele schöne Worte"
