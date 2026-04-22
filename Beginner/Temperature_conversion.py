
def main():
	while True: 
		# Prompting the User for a temperature 
		temp = float(input("Enter the temperature: "))
		
			
		# Error handling in action
		try:
			# Prompting the User for a choice whether celsius or fahrenheit.
			choice = input("Would you like to convert to Celsius or Fahrenheit? ").lower()
			
			# Evaluating user choice.
			if choice == 'fahrenheit':
				print(convert_to_fahrenheit(temp))
			elif choice == 'celsius':
				print(convert_to_celsius(temp))
			else:
				print("Please enter either 'celsius' or 'fahrenheit'.")
		except ValueError:
			print("Please enter a valid number.")
			
		# Evaluating user input if they want to continue or not.
		if input("\nDo you want to continue? (yes/no): ").lower() != 'yes':
			print("Goodbye\n")
			break
        
def convert_to_fahrenheit(temp):
	"""Converts the given temperature to fahrenheit."""
	fahrenheit = 9/5 * temp + 32
	return f"Temperature: {fahrenheit} F"
	
def convert_to_celsius(temp):
	"""Converts the given temperature to celsius."""
	celsius = 5/9 * (temp - 32)
	return f"Temperature: {celsius} C"
	
if __name__ == '__main__':
	main()
	
