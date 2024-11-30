


def Activity2():
    a = 5 + 5
    b = 2 - 1

    print(f"5 + 5 is {a} \n 2 - 1 is {b}")
    # Basic Operations



def Activity3():
    print("Multiple Input Activity 3 by Khian Calderon BSIT-1A Computer Programming 1")
    name = input("What's your name? --> ")
    age = input("How old are you? --> ")
    email = input("What is your email? --> ")
    gender = input("Are you a Male or Female? --> ")
    contact = input("What is your contact number? --> ")
    married = input("Are you married? Yes or No? --> ")

    def AgeDetect(x):
        age = int(x)
        if(age > 0 and age < 18):
            return "you are a minor"
        elif(age >= 18 and age <60):
            return "you are an adult"
        elif(age >= 60 and age <= 150):
            return "you are a senior citizen"
        elif(age > 150):
            return "you are immortal"
        else:
            return "your age seems a bit odd"
        
    def MarriageDetect(x):
        isMarried = str(x).lower()
        if(isMarried == "t" or isMarried == "true" or isMarried == "yes" or isMarried == "yep"):
            return "you are married"
        elif(isMarried == "f" or isMarried == "false" or isMarried == "no" or isMarried == "nope"):
            return "you are not married"
        else:
            return "ain't sure if you are married or not"

    def GenderDetect(x):
        gender = str(x).lower()
        if(gender == "m" or gender == "male" or gender == "boy" or gender == "man" or gender == "men"):
            return "you are male"
        elif(gender == "f" or gender == "female" or gender == "girl" or gender == "woman" or gender == "women"):
            return "you are female"
        else:
            return "not sure what your gender is"

    print("\n Welcome",name,AgeDetect(age),"and your email is",email,GenderDetect(gender),"and your contact number is",contact,"and",MarriageDetect(married))







def Activity4():
    number1 = eval(input("Enter a number: "))
    number2 = eval(input("Enter a number: "))
    print(f"The sum of {number1} + {number2} is {number1 + number2}")




def Activity5():
    # Assignment operator
    a = 1
    print(a)

    a += 2
    print(a)

    a -=1
    print(a)




def Activity6():
    #Assignment variable
    #This is a comment

    x = 5
    print(f"{x}")

    x = x + 10
    print(f"{x}")

    x += 15
    print(f"{x}")



def Activity7():
    # Ask the user for the gold input
    gold = 0
    miner = input("What is your name? --> ")
    isGold = input("Is your mineral gold? --> ")

    # Converts the user input to lower case
    if isGold.lower() == "yes":
        gold += 1
        print(f"Hello {miner}, your gold is {gold}")
    else:
        print(f"Hello {miner}, your gold is {gold}")
        
        
        
def Activity8():
    password = str(input("Enter your password --> ").lower())
    if password == "secret":
        print("Enjoy!")
        print("Access Granted")
    elif password == "pogiako123":
        print("Ikaw na")
        print("Access Granted")
    else:
        print("Wrong Password, Access Denied")
        
    print("Thank your for using the program, enjoy!")
    print("Activity 8, Calderon Khian Victory D. ")


def Activity9():
    age = int(input("Enter your age --> "))
    def inRange(a,x,y):
        if y == "infinity":
            if a >= x:
                return True
            else:
                return False
        elif a >= x and a <= y:
            return True
        else:
            return False
            
    if inRange(age,1,7):
        print("You are Toddler")
    elif inRange(age,8,13):
        print("You are in a PreTeen")
    elif inRange(age,14,18):
        print("You are a Teenager")
    elif inRange(age,19,31):
        print("You are in Early Adulthood")
    elif inRange(age,32,45):
        print("You are in Middle Adulthood")
    elif inRange(age,46,59):
        print("You are in Post Adulthood")
    elif inRange(age,60,"infinity"):
        print("You are Senior Citizen")
        

def Activity10():
    #python demo for nested condition
    #Data filtration program

    name = input("Enter your name :     ")
    isStudent = input("Are you a current student of DLL (yes / no):     ")

    if isStudent.lower() == "yes":
        yearLevel = input("What year are you currently enrolled on? \nF - Freshmen\nS - Sophomore\nJ - Junior\nSN - Senior\n")
        if yearLevel.lower() == "f":
            print(f"Hi {name}, Freshmen, welcome to DLL")
        elif yearLevel.lower() == "s":
            print(f"Hi {name}, Junior, welcome to DLL")
    else:
        print("THank your for using the system!")



def Activity11():
    y = 0
    for i in range(y,5):
        print(i)


def Activity12():
    # Reverse Step
    for i in range(10,1,-1):
        print(i)
        
    for x in range(10, 2, -2):
        print(x)
    


