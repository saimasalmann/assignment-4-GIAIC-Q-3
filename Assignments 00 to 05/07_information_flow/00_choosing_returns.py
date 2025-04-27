# ADULT_AGE = 18
# def is_adult(age:int):
#     if age>= ADULT_AGE:
#         return True
#     else:
#         return False
    

# def main():
#     age = int(input("please enter your age: "))
#     print(is_adult(age))    

# if __name__ == "__main__":
#     main()    


ADULT_AGE : int = 18 # U.S. age 

def is_adult(age: int):
    if age >= ADULT_AGE:
        return True
    
    return False
    
########## No need to edit code beyond this point :) ##########

def main():
    while True:
        try:
            age : str = int(input("How old is this person?: "))
            break
        except ValueError:
            print("\n\033[1;31mInvalid input. Please enter a valid integer.\033[0m")
    print(is_adult(age))
    

if __name__ == "__main__":
    main()