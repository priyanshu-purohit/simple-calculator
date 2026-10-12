#!/usr/bin/env python3
# Simple CLI calculator: supports +, -, *, /, %, and power (**)

"""calculator.py

Run: python3 calculator.py
"""

def get_number(prompt):
    while True:
        try:
            return float(input(prompt).strip())
        except ValueError:
            print("Please enter a valid number.")


def add(a, b): return a + b

def sub(a, b): return a - b

def mul(a, b): return a * b

def div(a, b):
    if b == 0:
        raise ZeroDivisionError("Division by zero")
    return a / b

def mod(a, b):
    if b == 0:
        raise ZeroDivisionError("Modulo by zero")
    return a % b

def power(a, b): return a ** b

ops = {
    "+": ("Add", add),
    "-": ("Subtract", sub),
    "*": ("Multiply", mul),
    "/": ("Divide", div),
    "%": ("Modulo", mod),
    "**": ("Power", power),
}

def print_menu():
    print("\nSimple Calculator")
    for sym, (name, _) in ops.items():
        print(f"  {sym:>2}  {name}")
    print("  h   Help (show this menu)")
    print("  q   Quit\n")


def main():
    print_menu()
    while True:
        cmd = input("Enter operation (e.g. +, -, *, /, %, **), h, or q: ").strip()
        if not cmd:
            continue
        if cmd.lower() == "q":
            print("Goodbye.")
            break
        if cmd.lower() == "h":
            print_menu()
            continue
        if cmd not in ops:
            print("Unknown operation. Type 'h' for help.")
            continue
        a = get_number("Enter first number: ")
        b = get_number("Enter second number: ")
        fn = ops[cmd][1]
        try:
            result = fn(a, b)
        except ZeroDivisionError as e:
            print("Error:", e)
            continue
        # print integer-looking results without .0
        if isinstance(result, float) and result.is_integer():
            result = int(result)
        print(f"Result: {result}")

if __name__ == "__main__":
    main()
