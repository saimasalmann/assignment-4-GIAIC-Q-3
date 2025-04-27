
def main():
    print("\n^^^^^^^ Welcome to the Square Calculator^^^^^^^")

    num: float = float(input("\nType a number to see its square: ")) # Make sure to cast the input to a float so we can do math with it!
    print(f"The square of {num} is  {num*num}") # num * num is equivalent to num ** 2. The ** operator raises something to a power!


# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()
