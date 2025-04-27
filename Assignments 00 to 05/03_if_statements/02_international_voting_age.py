
PETURKSBOUIPO_AGE : int = 16
STANLAU_AGE : int = 25
MAYENGUA_AGE : int = 48

def main():
    voter_age = int(input("\nHow old are you? "))
    if voter_age >= PETURKSBOUIPO_AGE:
        print(f"\033[1;32mYou can vote in Peturksbouipo where the voting-age is {PETURKSBOUIPO_AGE}.\033[0m")
    else:
        print(f"\033[1;31mYou cannot vote in Peturksbouipo where the voting-age is {PETURKSBOUIPO_AGE}.\033[0m")
    if voter_age >= STANLAU_AGE:
        print(f"\033[1;32mYou can vote in Stanlau where the voting-age is {STANLAU_AGE}.\033[0m")
    else:
        print(f"\033[1;31mYou cannot vote in Stanlau where the voting-age is {STANLAU_AGE}.\033[0m")
    if voter_age >= MAYENGUA_AGE:
        print(f"\033[1;32mYou can vote in Mayengua where the voting-age is {MAYENGUA_AGE}.\033[0m")
    else:
        print(f"\033[1;31mYou cannot vote in Mayengua where the voting-age is {MAYENGUA_AGE}.\033[0m")
    print("\n")

if __name__ == '__main__':  
    main()