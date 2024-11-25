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