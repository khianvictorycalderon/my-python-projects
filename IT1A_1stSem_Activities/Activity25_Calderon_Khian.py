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