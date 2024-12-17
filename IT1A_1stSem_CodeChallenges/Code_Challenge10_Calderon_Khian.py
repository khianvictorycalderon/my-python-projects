max = int(input("Enter the max number of asterisks (must be an even number): "))

if not max % 2 == 0:
    print(" Must be an even number.")
else:
    for line in range(2, max+1, 2):
        print(" " * (max - line), end="")
        print(" *" * line)
    for line in range(max, 0, -2):
        print(" " * (max - line), end="")
        print(" *" * line)