# Renamed to Sub_ to avoid conflicts with the final project
def Sub_Activity16():
    lines = int(input("How many * ?\n "))
    inv = 0
    for a in range(lines, 0, -1):
        print(" " * inv, end = "")
        print("* " * a)
        inv += 2
        
def Sub_Activity17():
    ui = int(input("Enter mumber of columns: "))
    for lines in range(1,10+1):
        print(f" {lines}", end="")
        for product in range(2,ui+1):
            print(f"\t{product * lines}",end="")
        print()
        
def Sub_Activity18():
    ui = int(input("Enter number of triangles: "))
    for new_line in range(1, 6):
        for line in range(1, ui + 1):
            print("* " * new_line, end="  " * (6 - new_line))
        print()
        
tryAgain = ""
while True:
    if tryAgain.lower().strip() == "no":
        break
    choose = input(" Choose activity you want to execute: \n A = Activity 16\n B = Activity 17\n C = Activity 18\n ")
    if choose.lower().strip() == "a":
        Sub_Activity16()
    elif choose.lower().strip() == "b":
        Sub_Activity17()
    elif choose.lower().strip() == "c":
        Sub_Activity18()
    else:
        print(" Invalid input, try again: ")
        continue
    print()
    while True:
        tryAgain = input(" Do you want to try again? yes / no\n ")
        if tryAgain.lower().strip() == "yes":
            break
        elif tryAgain.lower().strip() == "no":
            break
        else:
            print(" Invalid answer, try again")
            continue

print(" Thank you for using me.")