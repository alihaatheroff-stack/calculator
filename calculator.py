# calculator.py

import math

def add(a, b):
    """Add two numbers"""
    return a + b


def subtract(a, b):
    """Subtract b from a"""
    return a - b


def multiply(a, b):
    """Multiply two numbers"""
    return a * b


def divide(a, b):
    """Divide a by b"""
    if b == 0:
        raise ValueError("Cannot divide by zero!")
    return a / b
import math


def square_root(a):
    """Calculate square root of a number"""
    if a < 0:
        raise ValueError("Cannot calculate square root of negative number!")
    return math.sqrt(a)

def calculator():
    """Main calculator function - interactive menu"""
    print("=" * 30)
    print("   Simple Python Calculator")
    print("=" * 30)
    print("Operations:")
    print("  1. Add")
    print("  2. Subtract")
    print("  3. Multiply")
    print("  4. Divide")
    print("  5. Square Root")
    print("  6. Exit")        # change 5 to 6
    print("=" * 30)

    while True:
        choice = input("\nEnter choice (1/2/3/4/5): ")

        if choice == '5':
            print("Goodbye!")
            break

        if choice not in ['1', '2', '3', '4','5']:
            print("Invalid choice! Please enter 1-5.")
            continue

        try:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input! Please enter numbers only.")
            continue

        if choice == '1':
            print(f"Result: {a} + {b} = {add(a, b)}")
        elif choice == '2':
            print(f"Result: {a} - {b} = {subtract(a, b)}")
        elif choice == '3':
            print(f"Result: {a} x {b} = {multiply(a, b)}")
        elif choice == '4':
            try:
                print(f"Result: {a} / {b} = {divide(a, b)}")
            except ValueError as e:
                print(f"Error: {e}")
        elif choice == '5':
            try:
                print(f"Result: √{a} = {square_root(a)}")
            except ValueError as e:
                print(f"Error: {e}")

if __name__ == "__main__":
    calculator()
