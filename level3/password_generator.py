# import random
# import string

# def generato_password(length=12, use_digits=True, use_special=True):
#     # Basic Characters
#     letters = string.ascii_letters
#     digits = string.digits
#     special = string.punctuation
    
#     # Combine characters set based on user preference
#     characters = letters
#     if use_digits:
#         characters += digits
#     if use_special:
#         characters += special
        
#     # Ensure at least one character from each chosen set.
#     password = []
#     if use_digits:
#         password.append(random.choice(digits))
        
#     if use_special:
#         password.append(random.choice(special))
        
#     while len(password) < length:
#         password.append(random.choice(characters))
        
#     # Shuffle to avoid predictable positions
#     random.shuffle(password)
    
#     return "".join(password)

# # Example Usage
# print("Generated Password: ", generato_password(length=15))
    
    
import string
import random

def main():
    
    # Prompting user for filename
    filename = input("Enter filename to store password in: ")
    # Prompting user for password length
    length = int(input("Enter password length: "))
    character_list = ''
    # Menu and users choice of password characters
    print('''Choose character set for password from these : 
         1. Digits
         2. Letters
         3. Special characters
         4. Exit''')
    while True:
        choice = int(input("Pick a number: "))
        if choice == 1:
            # Adding letters
            character_list += string.ascii_letters
        elif choice == 2:
            # Adding digits
            character_list += string.digits
        elif choice == 3:
            # Adding special characters
            character_list += string.punctuation
        elif choice == 4:
            break
        else:
            print("Please pick a valid option!")
            
    # Calling the function     
    password_generator(length, character_list, filename)
    
    
def password_generator(length, character_list, filename):
    password = []
    for i in range(length):
        # Picking a random character from the character list.
        random_char = random.choice(character_list)
        
        # appending a random character to password
        password.append(random_char)
        
    # printing the password as a string
    random_password = "".join(password)
    with open(filename, 'w') as f:
        f.write(random_password)
    print("The random password is " + random_password)
    
    
if __name__ == "__main__":
    main()