def print_divisors(num:int):

    # divisors = []
    # for i in range(num):
    #     current_divisor = i + 1
    #     if num % current_divisor == 0 :
    #             # print(f"{current_divisor} is a divisor of {num}.")
    #         divisors.append(current_divisor)

    divisors = [ i for i in range(1 , num + 1) if num % i == 0 ]
    print(f"\nThe divisors of \033[1;34m{num}\033[0m are: \033[1;32m{divisors}\033[0m.")


def main():
    while True:
        try:
            num = int(input("\nPlease enter a number: "))
            print_divisors(num)
            break
        except ValueError:
            print("\n\033[1;31mInvalid input. Please enter a valid integer.\033[0m")


if __name__ == "__main__":
    main()                        