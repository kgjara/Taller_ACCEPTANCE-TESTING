from behave import given, when, then
from todo_list import TodoManager, Task
from datetime import datetime, timedelta

@given('I have started the to-do list manager')
def step_impl(context):
    context.todo_manager = TodoManager(filename='test_tasks.json')

@when('I add a new task with title "{title}", description "{description}", due date "{due_date}", priority "{priority}", and category "{category}"')
def step_impl(context, title, description, due_date, priority, category):
    task = Task(title, description, due_date, priority, category)
    context.todo_manager.tasks.append(task)
    context.todo_manager.save_tasks()

@then('the task should be added successfully')
def step_impl(context):
    assert len(context.todo_manager.tasks) > 0

@when('I list all tasks')
def step_impl(context):
    context.tasks_list = context.todo_manager.tasks

@then('I should see the task "{title}" in the list')
def step_impl(context, title):
    titles = [task.title for task in context.tasks_list]
    assert title in titles

@when('I mark the task "{title}" as completed')
def step_impl(context, title):
    for task in context.todo_manager.tasks:
        if task.title == title:
            task.completed = True
            task.completed_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            context.todo_manager.save_tasks()
            break

@then('the task should be marked as completed')
def step_impl(context):
    for task in context.todo_manager.tasks:
        if task.completed:
            assert task.completed_at is not None

@when('I delete all tasks')
def step_impl(context):
    context.todo_manager.tasks = []
    context.todo_manager.save_tasks()

@then('there should be no tasks in the list')
def step_impl(context):
    assert len(context.todo_manager.tasks) == 0

@when('I filter tasks by category "{category}"')
def step_impl(context, category):
    context.filtered_tasks = [task for task in context.todo_manager.tasks if task.category.lower() == category.lower()]

@then('I should see only tasks in the "{category}" category')
def step_impl(context, category):
    for task in context.filtered_tasks:
        assert task.category.lower() == category.lower()

@when('I show overdue tasks')
def step_impl(context):
    today = datetime.now().date()
    context.overdue_tasks = []
    for task in context.todo_manager.tasks:
        if not task.completed:
            due_date = datetime.strptime(task.due_date, "%Y-%m-%d").date()
            if due_date < today:
                context.overdue_tasks.append(task)

@then('I should see the list of overdue tasks')
def step_impl(context):
    assert len(context.overdue_tasks) > 0

# Implementing missing steps
@given('I have a task with title "{title}"')
def step_impl(context, title):
    task = Task(title, "Description", "2025-01-10", "High", "General")
    context.todo_manager.tasks.append(task)
    context.todo_manager.save_tasks()

@given('I have tasks in different categories')
def step_impl(context):
    task1 = Task("Task 1", "Description 1", "2025-01-10", "High", "Work")
    task2 = Task("Task 2", "Description 2", "2025-01-11", "Medium", "Shopping")
    context.todo_manager.tasks.extend([task1, task2])
    context.todo_manager.save_tasks()

@given('I have overdue tasks')
def step_impl(context):
    overdue_date = (datetime.now() - timedelta(days=1)).strftime("%Y-%m-%d")
    task = Task("Overdue Task", "Description", overdue_date, "High", "General")
    context.todo_manager.tasks.append(task)
    context.todo_manager.save_tasks()