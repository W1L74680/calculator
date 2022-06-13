def calculate():
    a = int(input("enter a number: "))
    b = int(input("enter another number: "))
    op = input("enter an operation: ")
    if op == "+":
        print(a+b)
    elif op == "-":
        print(a-b)
    elif op == "*":
        print(a*b)
    elif op == "/":
        print(a/b)

calculate()