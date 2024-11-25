max = int(input(" Enter max number of asterisk (Must be even number): \n "))
half = max // 2 - 1

if not max % 2 == 0:
    print(" Must be even number.")
else:
    for line in range(2, max-1, 2):
        print(" " * (max - line), end="")
        print(" *" * line)
        
    print(" *" * max)
    
    for line in range(1, max - half):
        print("  " * half, end=" * *\n")