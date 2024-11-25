fac = 1
num = int(input("Enter a number: "))
for i in range(num, 1, -1):
    fac *= i
print(f"The factorial of {num} is {fac}")    