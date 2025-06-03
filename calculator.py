import art
print(art.logo)

def add(n1, n2):
    return n1 + n2

def subtract(n1,n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    if n2 == 0:
        print("Invalid value undefined")
        return None
    return n1/n2

operations = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide,
}

def calculator():
    should_accumulate = True
    f_number = float(input("Enter first number\n"))
    while should_accumulate:

        for operator in operations:
            print(operator)
        operations_of_choice = input("Enter one of four operations\n")
        s_number = float(input("Enter your second number\n"))

        if operations_of_choice in operations:
            result = operations[operations_of_choice](f_number,s_number)
            print(f"The result of {f_number} {operations_of_choice} {s_number} is: {result}")
            choice = input(f"Type 'y' to continue calculating with {result}, or 'n' to stop")
            if choice == "y":
                f_number = result
            else:
                should_accumulate =False
                print("\n" * 20)
                calculator()
        else:
            print("Please enter a valid operation")

calculator()