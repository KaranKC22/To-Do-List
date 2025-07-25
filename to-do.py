def main():
    tasks = []

    while True:
        print("\n==== To-Do List ====")
        print("1. Add task")
        print("2. Show Tasks")
        print("3. Mark Task as Done")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            print()
            n_tasks = int(input("How many tasks do you want to add: "))

            for i in range(n_tasks):
                task = input("Enter the task: ")
                tasks.append({"task": task, "done": False})
                print("Task added!")

        elif choice == '2':
            if not tasks:
                print("\nNo tasks to show.")
            else:
                print("\nTasks:")
                for index, task in enumerate(tasks):
                    status = "Done" if task["done"] else "Not Done"
                    print(f"{index + 1}. {task['task']} - {status}")

        elif choice == '3':
            if not tasks:
                print("No tasks available to mark as done.")
            else:
                try:
                    task_index = int(input("Enter the task number to mark as done: ")) - 1
                    if 0 <= task_index < len(tasks):
                        tasks[task_index]["done"] = True
                        print("Task marked as done!")
                    else:
                        print("Invalid task number.")
                except ValueError:
                    print("Please enter a valid number.")

        elif choice == '4':
            print("Exiting the To-Do List.")
            break

        else:
            print("Invalid choice. Please try again.")

# This should be at the **bottom level**, not indented inside main()
if __name__ == "__main__":
    main()
