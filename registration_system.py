def main():
    users = [] # Store user details (first name, last name, email)
    print("User Registration\n")

    while True:
        """
            Prompting the user for inputs
            1. first Name
            2. Last Name
            3. Email
        """
        first_name = input("First Name: ")
        last_name = input("Last Name: ")
        email = input("Email: ")
        # Adds users inputs to the Users list (Array)
        users.append((first_name, last_name, email))

        # Performing operation on whether a user wants to register another user.
        another_user = input("Do you want to add another user (yes/no)? ").lower()
        if another_user != "yes":
            print("Thanks for registering!")
            break
     
    print("\nThanks for registering. ")
    # Displays the table with all registered users
    details_table(users)
    print("\n")
        


def details_table(users):
    # Header with fixed-width columns
    # first_name = "First Name"
    header = f"| {'First Name':<12} | {'last Name':<12} | {'Email':<30} |"
    print(header)
    # Styling the table with Hyphens
    print("-" * len(header))
    # Looping through each of the item in the users list. (first name, last name, email)
    for first_name, last_name, email in users:
        # Formating their display wuith fixed-width column
        row = f"| {first_name:<12} | {last_name:<12} | {email:<30} |"
        print(row)


if __name__ == "__main__":
    main()