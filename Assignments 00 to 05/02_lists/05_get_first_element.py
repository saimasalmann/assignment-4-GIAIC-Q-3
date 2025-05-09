
def get_first_element(lst):
    """
    Prints the first element of a provided list.
    """

    print(f"\033[1;32m The first element f the list : {lst[0]}'\033[0m")

# There is no need to edit code beyond this point

def get_lst():
    """
    Prompts the user to enter one element of the list at a time and returns the resulting list.
    """
    lst = []
    elem: str = input("Please enter an element of the list or press enter to stop. ")
    while elem != "":
        lst.append(elem)
    return lst

def main():
    lst = get_lst()
    get_first_element(lst)


if __name__ == '__main__':
    main()

