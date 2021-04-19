Feature: Search stuff on the main page of Amazon

  Background: go to main page of Amazon
    Given I open the main page

  @search @smoke
  Scenario: Searching on the main page
    When I search for "test automation"
    Then I should see "test automation" in search result