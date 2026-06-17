import random


def guessing_game():
    secret = random.randint(1, 100)

    attempts = 0

    while attempts < 5: 
        guess = int(input("Enter a number to guess: "))
        attempts += 1

        if guess < secret:
            print("Too low!")
        elif guess > secret:
            print("Too high!")
        else:
            break

    if guess == secret:
        print(f"Congrats!, you guessed it right in {attempts} guesses!")
    else:
        print(f"Sorry the number was {secret}")

guessing_game()

