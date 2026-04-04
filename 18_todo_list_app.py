# Todo List App
# This is a simple todo list app that allows users to add tasks and view their tasks. The tasks are stored in a text file called "tasks.txt".
# Author : Asad Sajjad


# Main menu
while True:
    print("\nTodo List App")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Delete a task")
    print("4. Exit")

# Get user input
    choice = int(input("\nEnter your choice: "))

# Add a task
    if choice == 1 :
        task = input("Enter a task: ").lower()
        with open("tasks.txt", "a") as f:
            f.write(task + "\n")

# View tasks
    elif choice == 2 :
        with open("tasks.txt") as f :
            tasks = f.readlines()
            if not tasks :
                print("No tasks found.")
            else :
                for i, task in enumerate(tasks, start=1): # Print each task with its number
                    print(f"{i}. {task.strip()}") # Strip the newline character from the end of each task


# Delete a task
    elif choice == 3 :
        with open("tasks.txt") as f :
            tasks = f.readlines()
            for i, task in enumerate(tasks, start=1) :
                print(f"{i}. {task.strip()}")
        task_number = int(input("Enter the task number to delete: "))
        if task_number > 0 and task_number <= len(tasks) : # Check if the task number is valid
            del tasks[task_number - 1] # Delete the task from the list
            with open("tasks.txt", "w") as f :
                f.writelines(tasks)
        else :
            print("Invalid task number.")

# Exit
    elif choice == 4 :
        print("Goodbye!")
        break
# Invalid choice
    else :
        print("Invalid choice. Please enter a number between 1 and 4.")
        
