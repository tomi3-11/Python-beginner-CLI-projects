import matplotlib
matplotlib.use('TKAgg')

import matplotlib.pyplot as plt

def main():
    print("Hello from Scatter plot world.")
    scatter()


def scatter():
    """Function that handles the scatter plot"""
    #squares = [2, 4]

    x_values = [x for X in range(20)]
    y_values = [x**2 for x in range(20)]

    plt.scatter(x_values, y_values, s=200)

    """Title and lables for the axes"""
    plt.title("Scatter plot for square of numbers")
    plt.xlabel("Value", fontsize=14)
    plt.ylabel("Square of the values", fontsize=14)

    # Showing the graph
    plt.show()


if __name__ == "__main__":
    main()