# Creating an empty list to store tasks added by a user.
tasks = []

def main():
    """Initializing the main function to handle user inputs and other function
        operations. """
    while True:
        print("| 1. Add | 2. View | 3. Remove | 4. Completed | 5. Save |")
        option = input("Enter choice: ")

        # Evaluating user options
        if option == "1":
            task = input("Enter task: ").strip() # making sure any white spaces is removed
            add_task(task)
        elif option == "2":
            view_task()
        elif option == "3":
            remove_task()
        elif option == "4":
            completed_task()
        elif option == '5':
            save_task()
        else:
            return "Invalid Input."
        
        choice = input("\nDo you want to continue? (y/n): ").lower() # evaluating user input in lower case
        if choice != "y" and "yes":
            print("\nMy Final To-do List.")
            for index, task in enumerate(tasks, start=1):
                mark = '✔' if task['completed'] else ''
                print(f"{index}. {task['task']}{mark}")
            print("\nGoodbye")
            break


def add_task(task):
    """Initializing a function to handle adding tasks."""
    if task:
        tasks.append({'task':task, 'completed':False}) # Adding each task to the list.
        print("Task added successfully.")
    else:
        return "Please enter task"


def view_task():
    """Initializing a function to handle viewing tasks."""
    if tasks:
        print("\nTo-do List.")
        for index, task in enumerate(tasks, start=1):
            mark = '✔' if task['completed'] else ''
            print(f"{index}. {task['task']}{mark}") # printing each task and its index.
    else:
        return "No task added."
    

def remove_task():
    """Initializing a function that handles task removal or deletion."""

    # displaying tasks and their index.
    view_task()

    if not tasks:
        return

    try:
        # Prompting the user for the task index
        index = int(input("Enter task number to be removed: ")) 

        # Evaluating the user index choice.
        if 1 <= index < len(tasks):
            # Storing removed task in a variable then Removes it from the list
            removed_task = tasks.pop(index-1)
            # Prints the removed task. 
            print(f"Task Removed: {removed_task['task']}")
        else:
            print("Enter a valid task number.")
    except ValueError:
        print("Please enter a number.")


def completed_task():
    """Performs the completion of tasks."""
    view_task()
    # Checks whether there are tasks.
    if not tasks:
        return
 
    # Prompting the user for a task number to mark as completed
    index = int(input("Enter task number: "))
    if 1 <= index <= len(tasks):
        # Mark task as completed
        tasks[index-1]['completed'] = True
        # Printing the completed task
        print(f"Marked as completed: {tasks[index-1]['task']}")
    else:
        print("Invalid task number.")


def save_task():
    """Saves a file suggested by a user with all the tasks added"""
    # Checking whether there are tasks
    if not tasks:
        return

    # Prompting a user for a file name to save the tasks
    FILENAME = input("Enter a file name with \".txt\" (file.txt): ")
    # Writing all the tasks to the file added by the user
    with open(FILENAME, 'w') as file:
        file.write("To-do List.\n")
        for i, task in enumerate(tasks, start=1):
            # formatting the contents in the file as a nicely-formatted list.
            file.write(f"{i}. {task['task']}\n")

    # Notifying the user about the saving action done.
    print(f"Task saved to {FILENAME} succesfully!")


def load_task():# COMING SOON...
    ...
    

if __name__ == "__main__":
    main()