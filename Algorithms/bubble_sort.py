def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp

                # arr[j], arr[j + 1] = arr[j + 1], arr[j]
                # this is the pythonic way of swapping two numbers called tuple unpacking.


if __name__ == "__main__":
    array = [5, 4, 2, 7, 8, 6]
    bubble_sort(array)
    print("Sorted Array: ")
    for i in range(len(array)):
        print(array[i])
