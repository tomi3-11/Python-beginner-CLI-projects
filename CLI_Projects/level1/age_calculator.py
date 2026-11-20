# Simple Age Calculator 
from datetime import date

"""
ask for user inputs
check their input
calculate their age
return the age.

"""

# Get input from the user
user_age = int(input("Enter your birth year: "))

# Calculate the Age
age = date.today().year - user_age

# print the age
print(age)