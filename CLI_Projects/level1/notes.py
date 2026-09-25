import os

# Creating the file name to store notes.
FILENAME = 'notes.txt'

def main(): 
    while True: 
        show_menu()   
        choice = input("Enter choice: ")

        if choice == '1':
            note = input("Write notes here: ")
            write_notes(note)
        elif choice == '2':
            note = input("Append notes here: ")
            append_notes(note)
        elif choice == '3':
            read_notes()
        elif choice == '4':
            delete_notes()
        elif choice == '5':
            print("Goodbye!!")
            break
        else: 
            print("Invalid Input! ")


def write_notes(note):
    """Adding notes to a file"""
    # Writing to the file
    with open(FILENAME, 'w') as file:
        file.write(note + '\n')
    print("Note written to file.")

def append_notes(note):
    """Appending notes to a file."""
    with open(FILENAME, 'a') as file:
        file.write(note + '\n')

    print("Notes appended to the file.")

def read_notes():
    """Reading the notes in a file."""
    # Checking the availability of (FILENAME) in the directory as the program.
    if not os.path.exists(FILENAME):
        print("No notes found.")
        return
    # Reading contents in the file.
    with open(FILENAME, 'r') as file:
        notes = file.readlines()
        print("\n--- Your Notes ---")
        for note in notes:
            print(note.strip())


def delete_notes():
    """Removing notes from the file."""
    # Checking the availability of (FILENAME) in the directory as the program.
    if os.path.exists(FILENAME):
        os.remove(FILENAME) # Removing the file completly from the directory
        print("All notes deleted.")
    else:
        print("No notes files to delete.")


def show_menu():
    """Giving options to the user to choose from."""
    print("\n--- Notes App Menu ---")
    print("1. Write new note (overwrite)")
    print("2. Append note")
    print("3. Read notes")
    print("4. Delete notes")
    print("5. Exit")

if __name__ == "__main__":
    main()