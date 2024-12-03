def print_statements_menu():
    
    """Submenu for print statements."""
    
    print("\n--- Print Statements Menu ---")
    print("Example 1: Print a simple message")
    print('Code: print("Hello, World!")')
    print("Output:")
    print("Hello, World!")
    input("Press Enter to return to the main menu...\n")


def variables_menu():
    
    """Submenu for variables."""
    
    print("\n--- Variables Menu ---")
    print("Example 1: Declare and print a variable")
    print('Code: name = "Lucena"\nprint(f"Welcome to {name}!")')
    print("Output:")
    print("Welcome to Lucena!")
    input("Press Enter to return to the main menu...\n")


def operators_menu():
    
    """Submenu for operators."""
    
    print("\n--- Operators Menu ---")
    print("Example 1: Basic Arithmetic Operators")
    print('Code: result = 5 + 3\nprint(f"5 + 3 = {result}")')
    print("Output:")
    print("5 + 3 = 8")
    input("Press Enter to return to the main menu...\n")


def conditionals_menu():
    
    """Submenu for conditionals."""
    
    print("\n--- Conditionals Menu ---")
    print("Example 1: If-Else Statement")
    print('Code: age = 18\nif age >= 18:\n    print("Adult")\nelse:\n    print("Minor")')
    print("Output:")
    print("Adult")
    input("Press Enter to return to the main menu...\n")


def loops_menu():
    
    """Submenu for loops."""
    
    print("\n--- Loops Menu ---")
    print("Example 1: For Loop")
    print('Code: for i in range(1, 4):\n    print(f"Number {i}")')
    print("Output:")
    print("Number 1\nNumber 2\nNumber 3")
    input("Press Enter to return to the main menu...\n")


def lists_menu():
    
    """Submenu for lists."""
    
    print("\n--- Lists Menu ---")
    print("Example 1: Iterating Through a List")
    print('Code: fruits = ["Apple", "Banana", "Cherry"]\nfor fruit in fruits:\n    print(fruit)')
    print("Output:")
    print("Apple\nBanana\nCherry")
    input("Press Enter to return to the main menu...\n")


def functions_menu():
    
    """Submenu for functions."""
    
    print("\n--- Functions Menu ---")
    print("Example 1: Defining and Calling a Function")
    print('Code: def greet(name):\n    return f"Hello, {name}!"\n\nprint(greet("Lucena"))')
    print("Output:")
    print("Hello, Lucena!")
    input("Press Enter to return to the main menu...\n")


def run_user_program():
    
    """Allows the user to input and run their Python code."""
    
    print("\n--- Run Your Own Python Program ---")
    print("Type your Python code below. To finish, enter a blank line.")
    user_code = []
    while True:
        line = input()
        if line.strip() == "":
            break
        user_code.append(line)
    try:
        exec("\n".join(user_code))
    except Exception as e:
        print(f"Error executing your code: {e}")
    input("Press Enter to return to the main menu...\n")
    
    
def main_menu():
    
    """ Displays the main menu and navigates to different topics."""
    
    while True:
        print("Interactive Menu Program")
        print("1. Print Statements")
        print("2. Variables")
        print("3. Operators")
        print("4. Conditionals")
        print("5. Loops")
        print("6. Lists")
        print("7. Functions")
        print("8. Run Your Own Python Program")
        print("9. Exit")
        choice = input("Select an option (1-9): ")

        if choice == '1':
            print_statements_menu()
        elif choice == '2':
            variables_menu()
        elif choice == '3':
            operators_menu()
        elif choice == '4':
            conditionals_menu()
        elif choice == '5':
            loops_menu()
        elif choice == '6':
            lists_menu()
        elif choice == '7':
            functions_menu()
        elif choice == '8':
            run_user_program()
        elif choice == '9':
            print("Thank you for using the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

main_menu() # Calls the main function program