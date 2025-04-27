def get_last_elem(list):
    """
    Prints the last element of a provided list.
    """
    print(f"\033[1;32m The last element of the list : {list[-1]}\033[0m")

def get_list():
    """ Prompts the user to enter one element of the list at a time and returns the resulting list. """
    lst =[]
    element = input("Please enter an element of the list or press enter to stop. ")
    while element != "":
        lst.append(element)
        element = input("Please enter an element of the list or press enter to stop. ")
    return lst

def main():
    lst = get_list()
    if len(lst) == 0:
        print("\033[1;31m The list is empty \033[0m")
    else:
        get_last_elem(lst)


if __name__ == '__main__':
    main()    
