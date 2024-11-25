noTriangle = 1

def printTriangle(triangleCount):
    for new_line in range(1, 6):
        for _ in range(1, triangleCount + 1):
            print("^ " * new_line, end="  " * (6 - new_line))
        print()

printTriangle(noTriangle)
while True:
    ui = input(" Do you wish to continue print triangle? ( yes / no ) ---> ")
    if ui.lower().strip() == "no":
        print(" Program / Loop terminated")
        break
    elif ui.lower().strip() == "yes":
        noTriangle += 1
        printTriangle(noTriangle)
    elif ui.lower().strip() == "reduce":
        noTriangle -= 1
        printTriangle(noTriangle)
    else:
        print(" Invalid input, try again\n")
        continue