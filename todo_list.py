# Creating an empty list to store tasks added by a user.
tasks = []

def main():
    """Initializing the main function to handle user inputs and other function
        operations. """
    while True:
        print("1. Add | 2. View | 3. Remove | 4. Exit |")
        option = input("Enter choice: ")

        # Evaluating user options
        if option == "1":
            task = input("Enter task: ").strip() # making sure any white spaces is removed
            add_task(task)
        elif option == "2":
            view_task(task)
        elif option == "3":
            remove_task(task)
        else:
            return "Invalid Input."
        
        choice = input("Do you want to continue? (y/n): ").lower() # evaluating user input in lower case
        if choice != "y" and "yes":
            print("\nMy Final To-do List.")
            for index, task in enumerate(tasks, start=1):
                print(f"{index}. {task}")
            print("\nGoodbye")
            break


def add_task(task):
    """Initializing a function to handle adding tasks."""
    if task:
        tasks.append(task) # Adding each task to the list.
        print("Task added successfully.")
    else:
        return "Please enter task"


def view_task(task):
    """Initializing a function to handle viewing tasks."""
    if tasks:
        print("To-do List.")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}") # printing each task and its index.
    else:
        return "No task added."
    

def remove_task(task):
    """Initializing a function that handles task removal or deletion."""

    # displaying tasks and their index.
    view_task(task)

    # Prompting the user for the task index
    index = int(input("Enter task number to be removed: ")) 

    # Evaluating the user index choice.
    if 0 <= index < len(tasks):
        tasks.pop(index) # Removes a task from the list
        print("Task Removed!")
    else:
        print("Enter a valid task number.")
    

if __name__ == "__main__":
    main()