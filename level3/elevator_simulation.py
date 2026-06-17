class Elevator:
	"""Initializing the Elevator class"""
	def __init__(self, floors):
		"""Initializing the class constructors and the instance attributes"""
		self.current_floor = 1
		self.total_floors = floors

	def move_to_floor(self, requested_floor):
		if requested_floor < 1 or requested_floor > self.total_floors:
			print(f"Invalid floor: {requested_floor}.")
			return

		print(f"Elevator moving from Floor: {self.current_floor} to {requested_floor}...")
		if requested_floor > self.current_floor:
			self.go_up(requested_floor)
		elif requested_floor < self.current_floor:
			self.go_down(requested_floor)
		else:
			print("Elevator is already here...")

		self.current_floor = requested_floor
		print(f"Elevator has arrived at Floor {self.current_floor}.\n")
		print("Door is opening...")

	def go_up(self, to_floor):
		for floor in range(self.current_floor + 1, to_floor + 1):
			print(f"Going up... Floor {floor}")

	def go_down(self, to_floor):
		for floor in range(self.current_floor - 1, to_floor - 1, -1):
			print(f"Going down... Floor {floor}")

def run_simulation():
	building_floors = 11
	elevator = Elevator(building_floors)

	while True:
		print(f"Elevator is on Floor {elevator.current_floor}.")
		user_input = input(f"Enter floor to go to ( 1 to {building_floors}, or 'q' to quit'): ")

		if user_input.lower() == 'q':
			print("Simulation ended!")
			break

		if user_input.isdigit():
			requested_floor = int(user_input)
			elevator.move_to_floor(requested_floor)
		else:
			print("Invalid Floor Number.")



if __name__ == "__main__":
	run_simulation()