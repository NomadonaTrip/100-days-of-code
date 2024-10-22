# Calculator
# add function


def add(n1, n2):
    return n1 + n2


# subtract function
def subtract(n1, n2):
    return n1 - n2


# multiply function
def multiply(n1, n2):
    return n1 * n2


# divide function
def divide(n1, n2):
    """A calculator function that divides the first integer by the   second"""
    return n1 / n2


operators = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}
# Create the banner
from art import logo

print(logo)

# Welcome the user
print("""MyCalculator helps you perform simple arithmetric tasks with two numbers\n""")

# ask the user for the first number
n1 = float(input("What's the first number: "))

use_answer = True
while use_answer:
    for operand in operators:
        print(operand)
    operation_symbol = input("Pick an operation from the line above: ")
    print("\n")
    n2 = float(input("What's the second number: "))
    answer = operators[operation_symbol](n1, n2)
    print(f"{n1} {operation_symbol} {n2} = {answer}\n")
    # Ask user if they want to calculate again using previous answer
    use_answer = input(
        f"""Type 'yes' to run another calculation using {answer} or 'no' to make a fresh calculation\n""")
    if use_answer == "yes":
        n1 = answer

    else:
        print("\n" * 40)
        print(logo)
        n1 = float(input("Type the first number "))


