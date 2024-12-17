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