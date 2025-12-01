import matplotlib
matplotlib.use("TKAgg")

import matplotlib.pyplot as plt 

def main():
    print("Hello from plotting-graphs-with-matplotlib!")
    plotting()


def plotting():
    squares = [1, 4, 9, 16, 25]

    plt.plot(squares, linewidth=5)
    plt.title("Square Numbers", fontsize=24)
    plt.xlabel("Value", fontsize=14)
    plt.ylabel("Square of Value", fontsize=14)

    # Set size of tick labels
    plt.tick_params(axis='both', labelsize=14)
    plt.show()


if __name__ == "__main__":
    main()
