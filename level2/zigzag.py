import time, sys

#print("Hello,", sys.argv[1])


# Assigning a default value for the spaces to indent
indent = 0
# Boolean: Whether the indentation is increasing or not
indent_increasing = True

try:
	#Main Loop
	while True:
		print(' ' * indent, end='')
		print('********')
		# Pause for 1/10 of a second
		time.sleep(0.1)
		
		if indent_increasing:
			# Increase the number of spaces
			indent += 1
			if indent == 15:
				# Change direction:
				indent_increasing = False
				
		else:
			# decrease the number of spaces
			indent -= 1
			if indent == 0:
				# Change direction
				indent_increasing = True
				
except KeyboardInterrupt:
	sys.exit()
