#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    from sys import argv
    if len(argv) != 4:
        print("Usage: {} <a> <operator> <b>".format(argv[0]))
        exit(1)
    a = int(argv[1])
    operator = argv[2]
    b = int(argv[3])
    if operator not in ("+", "-", "*", "/"):
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    if operator == "+":
        result = add(a, b)
    elif operator == "-":
        result = sub(a, b)
    elif operator == "*":
        result = mul(a, b)
    else:
        result = div(a, b)
    print("{} {} {} = {}".format(a, operator, b, result))
