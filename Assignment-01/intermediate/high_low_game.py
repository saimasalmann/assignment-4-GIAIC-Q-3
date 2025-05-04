import random

rounds = 5
def play_game():
    print("\n\033[48;5;153mWelcome to the High-Low Game!\033[0m")
    print("_____________________________") 
    score = 0
    
    
    for i in range(rounds):
        comp_num : int = random.randint(1,100)
        your_num : int = random.randint(1,100)
        
        print(f"\n\033[1;35mRound {i + 1} >>>>>>>>>>>>>>>>>>>>\033[0m")
        print(f"\nYour number is {your_num} ....")
        
        choice  = input(f"What do you think your number is higher or lower than computer's number? (higher/lower) ").lower()
        
        while choice != "higher" and choice != "lower": 
            choice = input("\033[1;31mInvalid input!\033[0m Please enter either 'higher' or 'lower'.").lower()
            
        if choice == "higher" and your_num > comp_num or choice == "lower" and your_num < comp_num:
            print(f"\033[1;32mYour guess is correct ! Your number is {your_num}, computer's number is {comp_num}.\033[0m")
            score += 1
            print(f"Your score is {score} .")
        else:
            print(f"\033[1;33mAww! Your guess is wrong ! Your number is {your_num}, computer's number is {comp_num}.\033[0m ")
            print(f"Your score is {score} .")
    print()
    if score == rounds:
        print("\033[1;32mCongratulations! You guessed all rounds correctly!\033[0m")
    elif score >= rounds//2:
        print("\033[1;33mGood job! You guessed more than half of the rounds correctly.\033[0m")
    else:
        print("\033[48;5;208mBetter luck next time!\033[0m")

    print(f"\nGame Over! Your final score is {score} for {rounds} rounds.")
    print("\n\033[48;5;104mThank you for playing!\033[0m")

if __name__ == "__main__":
    play_game()