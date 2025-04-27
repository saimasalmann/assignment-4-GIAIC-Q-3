def count_evens(lst):
    """
    This function takes a list of integers and returns the count of even numbers in the list.
    """
    count = []
    for num in lst:
        if num % 2 == 0 :
            count += 1
    print(count)        


def get_int_list():
    """
    This function prompts the user to enter a list of integers and returns the list.
    """
    lst = []

    user_int = input("Please enter a number or press enter to stop: ")
    while user_int != "":
        lst.append(int(user_int))
        user_int = input("Please enter a number or press enter to stop: ")
    return lst

def main():
    """
    Main function to execute the program.
    """
    lst = get_int_list()
    count_evens(lst)


if __name__ == "__main__":
    main()