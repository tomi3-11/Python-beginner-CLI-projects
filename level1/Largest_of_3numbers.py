
def main():
    numbers = [6, 7, 13, 2, 5, 9]
    result = largest_of_three(numbers)
    print(result)    
    
def largest_of_three(numbers):
    n = len(numbers)
    maximum = numbers[0]
    
    for i in range(n):
        if numbers[i] > maximum:
            maximum = numbers[i]
            
    return f"The largest number is {maximum}"    
if __name__ == "__main__":
    main()