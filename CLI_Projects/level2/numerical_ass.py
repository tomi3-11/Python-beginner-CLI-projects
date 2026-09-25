import math

# Define the function
def calculate_y(x):
    """
    Calculates a math function
    
          1  
    y = ───── ⋅ e^(-x²/2)
        √(2π)
    
    """
    
    
    return (1 / math.sqrt(2 * math.pi)) * math.exp(-(x ** 2) / 2)

def main():
    while True:
        # Ask user for x
        x = float(input("Enter the value of x: "))

        # Calculate y
        y = calculate_y(x)

        # Display the result
        print(f"\nFor x = {x}, y = {y:.4f}")
        
if __name__ == "__main__":
    main()
