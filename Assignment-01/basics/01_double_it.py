def double_it(curr_value):
    curr_value = 2 * curr_value 
    return curr_value

def main():
    while True:
        try:
            curr_value = int(input("\nEnter a number: "))
            
            if curr_value >= 100:
                print("\n\033[1;31mThe number is already 100 or more.\033[0m")
                continue
            break

        except ValueError:
            print("\n\033[1;31mPlease enter a valid number.\033[0m")    
 
    while curr_value < 100:
        curr_value = double_it(curr_value)
        print(curr_value)
if __name__ == "__main__":
    main()
