# DO NOT COPY PASTE THIS CODE
# WHOEVER DISTRIBUTE THIS CODE MAY FACE LEGAL CONSEQUENCE
# THIS IS AN INTELLECTUAL PROPERTY OF KHIAN VICTORY D. CALDERON
# THOU SHALT NOT COPY FILES WITHOUT PROPER AUTHORIZATION

def PrintTopics():
    print()
    print("Activities: ")
    print("Activity 2 - Print")
    print("Activity 3 - Print with Variables")
    print("Activity 4 - Eval and Input")
    print("Activity 5 - Asignment Operator")
    print("Activity 6 - Asignment Operator with Formatted String")
    print("Activity 7 - Conditional Statement")
    print("Activity 8 - Data Conversion with Conditional Statement")
    print("Activity 9 - Elif Statement")
    print("Activity 10 - Nested Conditional Statement")
    print("Activity 11 - For Loop")
    print("Activity 12 - For Loop Reverse Step")
    print("Activity 13 - For Loop Factorial")
    print("Activity 14 - Nested For Loop")
    print("Activity 15 - Nested For Loop")
    print("Activity 16 - For Loop Triangle")
    print("Activity 17 - Multiplication Table For Loop")
    print("Activity 18 - Dynamic Triangle")
    print("Activity 19 - Five Names")
    print("Activity 20 - Triangle with Hybrid Loop")
    print("Activity 21 - Names with Hybrid Loop")
    print("Activity 22 - Functions")
    print("Activity 23 - Documentation Strings")
    print("Activity 24 - Importing")
    print("Activity 25 - List (also known as Array)")
    print()
    print("Code Challenges: ")
    print("Code Challenge 1 - Escape Sequences")
    print("Code Challenge 2 - Input")
    print("Code Challenge 3 - Multiple Input with Value Display")
    print("Code Challenge 4 - Eval with Formatted String")
    print("Code Challenge 5 - Data Types (Float and Round)")
    print("Code Challenge 6 - Formula Computation")
    print("Code Challenge 7 - Grocerry Discount")
    print("Code Challenge 8 - Accumulation")
    print("Code Challenge 9 - Right Triangle")
    print("Code Challenge 10 - Diamond Asterisk (Even Number)")
    print("Code Challenge 11 - Diamond Asterisk (Odd Number)")
    print("Code Challenge 12 - Arrow Shape Asterisk (Even Number)")
    print("Code Challenge 13 - Diamond Numbers")
    print("Code Challenge 14 - Summation")
    print("Code Challenge 15 - Dynamic Triangle")
    print("Code Challenge 16 - Bank System")
    print()
    print("Type 'Show List' to show this list.")
    print("Type 'Exit' to stop the program.")
    print("-" * 50)
    
def Continue():
    print()
    input("Press any key to continue...")
    print("-" * 50)
# --------------------------------------------------------------------------------
# Activities
def Activity2():
    print("""---------------\nCode:
a = 5 + 5
b = 2 - 1
print(f"5 + 5 is {a} \\n 2 - 1 is {b}")
# Basic Operations""")
    print("---------------\nOutput:")
    a = 5 + 5
    b = 2 - 1
    print(f"5 + 5 is {a}\n2 - 1 is {b}")
    # Basic Operations
    
def Activity3():
    print("""---------------\nCode:
print("Multiple Input Activity 3 by Khian Calderon BSIT-1A Computer Programming 1")

name = input("What's your name? --> ")
age = input("How old are you? --> ")
email = input("What is your email? --> ")
gender = input("Are you a Male or Female? --> ")
contact = input("What is your contact number? --> ")
married = input("Are you married? Yes or No? --> ")

print("\n Welcome",name,"your age is",age,"and your email is",email,"and your gender is",gender,"and your contact number is",contact,"and are you married?",married)""")
    print("---------------\nOutput:")
    print("Multiple Input Activity 3 by Khian Calderon BSIT-1A Computer Programming 1")
    name = input("What's your name? --> ")
    age = input("How old are you? --> ")
    email = input("What is your email? --> ")
    gender = input("Are you a Male or Female? --> ")
    contact = input("What is your contact number? --> ")
    married = input("Are you married? Yes or No? --> ")
    print("\n Welcome",name,"your age is",age,"and your email is",email,"and your gender is",gender,"and your contact number is",contact,"and are you married?",married)

