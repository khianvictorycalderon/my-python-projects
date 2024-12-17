max = int(input(" Enter the highest number you want to be in display (Must be an odd number): \n "))

if max % 2 == 0:
    print(" Must be an odd number.")
else:
    # Upper part
    print("  " * (max - 1) + "1")
    for line in range(2, max + 1):
        print("  " * (max - line), end="")
        for numRight in range(line, 1, -1):
            print(f"{numRight} ",end="")
        for numLeft in range(1, line + 1):
            print(f"{numLeft} ",end="")
        print()
    
    # Lower part
    for lineReverse in range(max - 1, 0, -1):
        print("  " * (max - lineReverse), end="")
        for numRight in range(lineReverse, 1, -1):
            print(f"{numRight} ", end="")
        for numLeft in range(1, lineReverse + 1):
            print(f"{numLeft} ", end="")
        print()