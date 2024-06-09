import math 

def add(x,y):
    """Reurn the sum of x and y."""
    return x + y

def subtract(x,y):
    """Return the difference of x and y."""
    return x - y

def multiply(x,y):
    """Return the product of x and y."""
    return x * y

def divide(x,y):
    """Return the quotient of x and y."""
    if y == 0:
        raise ValueError("Cannot divide by zero.")
    return x / y

def main():
    """Main function to run the calculator."""
    while True:
        print("\nSelect operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit") 

        # Get user input
        choice = input("Enter choice (1/2/3/4/5): ")

        # Check if user wants to exit
        if choice == '5':
            print("Exiting the calculator. Goodbye!")   
            break
    
        # Validate choice
        if choice in ('1', '2', '3', '4'):
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            # Perform the corresponding operation and print the result
            if choice == '1':
                print(f"{num1} + {num2} = {add(num1, num2)}")
            elif choice == '2':
                print(f"{num1} - {num2} = {subtract(num1, num2)}")
            elif choice == '3':
                print(f"{num1} * {num2} = {multiply(num1, num2)}")
            elif choice == '4':
                print(f"{num1} / {num2} = {divide(num1, num2)}")
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()