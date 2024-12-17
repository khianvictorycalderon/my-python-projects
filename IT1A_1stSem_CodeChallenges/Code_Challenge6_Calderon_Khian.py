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