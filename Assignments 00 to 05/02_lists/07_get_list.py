def main():
    lst = []
    val = input("Please enter an element of the list or press enter to stop. ")
    while val:
        lst.append(val)
        val = input("Please enter an element of the list or press enter to stop. ")

    print(f"\033[1;34mYour list is here : {lst}\033[0m")
    
if __name__ == '__main__':  
    main()    