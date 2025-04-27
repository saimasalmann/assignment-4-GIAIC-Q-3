import random

NUM = 10 
MAX_NUM = 100
MIN_NUM = 1



def main():

    random_numbers = [random.randint(MIN_NUM, MAX_NUM) for i in range(NUM)]
    print(f"\n\033[1;32m The 10 random numbers between 1 and 100 are : \033[1;33m{random_numbers}\033[0m")


if  __name__ == '__main__':
    main()    