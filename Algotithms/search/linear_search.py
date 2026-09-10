def linear_search(arr, key):
    n = len(arr)

    for i in range(n):
        if key == arr[i]:
            return f"Found: {arr[i]}"
    return "Not Found"


def main():
    arr = [45, 6, 3, 90, 22, 65]
    print(arr)
    key = int(input("Enter a number to look for: "))

    print(linear_search(arr, key))


if __name__ == "__main__":
    main()
