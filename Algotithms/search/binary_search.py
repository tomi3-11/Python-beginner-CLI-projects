def binary_search(arr, key):
    n = len(arr)
    left = 0
    right = n - 1

    while left <= right:
        mid = (left + right)//2
        if arr[mid] == key:
            return mid

        if arr[mid] < key:
            left = mid + 1
        else:
            right = mid - 1

    return -1


def main():
    arr = [1, 4, 5, 7, 8, 44, 88, 22, 14, 45]
    print(arr)
    key = int(input("Enter a number to find: "))

    result = binary_search(arr, key)

    if result != -1:
        print("Value", key,"Found at index", result)
    else:
        print("Target not found in array.")


if __name__ == "__main__":
    main()
