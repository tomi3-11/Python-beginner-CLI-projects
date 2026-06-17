
def main():
    ans1 = add(4, 5)
    print(f"The addition result is {ans1}")

    ans2 = subtract(5, 2)
    print(f"The subtraction result is {ans2}")

    ans3 = multiply(5, 2)
    print(f"The multiply result is {ans3}")

    ans4 = divide(5, 2)
    print(f"The divide result is {ans4}")


def add(num1: int, num2: int) -> int:
    """Add two numbers and return the result."""
    return num1 + num2


def subtract(num1: int, num2: int) -> int:
    """Subtract two numbers and return the result."""
    return num1 - num2


def multiply(num1: int, num2: int) -> int:
    return num1 * num2


def divide(num1: int, num2: int) -> int:
    if num2 == 0:
        return 
    return num1 / num2


if __name__ == "__main__":
    main()