def Activity4():
    print("""---------------\nCode:
number1 = eval(input("Enter a number: "))
number2 = eval(input("Enter a number: "))
print(f"The sum of {number1} + {number2} is {number1 + number2}")""")
    print("---------------\nOutput:")
    number1 = eval(input("Enter a number: "))
    number2 = eval(input("Enter a number: "))
    print(f"The sum of {number1} + {number2} is {number1 + number2}")

def Activity5():
    print("""---------------\nCode:
# Assignment operator
a = 1
print(a)

a += 2
print(a)

a -=1
print(a)""")
    print("---------------\nOutput:")
    # Assignment operator
    a = 1
    print(a)

    a += 2
    print(a)

    a -=1
    print(a)

def Activity6():
    print("""---------------\nCode:
#Assignment variable
#This is a comment

x = 5
print(f"{x}")

x = x + 10
print(f"{x}")

x += 15
print(f"{x}")""")
    print("---------------\nOutput:")
    #Assignment variable
    #This is a comment

    x = 5
    print(f"{x}")

    x = x + 10
    print(f"{x}")

    x += 15
    print(f"{x}")


def Activity7():
    print("""---------------\nCode:
# Ask the user for the gold input
gold = 0
miner = input("What is your name? --> ")
isGold = input("Is your mineral gold? --> ")

# Converts the user input to lower case
if isGold.lower() == "yes":
    gold += 1
    print(f"Hello {miner}, your gold is {gold}")
else:
    print(f"Hello {miner}, your gold is {gold}")""")
    print("---------------\nOutput:")
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
    print("""---------------\nCode:
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
print("Activity 8, Calderon Khian Victory D. ")""")
    print("---------------\nOutput:")
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
    print("""---------------\nCode:
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
    print("You are Senior Citizen")""")
    print("---------------\nOutput:")
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
    print("""---------------\nCode:
# Python demo for nested condition

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
    print("THank your for using the system!")""")
    print("---------------\nOutput:")
    # Python demo for nested condition

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
    print("""---------------\nCode:
y = 0
for i in range(y,5):
    print(i)""")
    print("---------------\nOutput:")
    y = 0
    for i in range(y,5):
        print(i)

def Activity12():
    print("""---------------\nCode:
# Reverse Step
for i in range(10,1,-1):
    print(i)
    
for x in range(10, 2, -2):
    print(x)""")
    print("---------------\nOutput:")
    # Reverse Step
    for i in range(10,1,-1):
        print(i)
        
    for x in range(10, 2, -2):
        print(x)

def Activity13():
    print("""---------------\nCode:
fac = 1
num = int(input("Enter a number: "))
for i in range(num, 1, -1):
    fac *= i
print(f"The factorial of {num} is {fac}")""")
    print("---------------\nOutput:")
    fac = 1
    num = int(input("Enter a number: "))
    for i in range(num, 1, -1):
        fac *= i
    print(f"The factorial of {num} is {fac}")    

def Activity14():
    print("""---------------\nCode:
for x in range(0,11):
    print(x, end = " ")
    for y in range(0, 11):
        print("*", end=" ")""")
    print("---------------\nOutput:")
    for x in range(0,11):
        print(x, end = " ")
        for y in range(0, 11):
            print("*", end=" ")

def Activity15():
    print("""---------------\nCode:
for x in range(0,11):
    print("", x, end = "")
    for y in range(0, x):
        print("*", end = "")
    print("\n")    """)
    print("---------------\nOutput:")
    for x in range(0,11):
        print("", x, end = "")
        for y in range(0, x):
            print("*", end = "")
        print("\n")    

def Activity16():
    print("""---------------\nCode:
lines = int(input("How many * ?\n "))
inv = 0
for a in range(lines, 0, -1):
    print(" " * inv, end = "")
    print("* " * a)
    inv += 2""")
    print("---------------\nOutput:")
    lines = int(input("How many * ?\n "))
    inv = 0
    for a in range(lines, 0, -1):
        print(" " * inv, end = "")
        print("* " * a)
        inv += 2

