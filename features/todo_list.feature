Feature: To-Do List Management
  As a user
  I want to manage my to-do list
  So that I can keep track of my tasks

  Scenario: Add a new task
    Given I have started the to-do list manager
    When I add a new task with title "Buy groceries", description "Buy milk and eggs", due date "2025-01-10", priority "High", and category "Shopping"
    Then the task should be added successfully

  Scenario: List all tasks
    Given I have started the to-do list manager
    When I list all tasks
    Then I should see the task "Buy groceries" in the list

  Scenario: Mark a task as completed
    Given I have started the to-do list manager
    And I have a task with title "Buy groceries"
    When I mark the task "Buy groceries" as completed
    Then the task should be marked as completed

  Scenario: Delete all tasks
    Given I have started the to-do list manager
    When I delete all tasks
    Then there should be no tasks in the list

  Scenario: Filter tasks by category
    Given I have started the to-do list manager
    And I have tasks in different categories
    When I filter tasks by category "Shopping"
    Then I should see only tasks in the "Shopping" category

  Scenario: Show overdue tasks
    Given I have started the to-do list manager
    And I have overdue tasks
    When I show overdue tasks
    Then I should see the list of overdue tasks