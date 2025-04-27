
MINIMUM_HEIGHT : int = 50 

def main():
    height = float(input("\nPlease enter your height . "))
    if height >= MINIMUM_HEIGHT:
        print(f"\n\033[1;32mYou are tall enough to ride the roller coaster!\033[0m")
    else:
        print(f"\n\033[1;31mYou are not tall enough to ride the roller coaster.\033[0m")
    

if __name__ == '__main__':
    main()    