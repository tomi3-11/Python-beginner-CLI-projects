import matplotlib
matplotlib.use('TKAgg')

import matplotlib.pyplot as plt

class PlaneCubes:

    def plane_cubes():
        # Plotting the first five values
        #input_values = range(1, 6)
        #cubes_values = [x**3 for x in input_values ]


        # Plotting the first 5000 values
        input_values = range(1, 50001)
        cubes_values = [x**3 for x in input_values ]

        # Calling the scatter() function that handles the plotting of the values
        plt.scatter(input_values, cubes_values, s=40)

        # Scatter Plot titles and labels
        plt.title("Cubes of Numbers", fontsize=16)
        plt.xlabel("Values", fontsize=14)
        plt.ylabel("Cubes of the values", fontsize=14)

        # Calling the function to show the graph
        plt.show()


# Main function to handle creation of objects
def main():
    cubes = PlaneCubes
    cubes.plane_cubes()


# Entry point
if __name__ == "__main__":
    main()
