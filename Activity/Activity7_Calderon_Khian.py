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