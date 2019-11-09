@example

Feature: A simple example for BDD using pytest

  Scenario: Simple Hello World
  Given example-cli is started
  When  The parameter --greet is passed
  Then  "Hello, world" is displayed
