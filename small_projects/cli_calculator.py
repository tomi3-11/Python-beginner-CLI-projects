
def main():
    #ans1 = add(4, 5)
    #print(f"The addition result is {ans1}")

    #ans2 = subtract(5, 2)
    #print(f"The subtraction result is {ans2}")

    #ans3 = multiply(5, 2)
    #print(f"The multiply result is {ans3}")

    #ans4 = divide(5, 2)
    #print(f"The divide result is {ans4}")


    while True:
        try:
            num1 = int(input("Enter the first name: "))
            num2 = int(input("Enter the first name: "))
            operator = input("Enter a valid operator (+, -, /, *): ")

            if operator == "+":
                print(add(num1, num2))
            elif operator == "-":
                print(subtract(num1, num2))
            elif operator == "*":
                print(multiply(num1, num2))
            elif operator == "/":
                print(divide(num1, num2))
            else:
                print("Invalid operation")

            continue_cal = input("Do you want to continue? (y/n)").lower()
            if continue_cal != "y":
                print("Exiting cal")
                break
        except ValueError:
            print("Error: Invalid type")
        except ZeroDivisionError:
            print("Error: Cannot divide a number by zero.")
        except Exception as e:
            print(f"Error: {e}.")


def add(num1: int, num2: int) -> int:
    """Add two numbers and return the result."""
    return num1 + num2


def subtract(num1: int, num2: int) -> int:
    """Subtract two numbers and return the result."""
    return num1 - num2


def multiply(num1: int, num2: int) -> int:
    return num1 * num2


def divide(num1: int, num2: int) -> int:
    return num1 / num2


if __name__ == "__main__":
    main()
