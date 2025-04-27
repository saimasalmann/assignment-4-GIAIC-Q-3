# def main():
#     for i in range(10):
#         if is_odd(i):
#             print(f'{i} is odd.')
#         else:
#             print(f'{i} is even.')
            
# def is_odd(value: int):
#     """
#     Checks to see if a value is odd. If it is, returns true.
#     """
    
#       # 0 if value is divisible by 2, 1 if it isn't
#     return  value % 2 == 1


# # There is no need to edit code beyond this point

# if __name__ == '__main__':
#     main()
 
#     ************** other version using generator function***************


import time

def is_even(value:int):
    return value % 2 == 0

def generate_odd_even_list(limit:int):
    for i in range(limit):
        if is_even(i):
            yield (f"{i} is Even........")    
        else:    
            yield (f"{i} is Odd........")

def main():
    print("\n\033[1;35mWelcome to the Odd or Even Checker!\033[0m\n")
    for i in generate_odd_even_list(10):
        print(i)   
        time.sleep(1)         

if __name__ == "__main__":
    main()            
