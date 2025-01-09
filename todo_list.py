class Task:
    def __init__(self, name, description, due_date, priority):
        self.name = name
        self.description = description
        self.due_date = due_date
        self.priority = priority
        self.completed = False
    
    def mark_completed(self):
        self.completed = True
        
    def __str__(self):
        status = "Completed" if self.completed else "Pending"
        return f"Task: {self.name}\nDescription: {self.description}\nDue Date: {self.due_date}\nPriority: {self.priority}\nStatus: {status}\n"


class TodoListManager:
    def __init__(self):
        self.tasks = []
    
    def add_task(self, name, description, due_date, priority):
        new_task = Task(name, description, due_date, priority)
        self.tasks.append(new_task)
    
    def list_tasks(self):
        if not self.tasks:
            print("No tasks in the list.")
        else:
            for task in self.tasks:
                print(task)
    
    def mark_task_completed(self, task_name):
        for task in self.tasks:
            if task.name.lower() == task_name.lower():
                task.mark_completed()
                print(f"Task '{task_name}' marked as completed.")
                return
        print(f"Task '{task_name}' not found.")
    
    def clear_tasks(self):
        self.tasks.clear()
        print("All tasks have been cleared.")
        

def main():
    manager = TodoListManager()
    
    while True:
        print("\nTo-Do List Manager")
        print("1. Add a new task")
        print("2. List all tasks")
        print("3. Mark task as completed")
        print("4. Clear all tasks")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            name = input("Enter task name: ")
            description = input("Enter task description: ")
            due_date = input("Enter task due date (YYYY-MM-DD): ")
            priority = input("Enter task priority (Low, Medium, High): ")
            manager.add_task(name, description, due_date, priority)
            print("Task added successfully.")
        
        elif choice == '2':
            manager.list_tasks()
        
        elif choice == '3':
            task_name = input("Enter task name to mark as completed: ")
            manager.mark_task_completed(task_name)
        
        elif choice == '4':
            manager.clear_tasks()
        
        elif choice == '5':
            print("Exiting the To-Do List Manager. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
