
BOLD_ITALICS = "\033[1;3m"
UNDERLINE = "\033[4m"
RESET = "\033[0m"




def main():
    dividend:float = float(input("\nPlease enter a number to be divided! "))
    divisor : float = float(input("Please enter the number to divide by! "))
    quotient : int = int(dividend // divisor)
    remainder : int = int(dividend % divisor)

    print(f"{BOLD_ITALICS}{dividend}{RESET} divided by {BOLD_ITALICS}{divisor}{RESET} = {quotient}  , remainder = {remainder}")

if __name__ == "__main__":
    main()    