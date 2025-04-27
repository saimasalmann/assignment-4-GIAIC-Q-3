

def main():
    year = int(input('\nPlease input a year: '))
    if year % 4 == 0 :
        if year % 100 == 0 :
            if year % 400 == 0:
                print("\033[1;32mThat's a leap year!\033[0m")
            else:
                print("\033[1;31mThat's not a leap year.\033[0m")
        else:
            print("\033[1;32mThat's a leap year.\033[0m")        
    else:    
        print("\033[1;31mThat's not a leap year.\033[0m")        

if __name__ == '__main__':
    main()  