def Activity17():
    print("""---------------\nCode:
ui = int(input("Enter mumber of columns: "))
for lines in range(1,ui+1):
    print(f" {lines}", end="")
    for product in range(2,ui+1):
        print(f"\t{product * lines}",end="")
    print()""")
    print("---------------\nOutput:")
    ui = int(input("Enter mumber of columns: "))
    for lines in range(1,ui+1):
        print(f" {lines}", end="")
        for product in range(2,ui+1):
            print(f"\t{product * lines}",end="")
        print()

def Activity18():
    print("""---------------\nCode:
ui = int(input("Enter number of triangles: "))

for new_line in range(1, 6):
    for line in range(1, ui + 1):
        print("* " * new_line, end="  " * (6 - new_line))
    print()""")
    print("---------------\nOutput:")
    ui = int(input("Enter number of triangles: "))

    for new_line in range(1, 6):
        for line in range(1, ui + 1):
            print("* " * new_line, end="  " * (6 - new_line))
        print()

def Activity19():
    print("""---------------\nCode:
print(" Enter 5 names, type stop to terminate names")

for x in range(0,5):
    ui = input(" Enter your name: ")
    if ui.lower().strip() == "stop":
        print(" Program terminated.")
        break
    else:
        print(f" Hello {ui}")""")
    print("---------------\nOutput:")
    print(" Enter 5 names, type stop to terminate names")

    for x in range(0,5):
        ui = input(" Enter your name: ")
        if ui.lower().strip() == "stop":
            print(" Program terminated.")
            break
        else:
            print(f" Hello {ui}")

def Activity20():
    print("""---------------\nCode:
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
    else:
        print(" Invalid input, try again\n")
        continue""")
    print("---------------\nOutput:")
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
        else:
            print(" Invalid input, try again\n")
            continue

def Activity21():
    print("""---------------\nCode:
print(" Keep asking for name until user type stop. Type 'stop' to terminate the program.")
names = []

while True:
    ui = input(" Enter name: ")
    if ui.lower().strip() == "stop":
        for name in names:
            print(f" {name}")
        break
    else:
        names.append(ui)""")
    print("---------------\nOutput:")
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
    print("""---------------\nCode:
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

print(" Thank you for using me.")""")
    print("---------------\nOutput:")
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

def Activity23():
    print('''---------------\nCode:
def greet(name):
    """ Returns a Hello user statement """ 
    # Documentation Strings
    return f" Hello there {name}."

print(greet("Alice"))''')
    def greet(name):
        """ Returns a Hello user statement """ 
        # Documentation Strings
        return f" Hello there {name}."

    print(greet("Alice"))

def Activity24():
    print("""---------------\nCode:
from Activity23_Calderon_Khian import greet
# Importing

print(greet("John"))""")
    print("---------------\nOutput:")
    print(" Hello there John")

def Activity25():
    print("""---------------\nCode:
# List methods (I like to call this Array)

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
print(" -------------------")""")
    print("---------------\nOutput:")
    # List methods (I like to call this Array)

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

# --------------------------------------------------------------------------------
# Code challenges
def CodeChallenge1():
    print("""---------------\nCode:
print("\n\t\t\t\t\t\t\t\t\t\t      *\n\t\t\t\t\t\t\t\t\t\t    * * *\n\t\t\t\t\t\t\t\t\t\t  * * * * *\n\t\t\t\t\t\t\t\t\t\t* * * * * * *\n\t\t\t\t\t\t\t\t\t\t  * * * * *\n\t\t\t\t\t\t\t\t\t\t    * * *\n\t\t\t\t\t\t\t\t\t\t      *")""")
    print("---------------\nOutput:")
    print("\n\t\t\t\t\t\t\t\t\t\t      *\n\t\t\t\t\t\t\t\t\t\t    * * *\n\t\t\t\t\t\t\t\t\t\t  * * * * *\n\t\t\t\t\t\t\t\t\t\t* * * * * * *\n\t\t\t\t\t\t\t\t\t\t  * * * * *\n\t\t\t\t\t\t\t\t\t\t    * * *\n\t\t\t\t\t\t\t\t\t\t      *")

