import random 

def main():
    """Asking for coin flip"""

    print("\nTo flip a coin enter [flip]")
    print("To Exit enter [No]")

    """Input validation"""
    Input = input("Your choice: ")
    Flip = validate_input(Input)

    """Coin flip simulation"""
    coin_flip(Flip)
    

def validate_input(Input):
    if Input.lower() == "flip":
        print("\nLets flip a coin...")
        Flip = True
        return Flip

    elif Input.lower() == "no":
        print("\nOk, as you wish...")
        exit(1)
    else:
        print("\nNeed a valid input")
    
def coin_flip(Flip):
    if Flip:
        draw = random.choice(["Head", "Tail"])
        print(f"\nCoin fliped and it was a {draw} !!!")


if __name__ == "__main__":
    main()