def Activity13():
    fac = 1
    num = int(input("Enter a number: "))
    for i in range(num, 1, -1):
        fac *= i
    print(f"The factorial of {num} is {fac}")    
    


def Activity14():
    for x in range(0,11):
        print(x, end = " ")
        for y in range(0, 11):
            print("*", end=" ")
    


def Activity15():
    for x in range(0,11):
        print("", x, end = "")
        for y in range(0, x):
            print("*", end = "")
        print("\n")    
    


def Activity16():
    lines = int(input("How many * ?\n "))
    inv = 0
    for a in range(lines, 0, -1):
        print(" " * inv, end = "")
        print("* " * a)
        inv += 2
    


def Activity17():
    ui = int(input("Enter mumber of columns: "))
    for lines in range(1,10+1):
        print(f" {lines}", end="")
        for product in range(2,ui+1):
            print(f"\t{product * lines}",end="")
        print()
    


def Activity18():
    ui = int(input("Enter number of triangles: "))
    for new_line in range(1, 6):
        for line in range(1, ui + 1):
            print("* " * new_line, end="  " * (6 - new_line))
        print()
    


def Activity19():
    print(" Enter 5 names, type stop to terminate names")
    for x in range(0,5):
        ui = input(" Enter your name: ")
        if ui.lower().strip() == "stop":
            print(" Program terminated.")
            break
        else:
            print(f" Hello {ui}")
    


def Activity20():
    print(" Create a Triangle using hybrid loop")
    noTriangle = 1

    def printTriangle(triangleCount):
        for new_line in range(1, 6):
            for _ in range(1, triangleCount + 1):
                print("* " * new_line, end="  " * (6 - new_line))
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
        elif ui.lower().strip() == "reduce" or ui.lower().strip() == "decrease":
            noTriangle -= 1
            printTriangle(noTriangle)
        else:
            print(" Invalid input, try again\n")
            continue



def Activity21():
    print(" Keep asking for name until user type stop. Type 'stop' to terminate the program.")
    names = []
    while True:
        ui = input(" Enter name: ")
        if ui.lower().strip() == "stop":
            for name in names:
                print(f" {name}")
            break
        else:
            names.append(ui)



def Activity22():
    def Activity16():
        lines = int(input("How many * ?\n "))
        inv = 0
        for a in range(lines, 0, -1):
            print(" " * inv, end = "")
            print("* " * a)
            inv += 2
            
    def Activity17():
        ui = int(input("Enter mumber of columns: "))
        for lines in range(1,10+1):
            print(f" {lines}", end="")
            for product in range(2,ui+1):
                print(f"\t{product * lines}",end="")
            print()
            
    def Activity18():
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
            Activity16()
        elif choose.lower().strip() == "b":
            Activity17()
        elif choose.lower().strip() == "c":
            Activity18()
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
    



def Activity23():
    def greet(name):
        """ Returns a Hello user statement """ 
        # Documentation Strings
        return f" Hello there {name}."
    print(greet("John"))
    



def Activity24(): # Importing
    def greet(name):
        """ Returns a Hello user statement """ 
        # Documentation Strings
        return f" Hello there {name}."
    print(greet("John"))
    
    



def Activity25():
    #List
    fruits = ["Apple","Banana","Orange","Grapes","Mango","Dalandan"]
    print("",fruits) # Prints all the fruits as array format
    print("",fruits[1]) # Prints Banana
    print(" -------------------")

    fruits.append("Guyabano") # Adds Guyabano to the list
    print(" Added Guyabano")
    print("",fruits)
    print(" -------------------")

    fruits.remove("Orange") # Removed Orange from the list
    print(" Removed Orange")
    print("",fruits)
    print(" -------------------")

    fruits.insert(2, "Pineapple") # Inserts Pineapple to the list
    print(" Inserted Pineapple at the middle")
    print("",fruits)
    print(" -------------------")

    fruits.reverse() # Reverse the order of the array
    print(" Reversed the order of the array")
    print("",fruits)
    print(" -------------------")

    print(" For each fruits:") # Prints all Fruits each line
    for fruit in fruits:
        print("",fruit)
    print(" -------------------")






# --------------------------------------------------------------------------------------
# Main Runner of the program

print(" Type the number of activity you want to execute from 2 - 25.")
print(" Activity 1 is a picture, so no need to call it.")
print(" Type TERMINATE to stop the program. \n")

while True:
    Xui = input(" Choose Activity: ")
    if Xui.upper().strip() == "TERMINATE":
        print(" Program terminated, thank you for using me.")
        break
    try:
        number = int(Xui)
        if 2 <= number <= 25:
            eval(f"Activity{number}()")
            print("\n Activty execution done, you may choose another.")
        else:
            print(" Invalid input, please try again.\n")
    except ValueError:
        print(" Invalid input, please try again.\n")
