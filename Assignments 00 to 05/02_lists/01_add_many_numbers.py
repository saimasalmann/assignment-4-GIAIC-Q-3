def add_many_numbers(numbers):
    """
    Takes in a list of numbers and returns the sum of those numbers.
    """

    total: int = 0
    for number in numbers:
        total += number

    return total

# There is no need to edit code beyond this point

def main():
    numbers: list[int] = [1, 2, 3, 4, 5]  # Make a list of numbers
    sum_of_numbers: int = add_many_numbers(numbers)  # Find the sum of the list
    print(f"The sum of all numbers is : \033[1;32m{sum_of_numbers}\033[0m")  # Print out the sum above
    

if __name__ == '__main__':
    main()