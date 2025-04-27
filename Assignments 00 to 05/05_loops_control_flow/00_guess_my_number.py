import random

def main():
    # Generate the secret number at random!
    secret_number = random.randint(1, 99)
    print("\n\033[1;35m****** Welcome to the Guess My Number Game ******\033[0m\n")
    print("I am thinking of a number between 1 and 99...\n")
    
    # Get user's guess
    guess = int(input("Enter a guess: "))
    # True if guess is not equal to secret number
    while guess != secret_number:
        if guess < secret_number:  # If-statement is True if guess is less than secret number
            print("\033[1;33mYour guess is too low\033[0m")
        else:
            print("\033[1;35mYour guess is too high\033[0m")
            
        print() # Print an empty line to tidy up the console for new guesses
        guess = int(input("Enter a new guess: "))  # Get a new guess from the user
        
    print("\033[1;32mCongrats! You guessed the correct number.\033[0m" )
    
if __name__ == '__main__':
    main()