def CodeChallenge2():
    print("""---------------\nCode:
name = input("What is your name?")
print("\n\t\t\t\t\t\t\t\t\t\t      *\n\t\t\t\t\t\t\t\t\t\t    * * *\n\t\t\t\t\t\t\t\t\t\t  * * * * *\n\t\t\t\t\t\t\t\t\t\t* Hi " + name + " *\n\t\t\t\t\t\t\t\t\t\t  * * * * *\n\t\t\t\t\t\t\t\t\t\t    * * *\n\t\t\t\t\t\t\t\t\t\t      *")""")
    print("---------------\nOutput:")
    name = input("What is your name?")
    print("\n\t\t\t\t\t\t\t\t\t\t      *\n\t\t\t\t\t\t\t\t\t\t    * * *\n\t\t\t\t\t\t\t\t\t\t  * * * * *\n\t\t\t\t\t\t\t\t\t\t* Hi " + name + " *\n\t\t\t\t\t\t\t\t\t\t  * * * * *\n\t\t\t\t\t\t\t\t\t\t    * * *\n\t\t\t\t\t\t\t\t\t\t      *")

def CodeChallenge3():
    print("""---------------\nCode:
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

print("\n Welcome",name,AgeDetect(age),"and your email is",email,GenderDetect(gender),"and your contact number is",contact,"and",MarriageDetect(married))""")
    print("---------------\nOutput:")
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

def CodeChallenge4():
    print("""---------------\nCode:
print("Python Coding Challenge Arithmetic Operator by Khian Calderon BSIT-1A")
num1 = eval(input("Enter your first number: "))
num2 = eval(input("Enter your second number: "))
print(f"The sum of {num1} and {num2} is {num1 + num2}")
print(f"The difference of {num1} and {num2} is {num1 - num2}")
print(f"The product of {num1} and {num2} is {num1 * num2}")
print(f"The quotient of {num1} and {num2} is {num1 / num2}")
print(f"{num1} Exponent of {num2} is {num1 ** num2}")
print(f"The remainder of {num1} and {num2} is {num1 % num2}")
print(f"The floor division of {num1} and {num2} is {num1 // num2}")""")
    print("---------------\nOutput:")
    print("Python Coding Challenge Arithmetic Operator by Khian Calderon BSIT-1A")
    num1 = eval(input("Enter your first number: "))
    num2 = eval(input("Enter your second number: "))
    print(f"The sum of {num1} and {num2} is {num1 + num2}")
    print(f"The difference of {num1} and {num2} is {num1 - num2}")
    print(f"The product of {num1} and {num2} is {num1 * num2}")
    print(f"The quotient of {num1} and {num2} is {num1 / num2}")
    print(f"{num1} Exponent of {num2} is {num1 ** num2}")
    print(f"The remainder of {num1} and {num2} is {num1 % num2}")
    print(f"The floor division of {num1} and {num2} is {num1 // num2}")

def CodeChallenge5():
    print("""---------------\nCode:
f = float(input("Enter your fahreheit input: "))
c = round((f - 32) * (5/9),2)
print(f"{f} fahreneheit is equal to {c} celsius")
print("Code Challenge 5 by Khian Victory D. Calderon")""")
    print("---------------\nOutput:")
    f = float(input("Enter your fahreheit input: "))
    c = round((f - 32) * (5/9),2)
    print(f"{f} fahreneheit is equal to {c} celsius")
    print("Code Challenge 5 by Khian Victory D. Calderon")

def CodeChallenge6():
    print("""---------------\nCode:
prelim = float(input("What is your prelim Grade? --> "))
midterm = float(input("What is your midterm Grade? --> "))
semi = float(input("What is your semi finals Grade? --> "))
finals = float(input("What is your finals Grade? --> "))
quiz = float(input("What is your quiz Grade? --> "))
project = float(input("What is your project Grade? --> "))

# Final Grade
fg = (prelim * 0.15) + (midterm * 0.15) + (semi * 0.15) + (finals * 0.15) + (quiz * 0.25) + (project * 0.15)

# Conditional Statement
if (fg >= 75 and fg <= 100):
    print("Congratulations, you have passed")
elif (fg >= 100 or fg <= 0):
    print("Invalid grade")
else:
    print("Sorry you failed")""")
    print("---------------\nOutput:")
    prelim = float(input("What is your prelim Grade? --> "))
    midterm = float(input("What is your midterm Grade? --> "))
    semi = float(input("What is your semi finals Grade? --> "))
    finals = float(input("What is your finals Grade? --> "))
    quiz = float(input("What is your quiz Grade? --> "))
    project = float(input("What is your project Grade? --> "))

    # Final Grade
    fg = (prelim * 0.15) + (midterm * 0.15) + (semi * 0.15) + (finals * 0.15) + (quiz * 0.25) + (project * 0.15)

    # Conditional Statement
    if (fg >= 75 and fg <= 100):
        print("Congratulations, you have passed")
    elif (fg >= 100 or fg <= 0):
        print("Invalid grade")
    else:
        print("Sorry you failed")
        
    print("Code Challenge 8 by Khian Calderon, BSIT-1A")

