
def double(num:int):
    return num*2

def main():
    while True:
   
        try:
            num = int (input("\nPlease enter a number: "))
            result = double(num)    
            print(f"The double of \033[1;33m{num}\033[0m  is  \033[1;32m{result}\033[0m.")
            break
        except ValueError:
         print("\n\033[1;31mInvalid input. Please enter a valid integer.\033[0m")



if __name__ == "__main__":
    main()    