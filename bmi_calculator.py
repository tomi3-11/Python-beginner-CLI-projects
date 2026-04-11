def main():
    """Unit's selection"""
    print("Choose input units:\n" 
        "Enter 1 for Metric (kg, cm)\n" 
        "Enter 2 for Imperial (lbs, ft and inches)\n"
        "Enter 3 to Quit\n")
    
    choice = int(input("Your choice: "))

    unit_selection(choice)

    """inputs"""
    height, weight = inputs_conversions(choice)

    print(f"So, Your current height is {height:.2f}m and weight {weight:.1f}kg")

    """BMI calculation"""
    bmi = bmi_calculator(height, weight)
    print(f"Your BMI is {bmi:.1f}")

    """BMI category"""
    bmi_category(bmi)

def unit_selection(choice):
    
    match choice:
        case 1:
            print("ok you choose Metric units.")
        case 2:
            print("ok you choose Imperial unit.")
        case 3:
            quit(1)
        case _:
            print("That was not a valid choice.")
            quit(1)

def inputs_conversions(choice):
    match choice:
        case 1:
            height = int(input("Enter Your height in cm: "))
            weight = float(input("Enter Your weight in kg: "))

            height = height/float(100)

        case 2:
            print("For height:\n")
            ft = int(input("Enter Your height's ft: "))
            inches = int(input("Enter Your height's inches: "))
            weight = float(input("Enter Your weight in lbs: "))

            height = ft * float(0.3048) + inches * float(0.0254)
            weight = weight * float(0.4536)
        
    return height, weight
        
def bmi_calculator(height, weight):
    bmi = weight / (height ** 2)
    return bmi
    

def bmi_category(bmi):
    if bmi < 18.5:
        print("You are underweight.")
    elif 18.5 <= bmi < 25:
        print("You are normal weight.")
    elif 25 <= bmi < 30:
        print("You are overweight.")
    else:
        print("You are obese.")

if __name__ == "__main__":
    main()