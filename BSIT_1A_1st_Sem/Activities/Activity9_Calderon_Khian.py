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
    
