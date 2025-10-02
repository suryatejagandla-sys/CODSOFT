# Simple Calculator (CLI)
def calc():
    print("Simple Calculator")
    try:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
    except:
        print("Invalid number.")
        return
    print("Operations: + - * / ^ (power) % (modulo)")
    op = input("Choose operation: ").strip()
    if op == "+":
        print("Result:", a+b)
    elif op == "-":
        print("Result:", a-b)
    elif op == "*":
        print("Result:", a*b)
    elif op == "/":
        if b==0:
            print("Division by zero!")
        else:
            print("Result:", a/b)
    elif op == "^":
        print("Result:", a**b)
    elif op == "%":
        print("Result:", a % b)
    else:
        print("Unknown operation.")

if __name__ == '__main__':
    calc()
