import matplotlib
matplotlib.use('TKAgg')

import matplotlib.pyplot as plt

def main():
    print("Hello from Scatter plot world.")
    scatter()


def scatter():
    """Function that handles the scatter plot"""
    #squares = [2, 4]

    x_values = range(1, 1001)
    y_values = [x**2 for x in x_values]

    #plt.scatter(x_values, y_values, edgecolor='none', c=(0,0,0.8), s=20)
    plt.scatter(x_values, y_values, edgecolor='none', c=y_values, s=20, cmap=plt.cm.Blues)

    """Title and lables for the axes"""
    plt.title("Scatter plot for square of numbers")
    plt.xlabel("Value", fontsize=14)
    plt.ylabel("Square of the values", fontsize=14)

    # Set the param tick
    plt.tick_params(axis='both', labelsize=14, which='major')

    # Set the axis range
    plt.axis([0, 1100, 0, 1100000])

    plt.savefig('scatter_plot.png', bbox_inches='tight')

    # Showing the graph
    plt.show()


if __name__ == "__main__":
    main()