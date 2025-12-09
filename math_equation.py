import math

# Define the function
def calculate_y(x):
    return math.cos(x) - math.log(x) + math.exp(-x)


def main():
    while True:
        # Ask the user for x
        x = float(input("Enter the value of x (x > 0): "))

        # Calculate y
        y = calculate_y(x)

        # Display the result
        print(f"\nFor x = {x}, y = {y:.4f}")
    
    
if __name__ == "__main__":
    main()
