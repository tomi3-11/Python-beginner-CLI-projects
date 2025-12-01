import matplotlib
matplotlib.use("TKAgg")

import matplotlib.pyplot as plt 

def main():
    print("Hello from plotting-graphs-with-matplotlib!")
    plotting()


def plotting():
    # Setting the input values as X axis
    input_values = [1, 2, 3, 4, 5]
    # setting the squares as Y axis
    squares = [1, 4, 9, 16, 25]
    # Plotting the x and y axis
    plt.plot(input_values, squares, linewidth=5)
    plt.title("Square Numbers", fontsize=24)
    plt.xlabel("Value", fontsize=14)
    plt.ylabel("Square of Value", fontsize=14)

    # Set size of tick labels
    plt.tick_params(axis='both', labelsize=14)
    plt.show()


if __name__ == "__main__":
    main()
