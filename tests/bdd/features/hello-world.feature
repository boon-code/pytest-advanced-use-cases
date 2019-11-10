@bdd_example

Feature: A simple example for BDD using pytest

  Scenario: Simple Hello World
  Given hello is started
  When  The parameter "--greet" is passed
  Then  "Hello, world!" is displayed

  Scenario: Unfriendly use-case
  Given hello is started
  When  No parameter is passed
  Then  "Okay" is displayed

  Scenario: Dummy text from resource
  Given dummy-text is started
  When No parameter is passed
  Then "This is a dummy file, with dummy content" is displayed
