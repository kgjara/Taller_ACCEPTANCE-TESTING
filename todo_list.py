from datetime import datetime, timedelta
import json
import os

class Task:
    def __init__(self, title, description, due_date, priority, category):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.priority = priority
        self.category = category
        self.completed = False
        self.created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.completed_at = None

    def to_dict(self):
        return {
            'title': self.title,
            'description': self.description,
            'due_date': self.due_date,
            'priority': self.priority,
            'category': self.category,
            'completed': self.completed,
            'created_at': self.created_at,
            'completed_at': self.completed_at
        }

    @classmethod
    def from_dict(cls, data):
        task = cls(
            data['title'],
            data['description'],
            data['due_date'],
            data['priority'],
            data['category']
        )
        task.completed = data['completed']
        task.created_at = data['created_at']
        task.completed_at = data['completed_at']
        return task

class TodoManager:
    def __init__(self, filename='tasks.json'):
        self.filename = filename
        self.tasks = []
        self.load_tasks()

    def add_task(self):
        print("\n=== Add New Task ===")
        title = input("Enter task title: ")
        description = input("Enter task description: ")
        due_date = input("Enter due date (YYYY-MM-DD): ")
        priority = input("Enter priority (High/Medium/Low): ").capitalize()
        category = input("Enter category: ")

        task = Task(title, description, due_date, priority, category)
        self.tasks.append(task)
        self.save_tasks()
        print("Task added successfully!")

    def list_tasks(self):
        if not self.tasks:
            print("\nNo tasks found!")
            return

        print("\n=== Task List ===")
        for i, task in enumerate(self.tasks, 1):
            status = "✓" if task.completed else " "
            print(f"\n{i}. [{status}] {task.title}")
            print(f"   Description: {task.description}")
            print(f"   Due Date: {task.due_date}")
            print(f"   Priority: {task.priority}")
            print(f"   Category: {task.category}")
            print(f"   Created: {task.created_at}")
            if task.completed:
                print(f"   Completed: {task.completed_at}")

    def mark_completed(self):
        self.list_tasks()
        if not self.tasks:
            return

        try:
            task_num = int(input("\nEnter task number to mark as completed: ")) - 1
            if 0 <= task_num < len(self.tasks):
                task = self.tasks[task_num]
                task.completed = True
                task.completed_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                self.save_tasks()
                print("Task marked as completed!")
            else:
                print("Invalid task number!")
        except ValueError:
            print("Please enter a valid number!")

    def delete_all_tasks(self):
        confirm = input("\nAre you sure you want to delete all tasks? (yes/no): ")
        if confirm.lower() == 'yes':
            self.tasks = []
            self.save_tasks()
            print("All tasks deleted!")
        else:
            print("Operation cancelled!")

    # Additional Feature 1: Filter tasks by category
    def filter_by_category(self):
        if not self.tasks:
            print("\nNo tasks found!")
            return

        categories = set(task.category for task in self.tasks)
        print("\nAvailable categories:", ", ".join(categories))
        category = input("Enter category to filter by: ")
        
        filtered_tasks = [task for task in self.tasks if task.category.lower() == category.lower()]
        if not filtered_tasks:
            print(f"No tasks found in category '{category}'")
            return

        print(f"\n=== Tasks in category '{category}' ===")
        for i, task in enumerate(filtered_tasks, 1):
            status = "✓" if task.completed else " "
            print(f"\n{i}. [{status}] {task.title}")
            print(f"   Due Date: {task.due_date}")
            print(f"   Priority: {task.priority}")

    # Additional Feature 2: Show overdue tasks
    def show_overdue_tasks(self):
        today = datetime.now().date()
        overdue_tasks = []
        
        for task in self.tasks:
            if not task.completed:
                try:
                    due_date = datetime.strptime(task.due_date, "%Y-%m-%d").date()
                    if due_date < today:
                        overdue_tasks.append(task)
                except ValueError:
                    continue

        if not overdue_tasks:
            print("\nNo overdue tasks!")
            return

        print("\n=== Overdue Tasks ===")
        for i, task in enumerate(overdue_tasks, 1):
            print(f"\n{i}. {task.title}")
            print(f"   Due Date: {task.due_date}")
            print(f"   Priority: {task.priority}")
            print(f"   Days Overdue: {(today - datetime.strptime(task.due_date, '%Y-%m-%d').date()).days}")

    def save_tasks(self):
        with open(self.filename, 'w') as f:
            tasks_data = [task.to_dict() for task in self.tasks]
            json.dump(tasks_data, f, indent=2)

    def load_tasks(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as f:
                tasks_data = json.load(f)
                self.tasks = [Task.from_dict(task_data) for task_data in tasks_data]

def main():
    todo_manager = TodoManager()
    
    while True:
        print("\n=== To-Do List Manager ===")
        print("1. Add Task")
        print("2. List Tasks")
        print("3. Mark Task as Completed")
        print("4. Delete All Tasks")
        print("5. Filter Tasks by Category")
        print("6. Show Overdue Tasks")
        print("7. Exit")

        choice = input("\nEnter your choice (1-7): ")

        if choice == '1':
            todo_manager.add_task()
        elif choice == '2':
            todo_manager.list_tasks()
        elif choice == '3':
            todo_manager.mark_completed()
        elif choice == '4':
            todo_manager.delete_all_tasks()
        elif choice == '5':
            todo_manager.filter_by_category()
        elif choice == '6':
            todo_manager.show_overdue_tasks()
        elif choice == '7':
            print("\nGoodbye!")
            break
        else:
            print("\nInvalid choice! Please try again.")

if __name__ == "__main__":
    main()