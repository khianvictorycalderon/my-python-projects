lines = int(input("How many * ?\n "))
inv = 0
for a in range(lines, 0, -1):
    print(" " * inv, end = "")
    print("* " * a)
    inv += 2