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