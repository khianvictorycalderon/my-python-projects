ui = int(input("Enter number of triangles: "))

for new_line in range(1, 6):
    for line in range(1, ui + 1):
        print("* " * new_line, end="  " * (6 - new_line))
    print()