def CodeChallenge7():
    print("""---------------\nCode:
# Grocerry System
isBought = str(input("Did you buy a grocerry?: (Yes/No)\n"))
if isBought.lower() == "yes":
    itemName = str(input("Name of the item:\n"))
    itemPrice = float(input("Price of the item:\n"))
    age = int(input("Age: \n"))
    amountGiven = float(input("Amount Given:\n"))

    # Undiscounted prices
    totalPrice = round(float(itemPrice + (itemPrice * 0.123)),2)
    change = round(float(amountGiven - totalPrice),2)

    # Discounted prices
    totalPriceWithDiscount = round(totalPrice - (totalPrice * 0.052),2)
    changeWithDiscount = round(float(amountGiven - totalPriceWithDiscount),2)
    
    if age >= 60:
        print(f"Hi senior citizen customer, you purchased a/an {itemName} with a price of {itemPrice} plus 12.3% tax (30.75php)")
        print(f"Total cost: {totalPriceWithDiscount} including the 5.2% discount.")
        print(f"Amount Given: {amountGiven}")
        print(f"Change: {changeWithDiscount}")
    else:
        print(f"Hi customer, you purchased a/an {itemName} with a price of {itemPrice} plus 12.3% tax (30.75php)")
        print(f"Total cost: {totalPrice}")
        print(f"Amount Given: {amountGiven}")
        print(f"Change: {change}")
else:
    print("Thank you, you did not buy anything.")""")
    print("---------------\nOutput:")
    # Grocerry System
    isBought = str(input("Did you buy a grocerry?: (Yes/No)\n"))
    if isBought.lower() == "yes":
        itemName = str(input("Name of the item:\n"))
        itemPrice = float(input("Price of the item:\n"))
        age = int(input("Age: \n"))
        amountGiven = float(input("Amount Given:\n"))

        # Undiscounted prices
        totalPrice = round(float(itemPrice + (itemPrice * 0.123)),2)
        change = round(float(amountGiven - totalPrice),2)

        # Discounted prices
        totalPriceWithDiscount = round(totalPrice - (totalPrice * 0.052),2)
        changeWithDiscount = round(float(amountGiven - totalPriceWithDiscount),2)
        
        if age >= 60:
            print(f"Hi senior citizen customer, you purchased a/an {itemName} with a price of {itemPrice} plus 12.3% tax (30.75php)")
            print(f"Total cost: {totalPriceWithDiscount} including the 5.2% discount.")
            print(f"Amount Given: {amountGiven}")
            print(f"Change: {changeWithDiscount}")
        else:
            print(f"Hi customer, you purchased a/an {itemName} with a price of {itemPrice} plus 12.3% tax (30.75php)")
            print(f"Total cost: {totalPrice}")
            print(f"Amount Given: {amountGiven}")
            print(f"Change: {change}")
    else:
        print("Thank you, you did not buy anything.")

def CodeChallenge8():
    print("""---------------\nCode:
accumulations = 0

for x in range(1,11):
    current_number = float(input(f"Enter input {x} -> "))
    accumulations += current_number
    
print(f"The total of all numbers you inputted is {accumulations}")    
print("Code Challenge 8 by Khian Calderon, BSIT-1A")    """)
    print("---------------\nOutput:")
    accumulations = 0

    for x in range(1,11):
        current_number = float(input(f"Enter input {x} -> "))
        accumulations += current_number
        
    print(f"The total of all numbers you inputted is {accumulations}")    
    print("Code Challenge 8 by Khian Calderon, BSIT-1A")    

def CodeChallenge9():
    print("""---------------\nCode:
inv = 0
for a in range(10, 0, -1):
    print(" " * inv, end = "")
    print("* " * a)
    inv += 2""")
    print("---------------\nOutput:")
    inv = 0
    for a in range(10, 0, -1):
        print(" " * inv, end = "")
        print("* " * a)
        inv += 2

