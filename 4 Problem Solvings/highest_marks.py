if __name__ == "__main__":
    students = []
    n = int(input("How many students are in your class? "))

    for i in range(n):
        marks = int(input(f"Student {i + 1} marks: "))
        students.append(marks)  # Append means ADD the element to the end of the list

    highest = students[0]
    for i in range(1, n):  # Start from the second element
        if students[i] > highest:
            highest = students[i]

    print("The highest marks is:", highest)
