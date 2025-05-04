


def access_element(lst,index):
    try:
        return lst[index]
    except IndexError:
        return "Index out of range."
    
def modify_element(lst,index,new_value):
    try:
        lst[index] = new_value
        return lst   
    except IndexError:
        return "Index out of range."

def slice_list(lst ,start,end):
    try:
        return lst[start:end]   
    except IndexError:
        return "Invalid indices."
def get_integer(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("\033[1;31mInvalid input!\033[0m Please enter a valid integer.")


def index_game():
    print("\033[48;5;154mWelcome to index Game\033[0m\n")
    lst = [2,4,6,8,10]  # Example list
    print(f"\nCurrent List : {lst}")
    print("\nPlease choose an operation : access , modify ,slice")

    operation = input("Enter operation : ").lower()

    while operation != "access" and operation != "modify" and operation != "slice":
        operation = input("\033[1;31mInvalid input!\033[0m Please enter either 'access', 'modify', or 'slice'_____").lower()
    
    if operation == "access":
        index = get_integer("Enter index to access : ")
        print(f"\nThe element you accesssed : {access_element(lst,index)}")
    
    elif operation == "modify":
        index = get_integer("enter index to modify : ")
        new_value = input("Enter new value : ")
        print(f"\nYour modified List : {modify_element(lst,index,new_value)}")
    
    elif operation == "slice":
        start = get_integer("Enter start index : ")
        end = get_integer("Enter end index : ")
        print(f"\nYour sliced List : {slice_list(lst ,start,end)}")


index_game()        
