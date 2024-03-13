class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({"task": task, "completed": False})

    def complete_task(self, task_name):
        for task in self.tasks:
            if task["task"] == task_name:
                task["completed"] = True

    def remove_task(self, task_name):
        self.tasks = [task for task in self.tasks if task["task"] != task_name]

    def show_tasks(self):
        if not self.tasks:
            print("No tasks.")
        else:
            for idx, task in enumerate(self.tasks, start=1):
                status = "Completed" if task["completed"] else "Incomplete"
                print(f"{idx}. {task['task']} - {status}")


def main():
    task_manager = TaskManager()

    while True:
        print("\nTask Manager")
        print("1. Add Task")
        print("2. Complete Task")
        print("3. Remove Task")
        print("4. Show Tasks")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("Enter task name: ")
            task_manager.add_task(task)
            print("Task added.")

        elif choice == "2":
            task = input("Enter task name to mark as completed: ")
            task_manager.complete_task(task)
            print("Task marked as completed.")

        elif choice == "3":
            task = input("Enter task name to remove: ")
            task_manager.remove_task(task)
            print("Task removed.")

        elif choice == "4":
            task_manager.show_tasks()

        elif choice == "5":
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