def CodeChallenge10():
    print("""---------------\nCode:
max = int(input("Enter the max number of asterisks (must be an even number): "))

if not max % 2 == 0:
    print(" Must be an even number.")
else:
    for line in range(2, max+1, 2):
        print(" " * (max - line), end="")
        print(" *" * line)
    for line in range(max, 0, -2):
        print(" " * (max - line), end="")
        print(" *" * line)""")
    print("---------------\nOutput:")
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

def CodeChallenge11():
    print("""---------------\nCode:
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
""")
    print("---------------\nOutput:")
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

def CodeChallenge12():
    print("""---------------\nCode:
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
        print("  " * half, end=" * *\n")""")
    print("---------------\nOutput:")
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

def CodeChallenge13():
    print("""---------------\nCode:
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
        print()""")
    print("---------------\nOutput:")
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

def CodeChallenge14():
    print("""---------------\nCode:
sum = 0
while True:
    ui = int(input(" Enter a number --> "))
    sum += ui
    if ui == 0:
        print(" The loop has terminated")
        print(f" The sum of all the numbers given is {sum}")
        break""")
    print("---------------\nOutput:")
    sum = 0
    while True:
        ui = int(input(" Enter a number --> "))
        sum += ui
        if ui == 0:
            print(" The loop has terminated")
            print(f" The sum of all the numbers given is {sum}")
            break

def CodeChallenge15():
    print("""---------------\nCode:
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
        continue""")
    print("---------------\nOutput:")
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

