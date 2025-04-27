

def get_user_input():
    print("\n")
    user_nums = []
    while True:
        user_input = input("Enter a number or press enter to stop: ")
        if user_input == "" :
            break
        num = int(user_input)
        user_nums.append(num)
    return user_nums

def num_count(user_nums):
    num_dict = {}
    for num in user_nums:
        if num not in num_dict:
            num_dict[num] = 1
        else:
            num_dict[num] += 1
    return num_dict

def print_nums(num_dict):
    for num in num_dict:
        print(f"\n\033[1;34m{num}\033[0m  appears\033[1;33m {num_dict[num]}\033[0m times.")

def main():
    user_input = get_user_input()
    num_dict =num_count(user_input)
    print_nums(num_dict)

if __name__ == '__main__':
    main()    
            



    
    



