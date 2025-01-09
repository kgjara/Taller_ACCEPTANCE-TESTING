from behave import given, when, then
from datetime import date

# Clase para simular el gestor de la lista de tareas
class TodoListManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task_name):
        self.tasks.append({"task": task_name, "status": "Pending"})

    def list_tasks(self):
        return [task["task"] for task in self.tasks]

    def mark_completed(self, task_name):
        for task in self.tasks:
            if task["task"] == task_name:
                task["status"] = "Completed"

    def clear_all_tasks(self):
        self.tasks.clear()

# Crear una instancia del gestor de tareas
todo_list_manager = TodoListManager()

# Paso 1: Cuando la lista de tareas está vacía
@given('the to-do list is empty')
def step_impl_given_empty_list(context):
    todo_list_manager.clear_all_tasks()  # Asegurarse de que la lista esté vacía

# Paso 2: Cuando el usuario agrega una tarea
@when('the user adds a task "{task_name}"')
def step_impl_add_task(context, task_name):
    todo_list_manager.add_task(task_name)

# Paso 3: Verificar que la tarea se haya agregado a la lista
@then('the to-do list should contain "{task_name}"')
def step_impl_check_task_in_list(context, task_name):
    tasks = todo_list_manager.list_tasks()
    assert task_name in tasks, f"Task '{task_name}' not found in the list"

# Paso 4: Configuración de tareas en la lista (para listado de tareas)
@given('the to-do list contains tasks:')
def step_impl_given_list_of_tasks(context):
    todo_list_manager.clear_all_tasks()  # Asegurarse de que la lista esté vacía
    for row in context.table:
        task_name = row["Task"]
        todo_list_manager.add_task(task_name)

# Paso 5: Listar todas las tareas
@when('the user lists all tasks')
def step_impl_list_all_tasks(context):
    context.task_list = todo_list_manager.list_tasks()  # Guardar las tareas listadas

# Paso 6: Verificar la lista de tareas
@then('the output should contain:')
def step_impl_check_list_output(context):
    output = context.task_list
    expected_tasks = [row["Task"] for row in context.table]
    assert sorted(output) == sorted(expected_tasks), f"Expected tasks {expected_tasks}, but got {output}"

# Paso 7: Configuración de tareas con estado "Pending" o "Completed"
@given('the to-do list contains completed tasks:')
def step_impl_given_list_of_tasks_for_completed(context):
    todo_list_manager.clear_all_tasks()  # Limpiar la lista antes de agregar tareas
    for row in context.table:
        task_name = row["Task"]
        status = row["Status"]
        todo_list_manager.add_task(task_name)
        if status == "Completed":
            todo_list_manager.mark_completed(task_name)

# Paso 8: Marcar una tarea como completada
@when('the user marks task "{task_name}" as completed')
def step_impl_mark_task_completed(context, task_name):
    todo_list_manager.mark_completed(task_name)

# Paso 9: Verificar que la tarea esté marcada como completada
@then('the to-do list should show task "{task_name}" as completed')
def step_impl_check_task_completed(context, task_name):
    task_status = next((task for task in todo_list_manager.tasks if task["task"] == task_name), None)
    assert task_status is not None and task_status["status"] == "Completed", f"Task '{task_name}' was not marked as completed"

# Paso 10: Limpiar toda la lista de tareas
@when('the user clears the to-do list')
def step_impl_clear_all_tasks(context):
    todo_list_manager.clear_all_tasks()

# Paso 11: Verificar que la lista de tareas esté vacía
@then('the to-do list should be empty')
def step_impl_check_empty_list(context):
    tasks = todo_list_manager.list_tasks()
    assert len(tasks) == 0, f"The to-do list is not empty, it contains {tasks}"
