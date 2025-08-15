""" This is a simple hard coded chat bot"""

while True:
    # Prompting user for input
    chat = input("User: ").lower()
    
    if "hello" in chat:
        print("Hello how are you?")
    elif "fine and you" in chat:
        print("Am good also.")
    elif chat in ['exit', 'quit', 'bye']:
        print("Have a good day")
        break
    else:
        print("sorry i don't understand what you are saying.")
        