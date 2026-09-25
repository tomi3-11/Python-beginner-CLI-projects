from datetime import datetime, timedelta

# Global Variables to store books and their status

books = []
borrowed_books = []

def main():
    """Main function to run the Library system."""
    setup_sample_data()

    while True:
        display_menu()
        choice = int(input("Enter your Choice (1 - 8): "))

        if choice == 1:
            display_books(books, "All books in the Library")
        elif choice == 2:
            available = [book for book in books['available']]
            display_books(available, "Available Books")
        elif choice == "3":
            display_books(borrowed_books, "Boorowed Books")
        elif choice == "4":
            overdue = get_overdue_books()
            display_books(overdue, "OverDue Books")
        elif choice == "5":
            isbn = input("Enter the ISBN of the book you want to borrow: ")
            borrower = input("Enter your name: ")
            days = input("Enter loan period in days (default 14 days): ")
            try:
                days = int(days) if days else 14
            except ValueError:
                print("Invalid input. Using the default 14 days.")
                days = 14
            borrow_book(isbn, borrower, days)
        elif choice == "6":
            isbn = input("Enter the ISBN of the book you want to return: ")
            return(isbn)
        elif choice == "7":
            title = input("Enter book title: ")
            author = input("Enter Author name: ")
            isbn = input("Enter ISBN: ")
            if find_book(isbn=isbn):
                print("A Book with the isbn already exist!")
            else:
                add_book(title, author, isbn)
        elif choice == "8":
            print("Thanks for using the Library Management System.")
            break
        else:
            print("Invalid Choice Please try again.")


def add_book(title, author, isbn):
    """Add a new book to the library."""
    books.append({
        'title': title,
        'author': author,
        'isbn': isbn,
        'available': True
    })
    print(f"Book '{title}' added successfully")


def find_book(isbn=None, title=None):
    """Find a book by ISBN or title"""
    for book in books:
        if (isbn and book['isbn'] == isbn) or (title and book['title'].lower() == title.lower()):
            return book
        return None
    

def borrow_book(isbn, borrower_name, loan_period_days=14):
    """Borrow a book from the library."""
    book = find_book(isbn=isbn)

    if not book:
        print("Book not found.")
        return False
    
    if not book['available']:
        print("Book is already Borrowed")
        return False
    
    book['available'] = False
    book['borrower'] = borrower_name
    book['due_date'] = datetime.now() + timedelta(days=loan_period_days)
    borrowed_books.append(book)
    print(f"Book '{book['title']}' borrowed successfully! Due date: {book['due_date'].strftime('%Y-%M-%d')}")
    return True


def return_book(isbn):
    """Return a book to the library"""
    book = find_book(isbn=isbn)

    if not book:
        print("Book not found!")
        return False
    
    if book['available']:
        print("Book wasn't borrowed.")
        return False
    
    book['available'] = True
    book.pop('borrower', None)
    book.pop('due_date', None)

    #Removed from borrowed_books list
    for i, b in enumerate(borrowed_books):
        if b['isbn'] == isbn:
            borrowed_books.pop(i)
            break

    print(f"Book '{book['title']}' return successfully!")
    return True


def display_books(book_list, title):
    """Display a list of books with a title"""
    print(f"\n{title}:")
    if not book_list:
        print("No books found.")
        return
    
    for book in book_list:
        status = f"Title: {book['title']}, Author: {book['author']}, ISBN: {book['isbn']}"
        if book.get('avalable', True):
            status += ", Status: Available"
        else:
            status += f", Status: Borrowed by {book['borrower']}, Due Date: {book['due_date'].strftime('%Y-%M-%d')}"
        print(status)


def get_overdue_books():
    """Get the list of overdue books"""
    overdue = []
    for book in borrowed_books:
        if book['due_date'] < datetime.now():
            overdue.append(book)
    return overdue

"""
Enhancement:
1. Notify User if due_date passed.
2. User credentials should include their email.



"""


def display_menu():
    """Display the main menu."""
    print("\nLibrary Management System")
    print("1. Display all books")
    print("2. Display available books")
    print("3. Display borrowed books.")
    print("4. Display overdue books.")
    print("5. Borrow a book")
    print("6. Return a book")
    print("7. Add a new book.")
    print("8. Exit")


def setup_sample_data():
    """Initialize with some sample books"""
    add_book("The Great Gatsby", "F. Scott Fitzgerald", "9780743273565")
    add_book("To kill a mockingbird", "Harper Lee", "9780061120084")
    add_book("1984", "George Orwell", "9780451524935")
    add_book("Pride and Prejudice", "Jane Austen", "9780141439518")




if __name__ == "__main__":
    main()
    
    
    
"""
Bugs to Fix
1. Date time.
2. Status.
3. program crashes.


"""