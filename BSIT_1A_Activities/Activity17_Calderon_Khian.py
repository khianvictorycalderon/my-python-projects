ui = int(input("Enter mumber of columns: "))
for lines in range(1,10+1):
    print(f" {lines}", end="")
    for product in range(2,ui+1):
        print(f"\t{product * lines}",end="")
    print()