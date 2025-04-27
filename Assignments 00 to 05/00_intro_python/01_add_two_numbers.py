"""
Program: add2numbers
--------------------
Another python program to get some practice with
variables.  This program asks the user for two
integers and prints their sum.
"""


def main():
    print("""\n-----------------------------
This program adds two numbers.""")
    print("-----------------------------")
    num1 : str = input("\nEnter first number: ")
    num1 : int = int(num1)
    num2  : str = input("Enter second number: ")
    num2 : int = int(num2)
    total : int = num1 + num2
    print(f"\nThe sum of {num1} and {num2} is {total}.")


if __name__ == '__main__':
    main()