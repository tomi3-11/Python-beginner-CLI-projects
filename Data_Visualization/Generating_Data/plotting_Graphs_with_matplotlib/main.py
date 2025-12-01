import matplotlib
matplotlib.use("TKAgg")

import matplotlib.pyplot as plt 

def main():
    print("Hello from plotting-graphs-with-matplotlib!")
    plotting()


def plotting():
    squares = [1, 4, 9, 16, 25]

    plt.plot(squares)
    plt.show()


if __name__ == "__main__":
    main()
