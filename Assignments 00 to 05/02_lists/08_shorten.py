

max_length :int = 2
def shorten_length(lst: list):
    """
    Shorten the length of a list to max_length.
    """
    while len(lst) > max_length:
        removed_element = lst.pop()
        print(f"The removed element is : \033[1;34m{removed_element}\033[0m")

def get_list():
    """
    Prompts the user to enter one element of the list at a time and returns the resulting list.
    """
    lst = []
    elem = input("\nPlease enter the element to add to the list or press enter to stop. ")
    while elem != "":
        lst.append(elem)
        elem = input("Please enter the element to add to the list or press enter to stop. ")
    return lst

def main():
    lst = get_list()
    shorten_length(lst)
    print(f"\033[1;32mThe shortened list is : {lst}\033[0m")


if __name__ == '__main__':
    main()