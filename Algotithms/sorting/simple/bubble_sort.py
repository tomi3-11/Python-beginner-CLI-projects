def bubble_sort(arr):
    for i in range(len(arr)):
        swapped = False
        for j in range(0, len(arr) - i - 1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True

        if (swapped == False):
            break

def main():
    arr = [2, 5, 7, 1, 9, 6]
    bubble_sort(arr)

    print("Sorted Array")
    for i in range(len(arr)):
        print("%d" % arr[i], end=" ")


if __name__ == "__main__":
    main()
