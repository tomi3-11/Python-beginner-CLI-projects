tasks = []

def main():
    while True:
        print("1. Add | 2. View | 3. Remove |")
        option = input("Enter choice: ")

        if option == "1":
            task = input("Enter task: ").strip()
            add_task(task)
        elif option == "2":
            view_task(task)
        elif option == "3":
            remove_task(task)
        else:
            return "Invalid Input."
        
        choice = input("Do you want to continue? (y/n): ").lower()
        if choice != "y" and "yes":
            print("\nMy Final To-do List.")
            for index, task in enumerate(tasks, start=1):
                print(f"{index}. {task}")
            print("\nGoodbye")
            break


def add_task(task):
    if task:
        tasks.append(task)
        print("Task added successfully.")
    else:
        return "Please enter task"


def view_task(task):
    
    if tasks:
        print("To-do List.")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")
    else:
        return "No task added."
    

def remove_task(task):
    view_task(task)
    index = int(input("Enter task number to be removed: "))
    if 0 <= index < len(tasks):
        tasks.pop(index)
        print("Task Removed!")
    else:
        print("Enter a valid task number.")
    

if __name__ == "__main__":
    main()