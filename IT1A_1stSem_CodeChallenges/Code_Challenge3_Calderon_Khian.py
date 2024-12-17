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