def print_even_number():
    print("\n")
    for i in range(20):
        print(f"\033[1;33m {i*2} \033[0m", end="   ")


if __name__ == '__main__':
    print_even_number()        
    print("\n")
