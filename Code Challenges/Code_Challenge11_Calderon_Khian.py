max = int(input("Enter the max number of asterisks (must be an odd number): "))

if max % 2 == 0:
    print(" Must be an odd number.")
else:
    for row in range(1, max - 1, 2):
        for space in range((max - row) // 2):
            print("  ", end="")
        for asterisk in range(row):
            print("* ", end="")
        print()

    print("* " * max)

    for row in range(max - 2, 0, -2):
        for space in range((max - row) // 2):
            print("  ", end="")
        for asterisk in range(row):
            print("* ", end="")
        print()
