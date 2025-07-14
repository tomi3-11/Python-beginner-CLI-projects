import random
import string

def generato_password(length=12, use_digits=True, use_special=True):
    # Basic Characters
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation
    
    # Combine characters set based on user preference
    characters = letters
    if use_digits:
        characters += digits
    if use_special:
        characters += special
        
    # Ensure at least on character from each chosen set.
    password = []
    if use_digits:
        password.append(random.choice(digits))
        
    if use_special:
        password.append(random.choice(special))
        
    while len(password) < length:
        password.append(random.choice(characters))
        
    # Shuffle to avoid predictable positions
    random.shuffle(password)
    
    return "".join(password)

# Example Usage
print("Generated Password: ", generato_password(length=15))
    