def CodeChallenge16():
    print("""---------------\nCode:
def deposit(balance, amount):
    balance += amount
    print(f"Deposited: ₱{amount}")
    return balance

def withdraw(balance, amount):
    denominations = [1000, 500, 200, 100, 50, 20, 10, 5, 1]
    if amount > balance:
        print("Insufficient balance!")
        return balance
    else:
        print(f"Withdrawing: ₱{amount}")
        balance -= amount
        for denomination in denominations:
            count = int(amount // denomination)
            if count > 0:
                print(f"{count} x ₱{denomination}")
            amount %= denomination
        return balance

def bank_system():
    balance = 0
    while True:
        print("\nWelcome to the Bank System!")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Exit")
        
        choice = input("Please choose an option (1-4): ")

        if choice == "1":
            try:
                amount = float(input("Enter amount to deposit: ₱"))
                if amount > 0:
                    balance = deposit(balance, amount)
                else:
                    print("Amount must be greater than zero!")
            except ValueError:
                print("Invalid input. Please enter a valid amount.")
        
        elif choice == "2":
            try:
                amount = float(input("Enter amount to withdraw: ₱"))
                if amount > 0:
                    balance = withdraw(balance, amount)
                else:
                    print("Amount must be greater than zero!")
            except ValueError:
                print("Invalid input. Please enter a valid amount.")
        
        elif choice == "3":
            print(f"Current balance: ₱{balance}")
        
        elif choice == "4":
            print("Thank you for using the banking system. Goodbye!")
            break
        
        else:
            print("Invalid option! Please choose a valid option (1-4).")

bank_system()""")
    print("---------------\nOutput:")
    def deposit(balance, amount):
        balance += amount
        print(f"Deposited: ₱{amount}")
        return balance

    def withdraw(balance, amount):
        denominations = [1000, 500, 200, 100, 50, 20, 10, 5, 1]
        if amount > balance:
            print("Insufficient balance!")
            return balance
        else:
            print(f"Withdrawing: ₱{amount}")
            balance -= amount
            for denomination in denominations:
                count = int(amount // denomination)
                if count > 0:
                    print(f"{count} x ₱{denomination}")
                amount %= denomination
            return balance

    def bank_system():
        balance = 0
        while True:
            print("\nWelcome to the Bank System!")
            print("1. Deposit")
            print("2. Withdraw")
            print("3. Check Balance")
            print("4. Exit")
            
            choice = input("Please choose an option (1-4): ")

            if choice == "1":
                try:
                    amount = float(input("Enter amount to deposit: ₱"))
                    if amount > 0:
                        balance = deposit(balance, amount)
                    else:
                        print("Amount must be greater than zero!")
                except ValueError:
                    print("Invalid input. Please enter a valid amount.")
            
            elif choice == "2":
                try:
                    amount = float(input("Enter amount to withdraw: ₱"))
                    if amount > 0:
                        balance = withdraw(balance, amount)
                    else:
                        print("Amount must be greater than zero!")
                except ValueError:
                    print("Invalid input. Please enter a valid amount.")
            
            elif choice == "3":
                print(f"Current balance: ₱{balance}")
            
            elif choice == "4":
                print("Thank you for using the banking system. Goodbye!")
                break
            
            else:
                print("Invalid option! Please choose a valid option (1-4).")

    bank_system()

PrintTopics()
while True:
    print()
    choose = input("Choose which activity or code challenge you want to run:\n-> ")
    if choose.lower() == "exit":
        print("\nThank you for using this Program!")
        print("Final Project by: Khian Victory D. Calderon")
        print("BSIT-1A")
        print("Submitted to: Professor Leonard Andrew Mesiera")
        print("-" * 50)
        break
    elif choose.lower() == "show list":
        PrintTopics()
    elif choose.lower() == "activity 2":
        Activity2()
        Continue()
    elif choose.lower() == "activity 3":
        Activity3()
        Continue()
    elif choose.lower() == "activity 4":
        Activity4()
        Continue()
    elif choose.lower() == "activity 5":
        Activity5()
        Continue()
    elif choose.lower() == "activity 6":
        Activity6()
        Continue()
    elif choose.lower() == "activity 7":
        Activity7()
        Continue()
    elif choose.lower() == "activity 8":
        Activity8()
        Continue()
    elif choose.lower() == "activity 9":
        Activity9()
        Continue()
    elif choose.lower() == "activity 10":
        Activity10()
        Continue()
    elif choose.lower() == "activity 11":
        Activity11()
        Continue()
    elif choose.lower() == "activity 12":
        Activity12()
        Continue()
    elif choose.lower() == "activity 13":
        Activity13()
        Continue()
    elif choose.lower() == "activity 14":
        Activity14()
        Continue()
    elif choose.lower() == "activity 15":
        Activity15()
        Continue()
    elif choose.lower() == "activity 16":
        Activity16()
        Continue()
    elif choose.lower() == "activity 17":
        Activity17()
        Continue()
    elif choose.lower() == "activity 18":
        Activity18()
        Continue()
    elif choose.lower() == "activity 19":
        Activity19()
        Continue()
    elif choose.lower() == "activity 20":
        Activity20()
        Continue()
    elif choose.lower() == "activity 21":
        Activity21()
        Continue()
    elif choose.lower() == "activity 22":
        Activity22()
        Continue()
    elif choose.lower() == "activity 23":
        Activity23()
        Continue()
    elif choose.lower() == "activity 24":
        Activity24()
        Continue()
    elif choose.lower() == "activity 25":
        Activity25()
        Continue()
    elif choose.lower() == "code challenge 1":
        CodeChallenge1()
        Continue()
    elif choose.lower() == "code challenge 2":
        CodeChallenge2()
        Continue()
    elif choose.lower() == "code challenge 3":
        CodeChallenge3()
        Continue()
    elif choose.lower() == "code challenge 4":
        CodeChallenge4()
        Continue()
    elif choose.lower() == "code challenge 5":
        CodeChallenge5()
        Continue()
    elif choose.lower() == "code challenge 6":
        CodeChallenge6()
        Continue()
    elif choose.lower() == "code challenge 7":
        CodeChallenge7()
        Continue()
    elif choose.lower() == "code challenge 8":
        CodeChallenge8()
        Continue()
    elif choose.lower() == "code challenge 9":
        CodeChallenge9()
        Continue()
    elif choose.lower() == "code challenge 10":
        CodeChallenge10()
        Continue()
    elif choose.lower() == "code challenge 11":
        CodeChallenge11()
        Continue()
    elif choose.lower() == "code challenge 12":
        CodeChallenge12()
        Continue()
    elif choose.lower() == "code challenge 13":
        CodeChallenge13()
        Continue()
    elif choose.lower() == "code challenge 14":
        CodeChallenge14()
        Continue()
    elif choose.lower() == "code challenge 15":
        CodeChallenge15()
        Continue()
    elif choose.lower() == "code challenge 16":
        CodeChallenge16()
        Continue()
    else:
        print("Invalid input, try again!")