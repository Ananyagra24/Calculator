def sum(a,b):
    return a + b

def diff(a,b):
    return a - b

def prod(a,b):
    return a * b

def div(a,b):
    if b == 0:
        return "ERROR! Division by zero."
    return a / b

print("This is a simple calculator.\n")
print("The available operations are '+', '-', '*', '/'.\n")
print("Type 'exit' to to quit.\n")

while True:
    operation = input("Enter operation ('+', '-', '*', '/') or 'exit' to quit: ").strip()

    if operation.lower() == 'exit':
        print("Exiting calculator.")
        break

    if operation not in ('+', '-', '*', '/'):
        print("Invalid operation. Please try again.\n")
        continue

    try:
        num1 = float(input("Enter the first number: ").strip())
        num2 = float(input("Enter the second number: ").strip())

    except ValueError:
        print("Invalid input. Please enter numeric values.\n")
        continue

    match operation:
        case '+':
            result = sum(num1, num2)
        
        case '-':
            result = diff(num1, num2)

        case '*':
            result = prod(num1, num2)

        case '/':
            result = div(num1, num2)

    print(f"Result: {result}\n")