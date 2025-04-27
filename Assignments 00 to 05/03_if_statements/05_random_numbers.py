import random

N_NUMBERS = 10
MIN_VALUE = 1
MAX_VALUE = 100

def main():
        value = [random.randint(MIN_VALUE, MAX_VALUE) for i in range(N_NUMBERS)]

        print(f"\n\033[1;32m The 10 random numbers between 1 and 100 are : \033[1;33m{value}\033[0m")

if __name__ == '__main__':
    main()
