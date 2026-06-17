class CLICalculator:
    def __init__(self, num1, num2, operator):
        self.num1 = num1
        self.num2 = num2
        self.operator = operator

    def add(self):
        """Add two numbers and return the result."""
        result = self.num1 + self.num2
        return f"The sum of {self.num1} and {self.num2} is {result}."

    def subtract(self) -> str:
        """Subtract two numbers and return the result."""
        result = self.num1 - self.num2
        return f"The difference btn {self.num1} and {self.num2} is {result}."

def main():
    #ans1 = add(4, 5)
    #print(f"The addition result is {ans1}")

    #ans2 = subtract(5, 2)
    #print(f"The subtraction result is {ans2}")

    #ans3 = multiply(5, 2)
    #print(f"The multiply result is {ans3}")

    #ans4 = divide(5, 2)
    #print(f"The divide result is {ans4}")
    continuous_menu()

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

            continue_cal = input("Do you want to continue? (y/n) ").lower()
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


def continuous_menu():
    """A menu for continuous selction."""

    menu = """
    Welcome to the CLI Computer.

    Here are the accepted operations:
    1. Addition
    2. Subraction
    3. Multiply
    4. Divide

    Datatype: int
    """

    print(menu)


if __name__ == "__main__":
    main()
