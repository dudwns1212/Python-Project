def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

calculate = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide
}

import art
print(art.logo)

is_continue = "Continue"
while True:
    if is_continue == "Continue":
        num1 = int(input("Enter first number: "))

    operation = input("Enter operation\n+\n-\n*\n/: ")
    num2 = int(input("Enter second number: "))

    result = calculate[operation](num1, num2)
    print(result)

    continue_key = input("Press any key to continue...y/n : ")
    if continue_key == "y":
        num1 = result
        is_continue = "Pass"
    else:
        is_continue = "Continue"