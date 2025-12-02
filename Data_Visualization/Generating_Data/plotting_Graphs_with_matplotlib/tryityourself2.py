import matplotlib
matplotlib.use('TKAgg')

import matplotlib.pyplot as plt

class ColorMapCube:
    # This function handles the full operation of the plotting
    def color_Map_cube():
        # Initializing the x and y axes values to be plotted
        input_values = range(1, 5001)
        cubes_values = [x**3 for x in input_values]

        cmp = plt.cm.Blues

        # Calling the scatter function that handles the plotting of the graphs
        plt.scatter(input_values, cubes_values, c=cubes_values, cmap=cmp, edgecolor='none', s=20)

        # Setting the title and lables of axes
        plt.title("Cubes of Numbers", fontsize=16)
        plt.xlabel("Values", fontsize=14)
        plt.ylabel("Cubes of the values",fontsize=14)

        # Add the axes
        #plt.axes([1, 5000, 1, 130000000000])

        # Saves the an image
        plt.savefig('try_it_yourself2.png', bbox_inches='tight')

        # Show the plotted graph
        plt.show()


# Main function
def main():
    color_map_cubes = ColorMapCube
    color_map_cubes.color_Map_cube()


# Entry point
if __name__ == "__main__":
    main()