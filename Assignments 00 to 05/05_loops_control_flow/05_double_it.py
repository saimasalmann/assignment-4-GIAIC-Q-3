def main():
    user_input = []
    while True:
        try:
            num = input("\nPlease enter a number: ")
            print()
            current_value = int(num)
            break
        except ValueError:
            print("\033[1;31mThat is not a number.Please try again.\033[0m]")
        

    while current_value < 100:
        current_value *= 2
        user_input.append(current_value)
        
    for num in user_input:
        print(f"\033[1;32m{num}\033[0m", end=' ')

    print()    

if __name__ == '__main__':
    main()

