AFFIRMATION : str = "I am capable of doing anything I put my mind to."

def main():
    print("\n\033[1;35mPlease type the following affirmation: " + "\033[1;3m{AFFIRMATION}\033[0m\n")

    user_feedback = input()  # Get user's input
    while user_feedback != AFFIRMATION:  # While the user's input isn't the affirmation
        # Tell the user that they did not type the affirmation correctly
        print("\033[1;31mThat was not the affirmation.\033[0m")

        # Ask the user to type the affirmation again!
        print("\n\033[1;35mPlease type the following affirmation: " + "\033[1;3m{AFFIRMATION}\033[0m\n")

        user_feedback = input()

    print("\n\033[1;32mThat's right! :\033[0m")  # Tell the user they typed the affirmation correctly]")


# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()