# This program should be able to add, subtract, multiply, or divide any two numbers input by the user.

# Creates a function called add that adds 2 numbers.
def add(x, y):
    return x + y


# Creates a function called subtract that subtracts 2 numbers.
def subtract(x, y):
    return x - y


# Creates a function called multiply that multiplies 2 numbers.
def multiply(x, y):
    return x * y


# Creates a function called divide that divides 2 numbers.
def divide(x, y):
    return x / y


print("Select desired operation.")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

while True:
    # Prompt user input.
    choice = input("Enter number that corresponds to desired operation: (1/2/3/4): ")

    # If statement that checks if the input is one of the 4 options.
    if choice in ('1', '2', '3', '4'):
        # Creating a prompt for the user for the two numbers that the user wants to use.
        number1 = float(input("Enter first number: "))
        number2 = float(input("Enter second number: "))
# if statement for the 4 options, if it is the correct option then it will print the corresponding #'s and symbols.
        if choice == '1':
            print(number1, "+", number2, "=", add(number1, number2))

        elif choice == '2':
            print(number1, "-", number2, "=", subtract(number1, number2))

        elif choice == '3':
            print(number1, "*", number2, "=", multiply(number1, number2))

        elif choice == '4':
            print(number1, "/", number2, "=", divide(number1, number2))
        break
    else:
        print("Invalid selection, please choose 1, 2, 3, or 4.")
        # Extra option for if someone doesn't choose 1, 2, 3, 4.


