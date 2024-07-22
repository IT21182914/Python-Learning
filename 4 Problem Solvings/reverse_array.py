def reverse_array(arr):
    n = len(arr)
    for i in range(n // 2):  # // for integer division.
        temp = arr[i]
        arr[i] = arr[n - 1 - i]
        arr[n - 1 - i] = temp

        # arr[i], arr[n - 1 - i] = arr[n - 1 - i], arr[i] # Pythonic way of swapping two numbers called tuple unpacking.


if __name__ == "__main__":
    array = [5, 4, 2, 7, 8, 6]
    reverse_array(array)
    print("Reversed Array: ")
    for j in range(len(array)):
        print(array[j])
